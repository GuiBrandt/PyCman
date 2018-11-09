import io
from enum import Enum

class Map:
    """Classe de modelo de mapa do jogo"""

    class Tile(Enum):
        """Enumeração de tipos de tile no mapa"""
        EMPTY = 0
        WALL_S = 2
        WALL_D = 3
        POINT = 4
        BONUS = 5

    # Mapa de caracteres do arquivo para tipos de tile
    __TILE_DICT = {
        '\'':   Tile.EMPTY,
        's':    Tile.WALL_S,
        'd':    Tile.WALL_D,
        '.':    Tile.POINT,
        'o':    Tile.BONUS
    }

    def __init__(filename):
        """
            Construtor

            filename    : Nome do arquivo de passabilidade do mapa
        """

        file = io.open(filename, "r")
        __width, __height = map(int, file.readline().split())
        
        __map = ""
        for i in range(__height):
            __map += file.readline().rstrip("\n\r")

    def __get_tile_at(x, y):
        """
            Obtém o tipo de tile em uma posição no mapa

            x, y    : Coordenadas no mapa
        """
        return __map[y * __width + x]

    def is_passable(x, y):
        """
            Determina se uma posição no mapa é passável
        
            x, y    : Coordenadas no mapa
        """
        return __get_tile_at(x, y).lower() != 'x'

    def get_tile(x, y):
        """
            Obtém o tipo de tile numa posição do mapa

            x, y    : Coordenadas no mapa
        """
        return __TILE_DICT[__get_tile_at(x, y)]