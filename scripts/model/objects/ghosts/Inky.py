import random

from .Ghost import Ghost
from .Pinky import Pinky

class Inky(Ghost):

	def __init__(self):
		super().__init__()
		self._sprite_index = 5
	
	def get_sprite_index(self):
		return self._sprite_index
	
	def set_running_sprite(self):
		if self._sprite_index != 7:
			self._sprite_index = 2

	def set_dead_sprite(self):
		self._sprite_index = 7

	def set_normal_sprite(self):
		self._sprite_index = 5

	def update_movement(self, map, player):
		if random.choice([True, False, False, False]):
			self._desired_direction = random.choice([0, 2, 4, 6])
		else:
			Pinky.update_movement(self, map, player)