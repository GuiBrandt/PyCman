from ..model.objects.Pacman import Pacman

class GameManager:
    """Gerenciador dos objetos do jogo"""

    def init():
        """Inicializa os objetos e valores do jogo"""
        __score = 0
        __player = Pacman()

    def get_screen_size():
        """Determina o tamanho da tela do jogo"""
        return (224 * 2, 288 * 2 + 32)