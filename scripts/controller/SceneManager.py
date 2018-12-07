from ..model.Map import Map
from ..view.Tilemap import Tilemap
from ..model.scenes.GameScene import GameScene
from ..model.scenes.TitleScene import TitleScene

class SceneManager:
    
    def init():
        SceneManager._scene = TitleScene()
        #SceneManager._scene = GameScene()
    
    def render(screen):
        SceneManager._scene.render(screen)

    def call(scene):
        SceneManager._scene = scene()

    def update():
        SceneManager._scene.update()