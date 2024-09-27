from __future__ import annotations

import pygame

from abc import ABC, abstractmethod


class Matter(ABC):
    @abstractmethod
    def get_position(self) -> pygame.Vector2:
        """
        Gets the position of the matter.

        Returns:
            pygame.Vector2: The position of the matter.
        """
        pass

    @abstractmethod
    def get_velocity(self) -> pygame.Vector2:
        """
        Gets the velocity of the matter.

        Returns:
            pygame.Vector2: The velocity of the matter.
        """
        pass

    @abstractmethod
    def get_acceleration(self) -> pygame.Vector2:
        """
        Gets the acceleration of the matter.

        Returns:
            pygame.Vector2: The acceleration of the matter.
        """
        pass

    @abstractmethod
    def replace_position(self, position: pygame.Vector2) -> Matter:
        """
        Replaces the position of the matter.

        Args:
            position (pygame.Vector2): The new position of the matter.

        Returns:
            Matter: The matter with the new position.
        """
        pass

    @abstractmethod
    def replace_velocity(self, velocity: pygame.Vector2) -> Matter:
        """
        Replaces the velocity of the matter.

        Args:
            velocity (pygame.Vector2): The new velocity of the matter.

        Returns:
            Matter: The matter with the new velocity.
        """
        pass

    @abstractmethod
    def replace_acceleration(self, acceleration: pygame.Vector2) -> Matter:
        """
        Replaces the acceleration of the matter.

        Args:
            acceleration (pygame.Vector2): The new acceleration of the matter.

        Returns:
            Matter: The matter with the new acceleration.
        """
        pass
