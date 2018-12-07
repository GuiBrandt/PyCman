from heapq import heappush, heappop

import random
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
		self._direction = 6
	
	def make_path(self, came_from, cx, cy):
		path = [(cx, cy)]

		while (cx, cy) in came_from:
			cx, cy = came_from[(cx, cy)]
			path.insert(0, (cx, cy))

		return path

	def neighbors(self, map, player, x, y):
		result = set()
	
		for ix in range(-1, 2):
			for iy in range(-1, 2):
				if ix == 0 and iy == 0:
					continue

				if not (ix == 0 or iy == 0):
					continue

				if not map.is_passable(x + ix, y + iy):
					continue

				if player.x == x and player.y == y:
					continue
				
				result.add((x + ix, y + iy))
		
		return result

	def a_star(self, map, player, x, y):
		if not map.is_passable(x, y):
			return False

		q = []
		came_from = {}

		closed = set()

		sx, sy = self.adjust_xy(self.real_x, self.real_y)

		scores = {}
		scores[(sx, sy)] = 0

		heappush(q, (-1, sx, sy))

		it = 0

		while len(q) > 0:
			it += 1

			if it >= 300:
				break

			_, cx, cy = heappop(q)

			if (cx, cy) in closed:
				  continue

			if cx == x and cy == y:
				return self.make_path(came_from, cx, cy)

			closed.add((cx, cy))

			for nx, ny in self.neighbors(map, player, cx, cy):
				if (nx, ny) in closed:
					continue

				score = scores[(cx, cy)] + 1

				if score >= (scores[(nx, ny)] if (nx, ny) in scores else 0x7FFFFFFF):
					continue

				came_from[(nx, ny)] = (cx, cy)
				scores[(nx, ny)] = score
				
				heappush(q, (score + math.hypot(x - nx, y - ny), nx, ny))

		return None

	def set_running_sprite(self):
		self._sprite_index = 2

	def set_normal_sprite(self):
		self._sprite_index = 3

	def run_away(self, map, player):
		if self.x == Ghost.SPAWN_X and self.y == Ghost.SPAWN_Y:
			self.set_normal_sprite()
			return

		self._movement_speed = 0.075
		path = self.a_star(map, player, Ghost.SPAWN_X, Ghost.SPAWN_Y)

		x2, y2 = self.adjust_xy(self.real_x, self.real_y)
		if not map.is_passable(x2, y2) and not self._direction != self._desired_direction:
			self._desired_direction = random.choice([0, 2, 4, 6])
			return

		if not path or len(path) <= 1:
			return
			
		dx, dy = path[1]

		if dx < self.x:
			self._desired_direction = 2
		elif dx > self.x:
			self._desired_direction = 0

		if dy < self.y:
			self._desired_direction = 4
		elif dy > self.y:
			self._desired_direction = 6

		pass

	def update_movement(self, map, player):
		pass

	def update(self, map, player):
		super().update(map)

		if self._sprite_index == 2:
			self.run_away(map, player)

		else:
			self._movement_speed = 0.1
			self.update_movement(map, player)