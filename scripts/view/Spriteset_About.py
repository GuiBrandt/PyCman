from pygame import font, image

class Spriteset_About:
	def __init__(self):
		pass

	def render(self, back, screen):
		font.init()
		myfont = font.SysFont('consolas', 30)
		textsurface = myfont.render('About', True, (255, 255, 255))
		screen.blit(textsurface,(50, 100))

		myfont = font.SysFont('consolas', 18)

		textsurface = myfont.render('Desenvolvido por Guilherme, Júlia e Hideki', True, (255, 255, 255))

		screen.blit(textsurface,(16, 204))
		
		# s = 'Pac-Man (conhecido em japonês com o nome de Puckman ou パックマン) é um jogo eletrônico criado pelo Tōru Iwatani para a empresa Namco, e sendo distribuído para o mercado americano pela Midway Games. Produzido originalmente para Arcade no início dos anos 1980, tornou-se um dos jogos mais jogados e populares no momento, tendo versões para diversos consoles e continuações para tantos outros, inclusive na atualidade'
		textsurface = myfont.render('Programação de Microcontroladores', True, (255, 255, 255))

		screen.blit(textsurface,(56, 224))

		myfont = font.SysFont('consolas', 20)

		textsurface = myfont.render('Pacman em Python -> PyCman', True, (255, 255, 255))

		screen.blit(textsurface,(76,324))

		if back:
			textsurface = myfont.render('Go Back', True, (200, 200, 200))
		else:
			textsurface = myfont.render('Go Back', True, (255, 255, 255))

		screen.blit(textsurface,(200,424))


		