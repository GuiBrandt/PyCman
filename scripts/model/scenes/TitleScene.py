import pygame

from .SceneBase import SceneBase
from ...view.Spriteset_title import Spriteset_title

class TitleScene(SceneBase):

	def __init__(self):
		self._spriteset = Spriteset_title()
		self.play = False
 
	def update(self):
		super().update()
		mousepos = pygame.mouse.get_pos()
		if 200 < mousepos[0] < 280 and 304 < mousepos[1] < 324:
			self.play = True
		else:
			self.play = False

	def render(self, screen):
		self._spriteset.render(self.play, screen)