class Route:
	start: str
	end: str
	value: int

	def __init__(self, start: str, end: str, value: int):
		self.start = start
		self.end = end
		self.value = value
