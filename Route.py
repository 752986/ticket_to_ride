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
	
	def value(self) -> int:
		'''Returns the point value of the route, based on its length.
		
		This is implemented as an algorithm rather than a lookup table, so it can handle lengths above 6.
		'''
		result = 1
		for i in range(self.length):
			result += i
		return result

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
	