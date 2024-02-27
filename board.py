from Route import Route
from TrainColor import TrainColor
from queue import Queue

class Board:
	cities: list[str]
	routes: list[Route]
	
	def __init__(self, routes: list[Route]):
		self.routes = routes
		cities: set[str] = set()
		for r in routes:
			cities.add(r.start)
			cities.add(r.end)
		self.cities = list(cities)

	def connections(self, city: str) -> list[Route]:
		'''Returns all routes to/from `city`.'''

		return list(filter(lambda r: r.start == city or r.end == city, self.routes))
	
	def neighbors(self, city: str) -> list[str]:
		'''Returns all cities with a direct route to `city`.'''

		return list(map(lambda r: r.other(city), self.connections(city)))
		
	def distance(self, start: str, end: str) -> int:
		'''Returns the minimum distance between `start` and `end`, measured in train lengths.'''

		dists: dict[str, int] = {start: 0}
		unvisited: Queue[str] = Queue()
		visited: set[str] = set()
		for n in self.neighbors(start):
			unvisited.put(n)

		while not unvisited.empty():
			city = unvisited.get()
			# find the connections from the current city to already-checked cities
			toCheck = filter(lambda c: c.other(city) in dists, self.connections(city))
			# find the shortest total distance to the current city
			dists[city] = min(map(lambda c: dists[c.other(city)] + c.length, toCheck))

			if city == end: # early out
				break

			visited.add(city)
			for n in self.neighbors(city):
				if n not in visited:
					unvisited.put(n)

		return dists[end]
			

	def connected(self, start: str, end: str, player: int) -> bool:
		'''Determines whether a path exists between `start` and `end` through routes claimed by `player`.'''

