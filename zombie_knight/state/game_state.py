from dataclasses import dataclass

from .player import PlayerState
from .tile import TileState


@dataclass
class GameState:
    player: PlayerState
    tiles: list[TileState]
