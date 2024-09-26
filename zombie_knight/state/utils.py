import pygame

from .tile import (
    DirtTileState,
    GrassTileState,
    LeftTileState,
    RightTileState,
    TileState,
)
from ..constants.tile import TILE_SIZE


def create_tiles_from_tile_map(tile_map: list[list[int]]) -> list[TileState]:
    """
    Creates a list of tile states from a tile map.

    Args:
        tile_map (list[list[int]]): The tile map.

    Returns:
        list[TileState]: The list of tile states.
    """
    width, height = TILE_SIZE
    tiles = []
    for y, row in enumerate(tile_map):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * width, y * height, width, height)
            if tile == 1:
                tiles.append(GrassTileState(rect=rect))
            elif tile == 2:
                tiles.append(DirtTileState(rect=rect))
            elif tile == 3:
                tiles.append(LeftTileState(rect=rect))
            elif tile == 4:
                tiles.append(RightTileState(rect=rect))

    return tiles
