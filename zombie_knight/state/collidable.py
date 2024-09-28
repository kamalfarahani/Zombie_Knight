from __future__ import annotations

import pygame

from abc import abstractmethod

from .matter import Matter


class Collidable(Matter):
    @abstractmethod
    def get_collision_rect(self) -> pygame.Rect:
        """
        Gets the collision rect of the collidable.

        Returns:
            pygame.Rect: The collision rect of the collidable.
        """
        pass

    @abstractmethod
    def replace_collision_rect_position(self, position: pygame.Vector2) -> Collidable:
        """
        Replaces the position of the collision rect of the collidable.

        Args:
            position (pygame.Vector2): The new position of the collision rect of the collidable.

        Returns:
            Collidable: The collidable with the new position of the collision rect.
        """
        pass

    @abstractmethod
    def replace_collidable_velocity(self, velocity: pygame.Vector2) -> Collidable:
        """
        Replaces the velocity of the collidable.

        Args:
            velocity (pygame.Vector2): The new velocity of the collidable.

        Returns:
            Collidable: The collidable with the new velocity.
        """
        pass
