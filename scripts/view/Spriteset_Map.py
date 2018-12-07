from .CharacterSprite import CharacterSprite
from .Tilemap import Tilemap
from .HUD import HUD

MAP_OFFSET = (0, 48)

class Spriteset_Map:

    def __init__(self, player, _map, ghosts):
        self._player = CharacterSprite(player)
        self._map = Tilemap('wallSprite.dat', _map)
        self._ghosts = list(map(lambda g: CharacterSprite(g), ghosts))
        self._hud = HUD(player)

    def render(self, screen):
        self._map.render(screen, MAP_OFFSET)
        self._player.render(screen, MAP_OFFSET)
        self._hud.render(screen)

        for ghost in self._ghosts:
            ghost.render(screen, MAP_OFFSET)