from .SceneBase import SceneBase

from ..objects.Pacman import Pacman

from ..objects.ghosts.Blinky    import Blinky
from ..objects.ghosts.Inky      import Inky
from ..objects.ghosts.Pinky     import Pinky
from ..objects.ghosts.Clyde     import Clyde

from ..Map import Map

from ...view.CharacterSprite import CharacterSprite
from ...view.Spriteset_Map import Spriteset_Map

class GameScene(SceneBase):

    def __init__(self):
        self.setupPlayer()
        self.setupGhosts()
        self.setupMap()
        self.createSpriteset()
        self._power_countdown = 0

    def setupPlayer(self):
        self._player = Pacman()
        self._player.on('death', self._pacman_died)

    def setupGhosts(self):
        self._ghosts = [
            Blinky(),
            Clyde(),
            Inky(),
            Pinky()
        ]
        for ghost in self._ghosts:
            ghost.on('death', lambda: ghost.set_state(Ghost.DEAD))

    def setupMap(self):
        self._map = Map('map.dat')

    def createSpriteset(self):
        self._spriteset = Spriteset_Map(self._player, self._map, self._ghosts)

    def _pacman_died(self):
        pass

    def update(self):
        self._player.update(self._map)

        for ghost in self._ghosts:
            ghost.update(self._map, self._player)

    def render(self, screen):
        self._spriteset.render(screen)