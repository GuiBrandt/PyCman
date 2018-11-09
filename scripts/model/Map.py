import io

class Map:
    def __init__(filename):
        """Construtor"""
        __map = 

    def __get_tile_at(x, y):
        return __map

    def is_passable(x, y):
        """
            Determina se uma posição no mapa é passável
        
            x, y    : Coordenadas no mapa
        """
        return __get_tile_at(x, y) != 'x'

    def get_tile(x, y):
        """
            Obtém o tipo de tile numa posição do mapa

            x, y    : Coordenadas no mapa
        """
        return __get_tile_at(x, y)