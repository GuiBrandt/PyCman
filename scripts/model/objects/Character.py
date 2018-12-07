import pygame
import math

from ...controller.InputManager import InputManager
from .GameObject import GameObject

class Character(GameObject):

	def __init__(self):
		super().__init__()
		self._direction = 0
		self._desired_direction = 0

		self._movement_speed = 0.05

		self.real_x = self.real_y = 0.0
		self.x = self.y = 0

	def get_direction(self):
		return self._direction

	def get_sprite_index(self):
		return -1

	def update(self, map):
		super().update(map)

		self.move(
			map,
			self._movement_speed * self._dir_x_component(self._direction),
			self._movement_speed * self._dir_y_component(self._direction)
		)

		if InputManager.key_state(pygame.K_UP):
			self._desired_direction = 4
		elif InputManager.key_state(pygame.K_DOWN):
			self._desired_direction = 6
		elif InputManager.key_state(pygame.K_LEFT):
			self._desired_direction = 2
		elif InputManager.key_state(pygame.K_RIGHT):
			self._desired_direction = 0

		if self.can_turn(map, self._desired_direction):
			self._direction = self._desired_direction

	def can_turn(self, map, d):
		dx = self._dir_x_component(d) * self._movement_speed
		dy = self._dir_y_component(d) * self._movement_speed
		x2, y2 = int(round(self.real_x + dx)), int(round(self.real_y + dy))

		return map.is_passable(x2, y2)

	def _dir_x_component(self, d):
		if d == 0:
			return 1
		elif d == 2:
			return -1
		else:
			return 0

	def _dir_y_component(self, d):
		if d == 4:
			return -1
		elif d == 6:
			return 1
		else:
			return 0

	def move(self, map, x, y):
		dx = self._dir_x_component(self._direction) * self._movement_speed
		dy = self._dir_y_component(self._direction) * self._movement_speed
		x2, y2 = int(round(self.real_x + dx)), int(round(self.real_y + dy))

		if not map.is_passable(x2, y2):
			return

		self.real_x += x

		if self.real_x < -1:
			self.real_x += 28
		elif self.real_x > 28:
			self.real_x -= 28

		self.real_y += y

		if self.real_y < -1:
			self.real_y += 31
		elif self.real_y > 31:
			self.real_y -= 31

		self.x, self.y = int(round(self.real_x)), int(round(self.real_y))