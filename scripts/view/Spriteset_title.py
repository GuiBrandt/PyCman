from pygame import font, image

class Spriteset_title:
	def __init__(self):
		pass

	def render(self, play, about,  screen):
		font.init()
		myfont = font.SysFont('consolas', 30)
		textsurface = myfont.render('Bem-vindo ao PyCman', True, (255, 255, 255))
		screen.blit(textsurface,(50, 100))

		myfont = font.SysFont('consolas', 20)

		if play:
			textsurface = myfont.render('Play', True, (200, 200, 200))
		else:
			textsurface = myfont.render('Play', True, (255, 255, 255))

		screen.blit(textsurface,(200, 304))

		if about:
			textsurface = myfont.render('About', True, (200, 200, 200))
		else:
			textsurface = myfont.render('About', True, (255, 255, 255))

		screen.blit(textsurface,(200, 404))
