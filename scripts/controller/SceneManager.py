from ..model.Map import Map
from ..view.Tilemap import Tilemap
from ..model.scenes.GameScene import GameScene

class SceneManager:
    
    def init():
        SceneManager._scene = GameScene()

    def render(screen):
        SceneManager._scene.render(screen)

    def update():
        SceneManager._scene.update()