from dataclasses import dataclass

from .player import PlayerState
from .tile import TileState
from .matter import Matter


@dataclass
class GameState:
    player: PlayerState
    tiles: list[TileState]

    def get_matters(self) -> list[Matter]:
        return [
            getattr(self, obj)
            for obj in dir(self)
            if isinstance(getattr(self, obj), Matter)
        ]