USABoard = Board(
	[
		Route("Atlanta", "Charleston", 2, TrainColor.Wild),
		Route("Atlanta", "Miami", 5, TrainColor.Blue),
		Route("Atlanta", "Nashville", 1, TrainColor.Wild),
		Route("Atlanta", "New Orleans", 4, TrainColor.Orange),
		Route("Atlanta", "New Orleans", 4, TrainColor.Yellow),
		Route("Atlanta", "Raleigh", 2, TrainColor.Wild),
		Route("Atlanta", "Raleigh", 2, TrainColor.Wild),
		Route("Boston", "Montreal", 2, TrainColor.Wild),
		Route("Boston", "Montreal", 2, TrainColor.Wild),
		Route("Boston", "New York", 2, TrainColor.Red),
		Route("Boston", "New York", 2, TrainColor.Yellow),
		Route("Calgary", "Helena", 4, TrainColor.Wild),
		Route("Calgary", "Seattle", 4, TrainColor.Wild),
		Route("Calgary", "Vancouver", 3, TrainColor.Wild),
		Route("Calgary", "Winnipeg", 6, TrainColor.White),
		Route("Charleston", "Miami", 4, TrainColor.Pink),
		Route("Charleston", "Raleigh", 2, TrainColor.Wild),
		Route("Chicago", "Duluth", 3, TrainColor.Red),
		Route("Chicago", "Omaha", 4, TrainColor.Blue),
		Route("Chicago", "Pittsburg", 3, TrainColor.Orange),
		Route("Chicago", "Pittsburg", 3, TrainColor.Black),
		Route("Chicago", "Saint Louis", 2, TrainColor.Green),
		Route("Chicago", "Saint Louis", 2, TrainColor.White),
		Route("Chicago", "Toronto", 4, TrainColor.White),
		Route("Dallas", "El Paso", 4, TrainColor.Red),
		Route("Dallas", "Houston", 1, TrainColor.Wild),
		Route("Dallas", "Houston", 1, TrainColor.Wild),
		Route("Dallas", "Little Rock", 2, TrainColor.Wild),
		Route("Dallas", "Oklahoma City", 2, TrainColor.Wild),
		Route("Dallas", "Oklahoma City", 2, TrainColor.Wild),
		Route("Denver", "Helena", 4, TrainColor.Green),
		Route("Denver", "Kansas City", 4, TrainColor.Orange),
		Route("Denver", "Kansas City", 4, TrainColor.Black),
		Route("Denver", "Oklahoma City", 4, TrainColor.Red),
		Route("Denver", "Omaha", 4, TrainColor.Pink),
		Route("Denver", "Phoenix", 5, TrainColor.White),
		Route("Denver", "Salt Lake City", 3, TrainColor.Red),
		Route("Denver", "Salt Lake City", 3, TrainColor.Yellow),
		Route("Denver", "Santa Fe", 2, TrainColor.Wild),
		Route("Duluth", "Helena", 6, TrainColor.Orange),
		Route("Duluth", "Omaha", 2, TrainColor.Wild),
		Route("Duluth", "Omaha", 2, TrainColor.Wild),
		Route("Duluth", "Sault St. Marie", 3, TrainColor.Wild),
		Route("Duluth", "Toronto", 6, TrainColor.Pink),
		Route("Duluth", "Winnipeg", 4, TrainColor.Black),
		Route("El Paso", "Houston", 6, TrainColor.Green),
		Route("El Paso", "Los Angeles", 6, TrainColor.Black),
		Route("El Paso", "Oklahoma City", 5, TrainColor.Yellow),
		Route("El Paso", "Phoenix", 3, TrainColor.Wild),
		Route("El Paso", "Santa Fe", 2, TrainColor.Wild),
		Route("Helena", "Omaha", 5, TrainColor.Red),
		Route("Helena", "Salt Lake City", 3, TrainColor.Pink),
		Route("Helena", "Seattle", 6, TrainColor.Yellow),
		Route("Helena", "Winnipeg", 4, TrainColor.Blue),
		Route("Houston", "New Orleans", 2, TrainColor.Wild),
		Route("Kansas City", "Oklahoma City", 2, TrainColor.Wild),
		Route("Kansas City", "Oklahoma City", 2, TrainColor.Wild),
		Route("Kansas City", "Omaha", 1, TrainColor.Wild),
		Route("Kansas City", "Omaha", 1, TrainColor.Wild),
		Route("Kansas City", "Saint Louis", 2, TrainColor.Blue),
		Route("Kansas City", "Saint Louis", 2, TrainColor.Pink),
		Route("Las Vegas", "Los Angeles", 2, TrainColor.Wild),
		Route("Las Vegas", "Salt Lake City", 3, TrainColor.Orange),
		Route("Little Rock", "Nashville", 3, TrainColor.White),
		Route("Little Rock", "New Orleans", 3, TrainColor.Green),
		Route("Little Rock", "Oklahoma City", 2, TrainColor.Wild),
		Route("Little Rock", "Saint Louis", 2, TrainColor.Wild),
		Route("Los Angeles", "Phoenix", 3, TrainColor.Wild),
		Route("Los Angeles", "San Francisco", 3, TrainColor.Yellow),
		Route("Los Angeles", "San Francisco", 3, TrainColor.Pink),
		Route("Miami", "New Orleans", 6, TrainColor.Red),
		Route("Montreal", "New York", 3, TrainColor.Blue),
		Route("Montreal", "Sault St. Marie", 5, TrainColor.Black),
		Route("Montreal", "Toronto", 3, TrainColor.Wild),
		Route("Nashville", "Pittsburg", 4, TrainColor.Yellow),
		Route("Nashville", "Raleigh", 3, TrainColor.Black),
		Route("Nashville", "Saint Louis", 2, TrainColor.Wild),
		Route("New York", "Pittsburg", 2, TrainColor.Green),
		Route("New York", "Pittsburg", 2, TrainColor.White),
		Route("New York", "Washington", 2, TrainColor.Orange),
		Route("New York", "Washington", 2, TrainColor.Black),
		Route("Oklahoma City", "Santa Fe", 3, TrainColor.Blue),
		Route("Phoenix", "Santa Fe", 3, TrainColor.Wild),
		Route("Pittsburg", "Raleigh", 2, TrainColor.Wild),
		Route("Pittsburg", "Saint Louis", 5, TrainColor.Green),
		Route("Pittsburg", "Toronto", 2, TrainColor.Wild),
		Route("Pittsburg", "Washington", 2, TrainColor.Wild),
		Route("Portland", "Salt Lake City", 6, TrainColor.Blue),
		Route("Portland", "San Francisco", 5, TrainColor.Green),
		Route("Portland", "San Francisco", 5, TrainColor.Pink),
		Route("Portland", "Seattle", 1, TrainColor.Wild),
		Route("Portland", "Seattle", 1, TrainColor.Wild),
		Route("Raleigh", "Washington", 2, TrainColor.Wild),
		Route("Raleigh", "Washington", 2, TrainColor.Wild),
		Route("Salt Lake City", "San Francisco", 5, TrainColor.Orange),
		Route("Salt Lake City", "San Francisco", 5, TrainColor.White),
		Route("Sault St. Marie", "Toronto", 2, TrainColor.Wild),
		Route("Sault St. Marie", "Winnipeg", 5, TrainColor.Wild),
		Route("Seattle", "Vancouver", 1, TrainColor.Wild),
		Route("Seattle", "Vancouver", 1, TrainColor.Wild),
	]
)
