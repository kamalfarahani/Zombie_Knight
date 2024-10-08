from dataclasses import dataclass

from .player import PlayerState
from .tile import TileState
from .matter import Matter
from .collidable import Collidable


@dataclass
class GameState:
    player: PlayerState
    tiles: list[TileState]

    def get_matters(self) -> list[tuple[str, Matter]]:
        return [
            (attr, getattr(self, attr))
            for attr in dir(self)
            if isinstance(getattr(self, attr), Matter)
        ]

    def get_collidables(self) -> list[tuple[str, Collidable]]:
        return [
            (attr, getattr(self, attr))
            for attr in dir(self)
            if isinstance(getattr(self, attr), Collidable)
        ]
