from Board import Board
from TrainColor import TrainColor
from Ticket import Ticket
from Player import Player

class GameState:
	# board state, players, draw piles, APIs for player actions, 
	board: Board # the game board
	draw_pile: list[TrainColor] # the draw pile for train cards
	visible_pile: list[TrainColor] # the 5 face-up cards
	ticket_pile: list[Ticket] # the draw pile for destination ticket cards
	players: list[Player] # the players in the game
	current_turn: int # the current player number
	