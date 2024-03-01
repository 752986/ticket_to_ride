from TrainColor import TrainColor

class Route:
	start: str
	end: str
	length: int
	color: TrainColor
	claimedBy: int | None # player number if claimed, None otherwise

	def __init__(self, start: str, end: str, length: int, color: TrainColor):
		self.start = start
		self.end = end
		self.length = length
		self.color = color
		self.claimedBy = None

	def __contains__(self, item: "str") -> bool:
		return self.start == item or self.end == item

	def other(self, start: str) -> str:
		'''Returns the city at the other side of the route from `start`.'''
		if self.start == start:
			return self.end
		elif self.end == start:
			return self.start
		else:
			raise ValueError(f"{start} is not in route from {self.start} to {self.end}.")

	def claim(self, player: int):
		'''Claims the route for `player`.'''
		self.claimedBy = player
	