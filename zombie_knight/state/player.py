from __future__ import annotations

import pygame

from dataclasses import dataclass, replace
from enum import Enum

from .collidable import Collidable
from .direction import HorizontalDirection


class PlayerMode(Enum):
    IDLE = 0
    RUNNING = 3
    ATTACKING = 1
    JUMPING = 2


@dataclass
class PlayerState(Collidable):
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

    def get_collision_rect(self) -> pygame.Rect:
        return self.rect

    def replace_position(self, position: pygame.Vector2) -> PlayerState:
        return replace(
            self,
            rect=pygame.Rect(
                round(position.x),
                round(position.y),
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

    def replace_collision_rect_position(self, position: pygame.Vector2) -> Collidable:
        return self.replace_position(position)

    def replace_collidable_velocity(self, velocity: pygame.Vector2) -> Collidable:
        return self.replace_velocity(velocity)
