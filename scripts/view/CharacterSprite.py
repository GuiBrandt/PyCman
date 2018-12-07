import io, os
import pygame
from pygame import image
from ..model.objects.Pacman import Pacman
from .Tilemap import Tilemap

class CharacterSprite:

	CHARACTER_SPRITE = 'sprites.png'
	SPRITE_SIZE = 16
	ANIM_RATE = 16

	def __init__(self, character):
		self._character = character
		self.frame_number = 0
		self.__char_sprite = pygame.image.load(os.path.join('assets/', CharacterSprite.CHARACTER_SPRITE))

	def render(self, screen, offset):
		self.frame_number += 1
		self.frame_number %= CharacterSprite.ANIM_RATE

		y_pos = self._character.get_sprite_index() * CharacterSprite.SPRITE_SIZE
		x_pos = (self._character.get_direction() + (self.frame_number > CharacterSprite.ANIM_RATE / 2 - 1)) * CharacterSprite.SPRITE_SIZE

		tile = pygame.Surface((CharacterSprite.SPRITE_SIZE, CharacterSprite.SPRITE_SIZE))
		tile.blit(self.__char_sprite, (0, 0), (x_pos, y_pos, CharacterSprite.SPRITE_SIZE, CharacterSprite.SPRITE_SIZE))
		tile = pygame.transform.scale2x(tile)
		tile.set_colorkey(self.__char_sprite.get_at((0, 0)))

		offset = (offset[0] - Tilemap.TILE_SIZE, offset[1] - Tilemap.TILE_SIZE)
		
		screen.blit(tile, (offset[0] + self._character.real_x * 2 * Tilemap.TILE_SIZE, offset[1] + self._character.real_y * 2 * Tilemap.TILE_SIZE))