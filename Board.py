from Route import Route
from TrainColor import TrainColor

class Board:
	cities: set[str]
	routes: list[Route]
	
	def __init__(self, routes: list[Route]):
		self.routes = routes
		self.cities = set()
		for r in routes:
			self.cities.add(r.start)
			self.cities.add(r.end)

	def connections(self, city: str) -> list[Route]:
		'''Returns all routes to/from `city`.'''

		return list(filter(lambda r: city in r, self.routes))
	
	def neighbors(self, city: str) -> list[str]:
		'''Returns all cities with a direct route to `city`.'''

		return list(map(lambda r: r.other(city), self.connections(city)))
	
	def find(
		self, 
		start: str, 
		end: str, 
		*, 
		color: TrainColor | None = None, 
		claimed: bool | None = None
	) -> list[Route]:
		'''Finds all routes between `start` and `end`, optionally limited by `color` and `claimed`.
		The specified cities must be neighbors.
		'''

		if end not in self.neighbors(start):
			raise ValueError(f"`start` and `end` must be neighbors. (\"{start}\" and \"{end}\" given)")
		
		result = filter(lambda r: start in r and end in r, self.routes)

		if color != None:
			result = filter(lambda r: r.color == color, result)

		if claimed == True:
			result = filter(lambda r: r.claimedBy != None, result)
		elif claimed == False:
			result = filter(lambda r: r.claimedBy == None, result)

		return list(result)
	
	def distance(self, start: str, end: str, *, player: int | None = None) -> int | None:
		'''Returns the minimum distance between `start` and `end`, measured in train lengths.
		If `player` is specified, only considers routes claimed by that player.
		If no path exists, returns `None`.

		This functions serves a dual role, both for finding distances,
		and for checking player-specific connectedness.
		'''

		# algorithm:
		# 1. set the distance of the starting city to 0
		# 2. for each city, set its distance to its neighbor's plus the connection length
		# 3. the algorithm is finished once the distances stop changing

		# this is definitely not elegant code, but it gives the right answer (I hope)

		dists: dict[str, int] = {start: 0}
		prev_dists: dict[str, int] = {}
		while dists != prev_dists: # repeat until no changes occur
			prev_dists = dists.copy()
			for city in self.cities:
				# find routes connecting `city` to already-computed cities
				toCheck = filter(lambda r: r.other(city) in dists, self.connections(city))
				if player != None:
					toCheck = filter(lambda r: r.claimedBy == player, toCheck)
				toCheck = list(toCheck)

				if len(toCheck) != 0:
					# find the shortest total distance to the current city
					smallest = min(map(lambda r: dists[r.other(city)] + r.length, toCheck))
					# keep current distance if it's already the smallest
					if not (city in dists and dists[city] <= smallest):
						dists[city] = smallest

		if end in dists:
			return dists[end]
		else:
			return None
			

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
		Route("Chicago", "Pittsburgh", 3, TrainColor.Orange),
		Route("Chicago", "Pittsburgh", 3, TrainColor.Black),
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
		Route("Nashville", "Pittsburgh", 4, TrainColor.Yellow),
		Route("Nashville", "Raleigh", 3, TrainColor.Black),
		Route("Nashville", "Saint Louis", 2, TrainColor.Wild),
		Route("New York", "Pittsburgh", 2, TrainColor.Green),
		Route("New York", "Pittsburgh", 2, TrainColor.White),
		Route("New York", "Washington", 2, TrainColor.Orange),
		Route("New York", "Washington", 2, TrainColor.Black),
		Route("Oklahoma City", "Santa Fe", 3, TrainColor.Blue),
		Route("Phoenix", "Santa Fe", 3, TrainColor.Wild),
		Route("Pittsburgh", "Raleigh", 2, TrainColor.Wild),
		Route("Pittsburgh", "Saint Louis", 5, TrainColor.Green),
		Route("Pittsburgh", "Toronto", 2, TrainColor.Wild),
		Route("Pittsburgh", "Washington", 2, TrainColor.Wild),
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
