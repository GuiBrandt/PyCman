from .Ghost import Ghost

class Inky(Ghost):

	def __init__(self):
		super().__init__()
	
	def get_sprite_index(self):
		return 5