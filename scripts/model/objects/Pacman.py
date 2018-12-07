from .Character import Character
from ..Map import Map

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

	def update(self, map):
		super().update(map)
		#if morreu:
		#	self._trigger('death')]
		if self._power_countdown >= 0:
			self._power_countdown -= 1
		elif self.power == True:
			self.power = False

		cell_at = map.get_tile(self.x, self.y)

		if cell_at == Map.Tile.POINT:
			map.set_tile_at(self.x, self.y, Map.Tile.EMPTY)
			self.points += 10
		elif cell_at == Map.Tile.BONUS:
			map.set_tile_at(self.x, self.y, Map.Tile.EMPTY)
			self.power = True
			self._power_countdown = 300

	def get_sprite_index(self):
		return 0