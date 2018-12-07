from .Ghost import Ghost
import random

class Pinky(Ghost):
	
	def __init__(self):
		super().__init__()
		self._sprite_index = 4
	
	def get_sprite_index(self):
		return self._sprite_index
	
	def set_running_sprite(self):
		if self._sprite_index != 7:
			self._sprite_index = 2

	def set_dead_sprite(self):
		self._sprite_index = 7

	def set_normal_sprite(self):
		self._sprite_index = 4
	
	def update_movement(self, map, player):
		dx = self._dir_x_component(player._direction)
		dy = self._dir_y_component(player._direction)

		px, py = player.x, player.y
		px += dx
		py += dy
		
		path = self.a_star(map, player, px, py)

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