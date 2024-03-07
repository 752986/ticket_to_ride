from Ticket import Ticket
from TrainColor import TrainColor

class Player:
	name: str
	score: int
	hand: list[int] # each index corresponds to one train color; it stores the amount of that color
	trains: int # the number of plastic trains left
	tickets: list[Ticket] # the ticket cards currently held

	def __init__(self, name: str):
		self.name = name
		self.score = 0
		self.hand = [0 for _ in TrainColor]
		self.trains = 45
		self.tickets = []

	def add_cards(self, color: TrainColor, amount: int = 1):
		self.hand[color.value] += amount

	def remove_train(self, amount: int = 1):
		self.trains -= amount

	def change_score(self, amount: int):
		self.score += amount

	def turn(self):
		pass
	