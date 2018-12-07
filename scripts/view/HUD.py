from pygame import font, image

class HUD:
	"""docstring for HUD"""
	def __init__(self, p):
		self._player = p

	def render(self, screen):
		font.init()
		myfont = font.SysFont('consolas', 16)
		textsurface = myfont.render('Pontuação: %d' % self._player.points, True, (255, 255, 255))
		screen.blit(textsurface,(5, 5))