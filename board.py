from Connection import Connection
from TrainColor import TrainColor

class Board:
	cities: list[str]
	connections: list[Connection]
	
	def __init__(self, connections: list[Connection]):
		self.connections = connections
		cities: set[str] = set()
		for c in connections:
			cities.add(c.start)
			cities.add(c.end)
		self.cities = list(cities)

	def neighbors(self, city: str) -> list[Connection]:
		'''Returns all connections to/from `city`.'''

		return list(filter(lambda c: c.start == city or c.end == city, self.connections))
		
	def distance(self, start: str, end: str) -> int:
		'''Returns the minimum distance between `start` and `end`, measured in train lengths.'''

	def connected(self, start: str, end: str, player: int) -> bool:
		'''Determines whether a route exists between `start` and `end` through connections claimed by `player`.'''

USABoard = Board(
	connections = [
		Connection("Atlanta", "Charleston", 2, TrainColor.Wild),
		Connection("Atlanta", "Miami", 5, TrainColor.Blue),
		Connection("Atlanta", "Nashville", 1, TrainColor.Wild),
		Connection("Atlanta", "New Orleans", 4, TrainColor.Orange),
		Connection("Atlanta", "New Orleans", 4, TrainColor.Yellow),
		Connection("Atlanta", "Raleigh", 2, TrainColor.Wild),
		Connection("Atlanta", "Raleigh", 2, TrainColor.Wild),
		Connection("Boston", "Montreal", 2, TrainColor.Wild),
		Connection("Boston", "Montreal", 2, TrainColor.Wild),
		Connection("Boston", "New York", 2, TrainColor.Red),
		Connection("Boston", "New York", 2, TrainColor.Yellow),
		Connection("Calgary", "Helena", 4, TrainColor.Wild),
		Connection("Calgary", "Seattle", 4, TrainColor.Wild),
		Connection("Calgary", "Vancouver", 3, TrainColor.Wild),
		Connection("Calgary", "Winnipeg", 6, TrainColor.White),
		Connection("Charleston", "Miami", 4, TrainColor.Pink),
		Connection("Charleston", "Raleigh", 2, TrainColor.Wild),
		Connection("Chicago", "Duluth", 3, TrainColor.Red),
		Connection("Chicago", "Omaha", 4, TrainColor.Blue),
		Connection("Chicago", "Pittsburg", 3, TrainColor.Orange),
		Connection("Chicago", "Pittsburg", 3, TrainColor.Black),
		Connection("Chicago", "Saint Louis", 2, TrainColor.Green),
		Connection("Chicago", "Saint Louis", 2, TrainColor.White),
		Connection("Chicago", "Toronto", 4, TrainColor.White),
		Connection("Dallas", "El Paso", 4, TrainColor.Red),
		Connection("Dallas", "Houston", 1, TrainColor.Wild),
		Connection("Dallas", "Houston", 1, TrainColor.Wild),
		Connection("Dallas", "Little Rock", 2, TrainColor.Wild),
		Connection("Dallas", "Oklahoma City", 2, TrainColor.Wild),
		Connection("Dallas", "Oklahoma City", 2, TrainColor.Wild),
		Connection("Denver", "Helena", 4, TrainColor.Green),
		Connection("Denver", "Kansas City", 4, TrainColor.Orange),
		Connection("Denver", "Kansas City", 4, TrainColor.Black),
		Connection("Denver", "Oklahoma City", 4, TrainColor.Red),
		Connection("Denver", "Omaha", 4, TrainColor.Pink),
		Connection("Denver", "Phoenix", 5, TrainColor.White),
		Connection("Denver", "Salt Lake City", 3, TrainColor.Red),
		Connection("Denver", "Salt Lake City", 3, TrainColor.Yellow),
		Connection("Denver", "Santa Fe", 2, TrainColor.Wild),
		Connection("Duluth", "Helena", 6, TrainColor.Orange),
		Connection("Duluth", "Omaha", 2, TrainColor.Wild),
		Connection("Duluth", "Omaha", 2, TrainColor.Wild),
		Connection("Duluth", "Sault St. Marie", 3, TrainColor.Wild),
		Connection("Duluth", "Toronto", 6, TrainColor.Pink),
		Connection("Duluth", "Winnipeg", 4, TrainColor.Black),
		Connection("El Paso", "Houston", 6, TrainColor.Green),
		Connection("El Paso", "Los Angeles", 6, TrainColor.Black),
		Connection("El Paso", "Oklahoma City", 5, TrainColor.Yellow),
		Connection("El Paso", "Phoenix", 3, TrainColor.Wild),
		Connection("El Paso", "Santa Fe", 2, TrainColor.Wild),
		Connection("Helena", "Omaha", 5, TrainColor.Red),
		Connection("Helena", "Salt Lake City", 3, TrainColor.Pink),
		Connection("Helena", "Seattle", 6, TrainColor.Yellow),
		Connection("Helena", "Winnipeg", 4, TrainColor.Blue),
		Connection("Houston", "New Orleans", 2, TrainColor.Wild),
		Connection("Kansas City", "Oklahoma City", 2, TrainColor.Wild),
		Connection("Kansas City", "Oklahoma City", 2, TrainColor.Wild),
		Connection("Kansas City", "Omaha", 1, TrainColor.Wild),
		Connection("Kansas City", "Omaha", 1, TrainColor.Wild),
		Connection("Kansas City", "Saint Louis", 2, TrainColor.Blue),
		Connection("Kansas City", "Saint Louis", 2, TrainColor.Pink),
		Connection("Las Vegas", "Los Angeles", 2, TrainColor.Wild),
		Connection("Las Vegas", "Salt Lake City", 3, TrainColor.Orange),
		Connection("Little Rock", "Nashville", 3, TrainColor.White),
		Connection("Little Rock", "New Orleans", 3, TrainColor.Green),
		Connection("Little Rock", "Oklahoma City", 2, TrainColor.Wild),
		Connection("Little Rock", "Saint Louis", 2, TrainColor.Wild),
		Connection("Los Angeles", "Phoenix", 3, TrainColor.Wild),
		Connection("Los Angeles", "San Francisco", 3, TrainColor.Yellow),
		Connection("Los Angeles", "San Francisco", 3, TrainColor.Pink),
		Connection("Miami", "New Orleans", 6, TrainColor.Red),
		Connection("Montreal", "New York", 3, TrainColor.Blue),
		Connection("Montreal", "Sault St. Marie", 5, TrainColor.Black),
		Connection("Montreal", "Toronto", 3, TrainColor.Wild),
		Connection("Nashville", "Pittsburg", 4, TrainColor.Yellow),
		Connection("Nashville", "Raleigh", 3, TrainColor.Black),
		Connection("Nashville", "Saint Louis", 2, TrainColor.Wild),
		Connection("New York", "Pittsburg", 2, TrainColor.Green),
		Connection("New York", "Pittsburg", 2, TrainColor.White),
		Connection("New York", "Washington", 2, TrainColor.Orange),
		Connection("New York", "Washington", 2, TrainColor.Black),
		Connection("Oklahoma City", "Santa Fe", 3, TrainColor.Blue),
		Connection("Phoenix", "Santa Fe", 3, TrainColor.Wild),
		Connection("Pittsburg", "Raleigh", 2, TrainColor.Wild),
		Connection("Pittsburg", "Saint Louis", 5, TrainColor.Green),
		Connection("Pittsburg", "Toronto", 2, TrainColor.Wild),
		Connection("Pittsburg", "Washington", 2, TrainColor.Wild),
		Connection("Portland", "Salt Lake City", 6, TrainColor.Blue),
		Connection("Portland", "San Francisco", 5, TrainColor.Green),
		Connection("Portland", "San Francisco", 5, TrainColor.Pink),
		Connection("Portland", "Seattle", 1, TrainColor.Wild),
		Connection("Portland", "Seattle", 1, TrainColor.Wild),
		Connection("Raleigh", "Washington", 2, TrainColor.Wild),
		Connection("Raleigh", "Washington", 2, TrainColor.Wild),
		Connection("Salt Lake City", "San Francisco", 5, TrainColor.Orange),
		Connection("Salt Lake City", "San Francisco", 5, TrainColor.White),
		Connection("Sault St. Marie", "Toronto", 2, TrainColor.Wild),
		Connection("Sault St. Marie", "Winnipeg", 5, TrainColor.Wild),
		Connection("Seattle", "Vancouver", 1, TrainColor.Wild),
		Connection("Seattle", "Vancouver", 1, TrainColor.Wild),
	]
)
