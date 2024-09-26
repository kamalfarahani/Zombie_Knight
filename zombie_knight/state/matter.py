import pygame

from abc import ABC, abstractmethod


class Matter(ABC):
    @abstractmethod
    def get_velocity(self) -> pygame.Vector2:
        pass

    @abstractmethod
    def get_acceleration(self) -> pygame.Vector2:
        pass
