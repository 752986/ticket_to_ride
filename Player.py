from Route import Route
from TrainColor import TrainColor

class Player:
	score: int
	hand: list[int] # each index corresponds to one train color; it stores the amount of that color
	trains: int # the number of plastic trains left
	routes: list[Route] # the route cards currently held

	def __init__(self):
		self.score = 0
		self.hand = [0 for i in TrainColor]
		self.trains = 45

	def change_card(self, color: TrainColor, amount: int = 1):
		self.hand[color.value] += amount

	def remove_train(self, amount: int = 1):
		self.trains -= amount

	def change_score(self, amount: int):
		self.score += amount

	def turn(self):
		pass
	