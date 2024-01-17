from TrainColor import TrainColor

class Connection:
	start: str
	end: str
	length: int
	color: TrainColor
	taken: bool

	def __init__(self, start: str, end: str, length: int, color: TrainColor):
		self.start = start
		self.end = end
		self.length = length
		self.color = color
		self.taken = False
