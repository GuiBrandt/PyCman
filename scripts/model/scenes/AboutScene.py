import pygame

from .SceneBase import SceneBase
from . import TitleScene
from ...view.Spriteset_About import Spriteset_About
from ...controller import SceneManager

class AboutScene(SceneBase):

	def __init__(self):
		self._spriteset = Spriteset_About()
		self.back = False
 
	def update(self):
		super().update()
		mousepos = pygame.mouse.get_pos()
		if 200 < mousepos[0] < 340 and 424 < mousepos[1] < 444:
			self.back = True
			if pygame.mouse.get_pressed()[0]:
				SceneManager.SceneManager.call(TitleScene.TitleScene)			
		else:
			self.back = False


	def render(self, screen):
		self._spriteset.render(self.back, screen)