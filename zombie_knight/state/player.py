from __future__ import annotations

import pygame

from dataclasses import dataclass, replace
from enum import Enum

from .matter import Matter
from .direction import HorizontalDirection


class PlayerMode(Enum):
    idle = 0
    walking = 1
    jumping = 2
    attacking = 3


@dataclass
class PlayerState(Matter):
    rect: pygame.Rect
    mode: PlayerMode
    horizontal_direction: HorizontalDirection
    animation_index: int
    lives: int
    score: int
    velocity: pygame.Vector2
    acceleration: pygame.Vector2

    def get_position(self) -> pygame.Vector2:
        position = pygame.Vector2(
            self.rect.x,
            self.rect.y,
        )

        return position

    def get_velocity(self) -> pygame.Vector2:
        return self.velocity

    def get_acceleration(self) -> pygame.Vector2:
        return self.acceleration

    def replace_position(self, position: pygame.Vector2) -> PlayerState:
        return replace(
            self,
            rect=pygame.Rect(
                position.x,
                position.y,
                self.rect.width,
                self.rect.height,
            ),
        )

    def replace_velocity(self, velocity: pygame.Vector2) -> PlayerState:
        return replace(
            self,
            velocity=velocity,
        )

    def replace_acceleration(self, acceleration: pygame.Vector2) -> PlayerState:
        return replace(
            self,
            acceleration=acceleration,
        )
