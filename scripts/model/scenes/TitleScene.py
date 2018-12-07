import pygame

from .SceneBase import SceneBase
from .AboutScene import AboutScene
from . import GameScene
from ...view.Spriteset_title import Spriteset_title
from ...controller import SceneManager

class TitleScene(SceneBase):

	def __init__(self):
		self._spriteset = Spriteset_title()
		self.play = False
		self.about = False
 
	def update(self):
		super().update()
		mousepos = pygame.mouse.get_pos()
		if 200 < mousepos[0] < 280 and 304 < mousepos[1] < 324:
			self.play = True
			if pygame.mouse.get_pressed()[0]:
				SceneManager.SceneManager.call(GameScene.GameScene)			
		else:
			self.play = False


		mousepos = pygame.mouse.get_pos()
		if 200 < mousepos[0] < 280 and 404 < mousepos[1] < 424:
			self.about = True
			if pygame.mouse.get_pressed()[0]:
				SceneManager.SceneManager.call(AboutScene)			
		else:
			self.about = False

	def render(self, screen):
		self._spriteset.render(self.play, self.about, screen)