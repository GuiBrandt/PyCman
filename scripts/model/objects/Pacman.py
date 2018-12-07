from .Character import Character
from ..Map import Map

import pygame
from ...controller.InputManager import InputManager

from ...controller.AudioManager import AudioManager
from ...controller.AudioManager import Sound

class Pacman(Character):

	def __init__(self):
		super().__init__()
		self.real_x = 13
		self.real_y = 17
		self.x = 13
		self.y = 17
		self.points = 0
		self.power = False
		self._power_countdown = 0
		self._sprite_index = 0
		AudioManager.play_sound(Sound.WAKA_SOUND)

	def kill(self):
		self._sprite_index = 1
		self._trigger('death')

	def update(self, map):
		super().update(map)

		if InputManager.key_state(pygame.K_UP):
			self._desired_direction = 4
		elif InputManager.key_state(pygame.K_DOWN):
			self._desired_direction = 6
		elif InputManager.key_state(pygame.K_LEFT):
			self._desired_direction = 2
		elif InputManager.key_state(pygame.K_RIGHT):
			self._desired_direction = 0

		if self._power_countdown >= 0:
			self._power_countdown -= 1
		elif self.power == True:
			AudioManager.play_sound(Sound.WAKA_SOUND)
			self.power = False

		cell_at = map.get_tile(self.x, self.y)

		if cell_at == Map.Tile.POINT:
			map.set_tile_at(self.x, self.y, Map.Tile.EMPTY)
			self.points += 10
		elif cell_at == Map.Tile.BONUS:
			map.set_tile_at(self.x, self.y, Map.Tile.EMPTY)
			self.power = True
			AudioManager.play_sound(Sound.POWER_SOUND)
			self._power_countdown = 300
		

	def get_sprite_index(self):
		return self._sprite_index