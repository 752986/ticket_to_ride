class Ticket:
	start: str
	end: str
	value: int

	def __init__(self, start: str, end: str, value: int):
		self.start = start
		self.end = end
		self.value = value

USATickets = [
	Ticket("Boston", "Miami", 12),
	Ticket("Calgary", "Phoenix", 13),
	Ticket("Calgary", "Salt Lake City", 7),
	Ticket("Chicago", "New Orleans", 7),
	Ticket("Chicago", "Santa Fe", 9),
	Ticket("Dallas", "New York", 11),
	Ticket("Denver", "El Paso", 4),
	Ticket("Denver", "Pittsburgh", 11),
	Ticket("Duluth", "El Paso", 10),
	Ticket("Duluth", "Houston", 8),
	Ticket("Helena", "Los Angeles", 8),
	Ticket("Kansas City", "Houston", 5),
	Ticket("Los Angeles", "Chicago", 16),
	Ticket("Los Angeles", "Miami", 20),
	Ticket("Los Angeles", "New York", 21),
	Ticket("Montreal", "Atlanta", 9),
	Ticket("Montreal", "New Orleans", 13),
	Ticket("New York", "Atlanta", 6),
	Ticket("Portland", "Nashville", 17),
	Ticket("Portland", "Phoenix", 11),
	Ticket("San Francisco", "Atlanta", 17),
	Ticket("Sault St. Marie", "Nashville", 8),
	Ticket("Sault St. Marie", "Oklahoma City", 9),
	Ticket("Seattle", "Los Angeles", 9),
	Ticket("Seattle", "New York", 22),
	Ticket("Toronto", "Miami", 10),
	Ticket("Vancouver", "Montreal", 20),
	Ticket("Vancouver", "Santa Fe", 13),
	Ticket("Winnipeg", "Houston", 12),
	Ticket("Winnipeg", "Little Rock", 11),
]
