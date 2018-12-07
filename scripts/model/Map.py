import io, os, pygame
from enum import Enum

class Map:
    """Classe de modelo de mapa do jogo"""

    class Tile(Enum):
        """Enumeração de tipos de tile no mapa"""
        EMPTY = 0
        POINT = 1
        BONUS = 2
        WALL = 3

    # Mapa de caracteres do arquivo para tipos de tile
    __TILE_DICT = {
        '/': Tile.EMPTY,
        '.': Tile.POINT,
        'o': Tile.BONUS,
        'x': Tile.WALL
    }

    def __init__(self, filename):
        """
            Construtor

            filename    : Nome do arquivo de passabilidade do mapa
        """

        file = io.open(os.path.join('assets/', filename), 'r')
        self.__width, self.__height = map(int, file.readline().split())
        
        self.__map = ''
        for i in range(self.__height):
            self.__map += file.readline().rstrip("\n\r")

    def __get_tile_at(self, x, y):
        """
            Obtém o tipo de tile em uma posição no mapa

            x, y    : Coordenadas no mapa
        """
        index = (y % self.__height) * self.__width + (x % self.__width)
        return self.__map[index] if index > 0 and index < len(self.__map) else '/'

    def set_tile_at(self, x, y, tile):
        """
            Obtém o tipo de tile em uma posição no mapa

            x, y    : Coordenadas no mapa
        """
        index = y * self.__width + x
        tile_char = dict(map(reversed, Map.__TILE_DICT.items()))[tile]

        self.__map = self.__map[:index] + tile_char + self.__map[index+1:]

    def is_passable(self, x, y):
        """
            Determina se uma posição no mapa é passável
        
            x, y    : Coordenadas no mapa
        """
        return self.__get_tile_at(x, y).lower() != 'x'

    def get_tile(self, x, y):
        """
            Obtém o tipo de tile numa posição do mapa

            x, y    : Coordenadas no mapa
        """
        return Map.__TILE_DICT[self.__get_tile_at(x, y)]