import pygame

from dataclasses import dataclass
from enum import Enum

from .matter import Matter


class PlayerMode(Enum):
    idle = 0
    walking = 1
    jumping = 2
    attacking = 3


@dataclass
class PlayerState(Matter):
    rect: pygame.Rect
    mode: PlayerMode
    lives: int
    score: int
    velocity: pygame.Vector2
    acceleration: pygame.Vector2

    def get_velocity(self) -> pygame.Vector2:
        return self.velocity

    def get_acceleration(self) -> pygame.Vector2:
        return self.acceleration
