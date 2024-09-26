import pygame

from dataclasses import dataclass


@dataclass
class TileState:
    rect: pygame.Rect


class GrassTileState(TileState):
    pass


class DirtTileState(TileState):
    pass


class RightTileState(TileState):
    pass


class LeftTileState(TileState):
    pass
