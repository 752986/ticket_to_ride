from Board import Board
from TrainColor import TrainColor
from Route import Route
from Ticket import Ticket
from Player import Player
import random

class GameState:
	# board state, players, draw piles, APIs for player actions, 
	
	class InvalidAction(Exception):
		'''A player action was attempted that the player cannot do.'''
	
	board: Board # the game board
	draw_pile: list[TrainColor] # the draw pile for train cards
	visible_pile: list[TrainColor] # the 5 face-up cards
	discard_pile: list[TrainColor] # the cards that have been discarded
	ticket_pile: list[Ticket] # the draw pile for destination ticket cards
	players: list[Player] # the players in the game
	current_turn: int # the current player number

	def _draw(self, amount: int = 1) -> list[TrainColor]:
		'''Draws the specified number of cards from the draw pile, reshuffling the discard pile if needed.'''

		result: list[TrainColor] = []
		for _ in range(amount):
			if len(self.draw_pile) == 0:
				self.draw_pile = self.discard_pile.copy()
				self.discard_pile.clear()
				random.shuffle(self.draw_pile)
			result.insert(0, self.draw_pile.pop()) # inserting rather than appending to preserve card order, idk if this is needed

		return result

	def _discard(self, color: TrainColor, amount: int = 1):
		'''Adds the specified number of cards to the discard pile.
		If discarding multiple colors, this method will need to be called multiple times.
		'''

		self.discard_pile.extend((color for _ in range(amount)))
	
	def current_player(self) -> Player:
		return self.players[self.current_turn]

	def can_claim(self, route: Route) -> list[int | None]:
		'''Checks whether the current player has the resources necessary to claim `route`. 

		Returns a list where each index corresponds to a TrainColor. If the player can't use a color
		to complete the route, that index will contain `None`. Otherwise, it will contain the minimum
		number of supplementary wild cards that are needed (`0` if it can be completed using solid colors alone).

		To summarize, for each slot in the returned list:
		- `None` means that the current player can't fulfill `route` with their current resources.
		- `0` means that they can fulfill the route using just cards of that slot's color.
		- Another value means that they can fulfill the route, but they would need to use that many wild cards.

		Note that:
		- even if the color matches, an index may still be `None` if the player doesn't have enough wild cards.
		- this function does not take into account the player's remaining supply of plastic trains.
		- the result in index 8 (wild cards) will always be `None` or `0`.
		'''

		# thinking:
		# ideally this gives 2 pieces of info:
		# 1. for a gray route, which colors can be used to fill it?
		# 2. for each of those colors (or just the one if it's a colored route), how many rainbow cards need to be played to complete it?

		player = self.current_player()

		result: list[int | None] = [None for _ in TrainColor]

		for color in TrainColor:
			if route.color != TrainColor.Wild and color != TrainColor.Wild and route.color != color:
				continue

			if player.query_cards(color) >= route.length:
				result[color.value] = 0
			elif (
				color != TrainColor.Wild and 
				player.query_cards(color) + player.query_cards(TrainColor.Wild) >= route.length
			):
				result[color.value] = route.length - (player.query_cards(color))

		return result

	def claim(self, start: str, end: str, route_color: TrainColor, play_color: TrainColor | None = None, num_wild: int = 0):
		'''Claims the specified route for the current player, spending the correct amount of resources.
		`color` is the color of the route to be claimed. If it's wild, `play_color` specifies the color of cards played.
		`play_wild` specifies the number of wild cards to be used (defaults to 0).
		'''

		# argument validation
		if route_color != TrainColor.Wild and play_color != None:
			raise ValueError("`play_color` should not be set unless `route_color` is wild.")
		elif route_color == TrainColor.Wild and play_color == None:
			raise ValueError("`play_color` must be set when `route_color` is wild.")

		# use route color if not on a gray route
		if play_color == None:
			play_color = route_color

		player = self.current_player()

		# find matching free route
		possible = self.board.find(start, end, color=route_color, claimed=False)
		if len(possible) == 0:
			raise GameState.InvalidAction(f"No unclaimed routes found between {start} and {end} with color {route_color.name}.")
		
		route = possible[0]

		# determine number of color and wild cards being used
		num_color = route.length - num_wild

		# ensure not too many wild cards are being used
		if num_color < 0 or num_wild < 0:
			raise ValueError(f"Invalid number of wild cards ({num_wild} on route length {route.length}).")

		can_play = self.can_claim(route)[play_color.value]

		# if `can_play` is None there is no way to complete the route with this color 
		if can_play == None:
			raise GameState.InvalidAction(f"The route can't be claimed using {play_color.name}.")
		
		# past this point we know that the player has enough to claim the route, as long as enough wild cards are used
		if num_wild < can_play:
			raise GameState.InvalidAction(f"At least {can_play} wild cards must be used to claim this route using {play_color.name}.")
		
		# and past this point we know that that is indeed the case, so the last thing to check is plastic trains
		if player.trains < route.length:
			raise GameState.InvalidAction("The player doesn't have enough trains left to complete the route.")

		# put the claim into effect
		route.claim(self.current_turn)

		player.remove_cards(play_color, num_color)
		player.remove_cards(TrainColor.Wild, num_wild)
		player.remove_trains(route.length)
		player.change_score(route.value())
	
	def draw_blind(self, amount: int = 1):
		'''Draws the specified number of cards from the draw pile into the current player's hand.'''
		cards = self._draw(amount)
		for card in cards:
			self.current_player().add_cards(card)
	
	def draw_visible(self, color: TrainColor):
		'''Draws the specified card from the face-up pile into the current player's hand, replacing it.'''

		if color not in self.visible_pile:
			raise GameState.InvalidAction(f"{color} is not present in the face-up draw pile.")
		
		self.visible_pile.remove(color)
		self.visible_pile.append(self._draw()[0])
		self.current_player().add_cards(color)

	def draw_tickets(self, amount: int) -> list[Ticket]:
		'''Draws the specified number of tickets from the ticket draw pile and returns them.
		Note that unlike the other draw methods, this doesn't add them to the current player.
		This is done so that the player may choose which ones to keep.
		'''

		if len(self.ticket_pile) < amount:
			raise GameState.InvalidAction(f"There are not enough tickets in the pile ({amount} requested, {len(self.ticket_pile)} available).")
		
		result: list[Ticket] = []
		for _ in range(amount):
			result.append(self.ticket_pile.pop())

		return result
	
	def decide_tickets(self, tickets: list[Ticket], keep: list[bool]):
		'''For each ticket in `tickets`, either adds it to the current player's hand, or puts it back into the draw pile, 
		depending on whether `keep` at the same index is true or false, respectively.
		'''

		if len(tickets) != len(keep):
			return ValueError("The lengths of `tickets` and `keep` must match.")
		
		player = self.current_player()

		for ticket, should_keep in zip(tickets, keep):
			if should_keep:
				player.add_ticket(ticket)
			else:
				self.ticket_pile.insert(random.randint(0, len(self.ticket_pile)), ticket) # replace it at a random position
		