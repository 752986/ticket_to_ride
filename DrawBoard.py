import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from Board import Board, USABoard
import random
from copy import deepcopy


# config:
FRAMERATE = 60
SCREEN_SIZE = Vector2(1200, 800)

RELAX_FREQUENCY = 1/60

SCALE = 50
SIZE = 800


# pygame init:
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("")
font = pygame.font.SysFont(pygame.font.get_default_font(), 12)


# definitions:
def smoothMax(x: float) -> float:
	return (1 - 1 / (1 + abs(x))) * (1 if x >= 0 else -1)

def relaxGraph(board: Board, positions: dict[str, Vector2], move_factor: float, length_per_unit: float) -> dict[str, Vector2]:
	'''Iteratively moves vertices closer to their proper position based on edge lengths.'''

	working_copy = deepcopy(positions)

	# max_length = max(map(lambda r: r.length, board.routes))
	
	for c in board.cities:
		overall_distance = 0
		for r in board.connections(c):
			difference = positions[r.other(c)] - positions[c] # vector from `c` to other city on route
			length_difference = difference.length() - r.length * length_per_unit
			overall_distance += length_difference
			working_copy[c] += difference.normalize() * smoothMax(length_difference) * move_factor # move towards the other city based on length
			working_copy[c] += Vector2(random.random() * 2 - 1, random.random() * 2 - 1) * smoothMax(abs(length_difference)) * 1
		if random.random() < (smoothMax(overall_distance) * 0.001) - 0.0001:
			# working_copy[c] = Vector2(random.random(), random.random()) * SIZE
			working_copy[c] = Vector2(0.5, 0.5) * SIZE

	return working_copy


def main():
	# game setup:
	clock = pygame.time.Clock()

	positions: dict[str, Vector2] = {}
	for c in USABoard.cities:
		positions[c] = Vector2(random.random(), random.random()) * SIZE

	timer = 0

	# main loop:
	running = True
	while running:
		delta = clock.tick(FRAMERATE) / 1000
		timer += delta

		# input:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# update:
		if timer >= RELAX_FREQUENCY:
			positions = relaxGraph(USABoard, positions, 1, SCALE)
			timer = 0

		# draw:
		screen.fill("#000000")
		for c, p in positions.items():
			pygame.draw.circle(screen, "#ffffff", p, 2)

			text = font.render(c, True, "#ffffff")

			screen.blit(text, p + Vector2(4, 4))

		for r in USABoard.routes:
			desired_length = SCALE * r.length
			actual_length = positions[r.start].distance_to(positions[r.end])
			error = abs(actual_length - desired_length)
			value = int(smoothMax(error) * 255)

			# pygame.draw.aaline(screen, "#ff8844", positions[r.start], positions[r.end])
			pygame.draw.aaline(screen, (value, value, value), positions[r.start], positions[r.end])

		pygame.display.flip()

if __name__ == "__main__":
	main()
