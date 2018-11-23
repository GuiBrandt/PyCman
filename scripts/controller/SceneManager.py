from ..model.Map import Map
from ..view.Tilemap import Tilemap

class SceneManager:
    
    def render(screen):
        map = Map('map.dat')
        tile_map = Tilemap('wallSprite.dat', map)
        tile_map.draw(screen, (0, 58))