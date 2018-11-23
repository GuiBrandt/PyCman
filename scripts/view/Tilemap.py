import io, os
import pygame
from enum import Enum
from pygame import image
from ..model.Map import Map

class Tilemap:
    """Classe de vizualização de mapa do jogo"""

    TILESET_SPRITE = 'tileset.png'
    TILESET_COLS = 3
    TILE_SIZE = 8

    def __init__(self, filename, m):
        """
            Construtor

            filename    : Nome do arquivo de paredes
            m           : Map
        """

        file = io.open(os.path.join('assets/', filename), 'r')
        self.__map = m

        self.__width, self.__height = map(int, file.readline().split())
        self.__wall_sprite = ''
        for i in range(self.__height):
            self.__wall_sprite += file.readline().rstrip("\n\r")

        self.__tile_sprite = pygame.image.load(os.path.join('assets/', Tilemap.TILESET_SPRITE))

    def __get_wall_info(self, x, y):
        """
            Obtém o tipo de parede assim como sua rotação.
            O mapa contém informações agrupadas de dois em dois números,
            significando sua posição e rotação respectivamente.

            x, y    : Coordenadas no mapa
        """
        pos = y * 2 * self.__width + 2 * x
        return (int(self.__wall_sprite[pos]), int(self.__wall_sprite[pos + 1]))

    def __get_tile_info (self, x, y):
        """
            Descobre o tipo específico de pedaço por meio dos arredores da coordenada
        """

        # if Map.__get_tile_at(x, y) == Map.Tile.WALL_D or Map.__get_tile_at(x, y) == Map.Tile.WALL_S:
        #     if x == 0:
        #         if y == 0:
        #             return (0, 0)
        #         elif y == Map.__heigth - 1:
        #             return (0, 3)
        #         else:
        #             if top == Map.Tile.WALL_D and bottom == Map.Tile.WALL_D:
        #                 if right == Map.Tile.WALL_s:
        #                     if Map.__get_tile_at(x + 1, y - 1) ==  Map.Tile.WALL_D:
        #                 else:
        #                     return ()
        cell = self.__map.get_tile(x, y)

        if cell == Map.Tile.WALL:
            wall_info = self.__get_wall_info(x, y)
            x_pos = (wall_info[0] % Tilemap.TILESET_COLS) * Tilemap.TILE_SIZE
            y_pos = (wall_info[0] // Tilemap.TILESET_COLS) * Tilemap.TILE_SIZE
            return (x_pos, y_pos, wall_info[1])
        else:
            return (int(cell.value) * Tilemap.TILE_SIZE, 2 * Tilemap.TILE_SIZE, 0)

    def draw(self, screen, offset):
        """
            Desenhar o mapa de acordo com o arquivo da classe Map
        """
        for x in range(0, self.__width):
            for y in range(0, self.__height):
                tile_info = self.__get_tile_info(x, y)
                x_pos = tile_info[0]
                y_pos = tile_info[1]
                rot = tile_info[2]

                tile = pygame.Surface((Tilemap.TILE_SIZE, Tilemap.TILE_SIZE))
                tile.blit(self.__tile_sprite, (0, 0), (x_pos, y_pos, Tilemap.TILE_SIZE, Tilemap.TILE_SIZE))
                tile = pygame.transform.rotate(tile, 360 - (90 * rot))
                tile = pygame.transform.scale2x(tile)
                screen.blit(tile, (x * Tilemap.TILE_SIZE * 2 + offset[0], y * Tilemap.TILE_SIZE * 2 + offset[1]))
