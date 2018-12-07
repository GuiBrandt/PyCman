from heapq import heappush, heappop

import math

from ..Character import Character

class Ghost(Character):

	SPAWN_X = 15 
	SPAWN_Y = 15 

	def __init__(self):
		super().__init__()
		self.real_x = Ghost.SPAWN_X
		self.real_y = Ghost.SPAWN_Y
		self.x = Ghost.SPAWN_X
		self.y = Ghost.SPAWN_Y
	
	def make_path(self, came_from, cx, cy):
		path = [(cx, cy)]

		while (cx, cy) in came_from:
			cx, cy = came_from[(cx, cy)]
			path.insert(0, (cx, cy))

		return path

	def neighbors(self, map, x, y):
		result = set()
	
		for ix in range(-1, 2):
			for iy in range(-1, 2):
				if ix == 0 and iy == 0:
					continue

				if not (ix == 0 or iy == 0):
					continue

				if not map.is_passable(x + ix, y + iy):
					continue
				
				result.add((x + ix, y + iy))
		
		return result

	def a_star(self, map, x, y):
		q = []
		came_from = {}
		closed = set()

		scores = {}
		scores[(self.x, self.y)] = 0

		heappush(q, (math.hypot(x - self.x, y - self.y), self.x, self.y))

		while len(q) > 0:
			_, cx, cy = heappop(q)

			if cx == x and cy == y:
				return self.make_path(came_from, cx, cy)

			closed.add((cx, cy))

			for nx, ny in self.neighbors(map, cx, cy):
				if (nx, ny) in closed:
					continue

				score = scores[(cx, cy)] + 1

				if (nx, ny) not in q:
					heappush(q, (score + math.hypot(x - nx, y - ny), nx, ny))
				elif (nx, ny) in scores and score >= scores[(nx, ny)]:
					continue

				came_from[(nx, ny)] = (cx, cy)
				scores[(nx, ny)] = score

		return None

	def update(self, map, player):
		super().update(map)