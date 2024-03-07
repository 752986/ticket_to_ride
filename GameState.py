from Board import Board
from TrainColor import TrainColor
from Ticket import Ticket
from Player import Player
import random

class GameState:
	# board state, players, draw piles, APIs for player actions, 
	board: Board # the game board
	draw_pile: list[TrainColor] # the draw pile for train cards
	visible_pile: list[TrainColor] # the 5 face-up cards
	discard_pile: list[TrainColor] # the cards that have been discarded
	ticket_pile: list[Ticket] # the draw pile for destination ticket cards
	players: list[Player] # the players in the game
	current_turn: int # the current player number

	def _draw(self, amount: int = 1) -> list[TrainColor]:
		'''Draw the specified number of cards from the draw pile, reshuffling the discard pile if needed.'''
		result: list[TrainColor] = []
		for _ in range(amount):
			if len(self.draw_pile) == 0:
				self.draw_pile = self.discard_pile.copy()
				self.discard_pile.clear()
				random.shuffle(self.draw_pile)
			result.insert(0, self.draw_pile.pop()) # inserting rather than appending to preserve card order, idk if this is needed

	def _discard(self, color: TrainColor, amount: int = 1):
		self.discard_pile.extend((color for _ in range(amount)))

	def claim(self, start: str, end: str, color: TrainColor):
		'''Claims the specified route for the current player, spending the correct amount of resources.'''
	
	def draw_blind(self, amount: int = 1):
		'''Draws the specified number of cards from the draw pile into the current player's hand.'''
	
	def draw_visible(self, color: TrainColor):
		'''Draws the specified card from the face-up pile into the current player's hand.'''

	def draw_tickets(self, amount: int) -> list[Ticket]:
		'''Draws the specified number of tickets from the ticket draw pile and returns them.
		Note that unlike the other draw methods, this doesn't add them to the current player.
		This is done so that the player may choose which ones to keep.
		'''