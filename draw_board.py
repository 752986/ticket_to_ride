# An experiment in graph visualization. It attempts to lay out the cities of the U.S. board
# knowing only their relative distances. The final game will probably just use hardcoded positions.
# 
# The `Board` class implements a graph by storing its edges. `USABoard` is a Board object
# encoding the Ticket to Ride USA map. This file implements "force-directed graph drawing", where
# close nodes are pushed apart and linked nodes are pushed or pulled to a desired distance. 

import pygame
from pygame.math import Vector2
from Board import Board, USABoard
import random
from copy import deepcopy


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)

RELAX_FREQUENCY = 0 # seconds between iterations # set to 0 for 1 iteration per frame

SCALE = 20
KEEP_CENTERED = True


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")
font = pygame.font.SysFont(pygame.font.get_default_font(), 16)


# definitions:
def relaxGraph(board: Board, positions: dict[str, Vector2], pull_factor: float, push_factor: float, scale: float) -> dict[str, Vector2]:
	'''Iteratively moves vertices closer to their proper position based on edge lengths.'''

	working_copy = deepcopy(positions)
	
	for c in board.cities:
		to_move = Vector2(0, 0)

		# pull towards connected cities
		for r in board.connections(c):
			difference = positions[r.other(c)] - positions[c] # vector from `c` to other city on route
			length_difference = difference.length() - r.length * scale
			to_move += difference.normalize() * length_difference * pull_factor # move towards the other city based on length
		
		# push away from nearby cities
		for p in positions.values():
			if p != positions[c]:
				to_move += (positions[c] - p) / positions[c].distance_to(p) * scale * push_factor
		
		working_copy[c] += to_move / len(board.connections(c))

	return working_copy


def main():
	# game setup:
	clock = pygame.time.Clock()

	positions: dict[str, Vector2] = {}
	for c in USABoard.cities:
		positions[c] = Vector2(random.random() * SCREEN_SIZE.x, random.random() * SCREEN_SIZE.y)

	timer = 0

	# currently dragged node
	held = ""

	# shortest path display
	choosing_start = True
	start = ""
	end = ""
	path: list[str] = []
	dists: dict[str, int] = {}

	# main loop:
	running = True
	while running:
		delta = clock.tick(FRAMERATE) / 1000
		timer += delta

		# input:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				closest_city = sorted(USABoard.cities, key=lambda c: Vector2(pygame.mouse.get_pos()).distance_to(positions[c]))[0]
				if pygame.mouse.get_pressed()[0]:
					held = closest_city
				if pygame.mouse.get_pressed()[2]:
					if end == "":
						if choosing_start:
							start = closest_city
						else:
							end = closest_city
						choosing_start = not choosing_start
					else:
						start = end
						end = closest_city

					if start != "":
						dists = USABoard.distances(start)
						if end != "":
							result = USABoard.path(start, end)
							path = result if result != None else []
			elif event.type == pygame.MOUSEBUTTONUP:
				if not pygame.mouse.get_pressed()[0]:
					held = ""
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					# reset distance elements
					choosing_start = True
					start = ""
					end = ""
					path = []
					dists = {}

		# update:
		if held != "":
			positions[held] = Vector2(pygame.mouse.get_pos())

		if timer >= RELAX_FREQUENCY:
			timer = 0
			positions = relaxGraph(USABoard, positions, 1, 0.1, SCALE)

			if KEEP_CENTERED:
				avg_position = Vector2(0, 0)
				for p in positions.values():
					avg_position += p
				avg_position /= len(positions)
				avg_position -= SCREEN_SIZE / 2
				for p in positions.values():
					p -= avg_position

		# draw:
		screen.fill("#111111")

		for r in USABoard.routes:
			color = "#ff8535"
			pygame.draw.aaline(screen, color, positions[r.start], positions[r.end])

			text = font.render(str(r.length), True, color)

			screen.blit(text, (positions[r.start] + positions[r.end]) / 2 + Vector2(0, -16))

		for child, p in positions.items():
			if child == start:
				pygame.draw.circle(screen, "#008d5c", p, 4)
			elif child == end:
				pygame.draw.circle(screen, "#dd1100", p, 4)
			pygame.draw.circle(screen, "#ffffff", p, 2)

			text = font.render(child, True, "#ffffff")

			screen.blit(text, p + Vector2(4, 4))

			if child in dists:
				dist_text = font.render(str(dists[child]), True, "#87ffc3")

				screen.blit(dist_text, p + Vector2(4, -8))

		if len(path) > 1:
			for i in range(len(path) - 1):
				pygame.draw.aaline(screen, "#00ac71", positions[path[i]], positions[path[i + 1]])

		pygame.display.flip()

if __name__ == "__main__":
	main()
