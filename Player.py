from TrainColor import TrainColor

class Player:
	score: int
	hand: list[int] # each index corresponds to one train color; it stores the amount of that color
	trains: int # the number of plastic trains left
	routes: list[Route] # the route cards currently held
	