import pygame

from typing import Callable
from dataclasses import replace

from ...state.matter import Matter
from ...state.game_state import GameState
from ...constants.physics import GRAVITY_ACCELERATION_CONST


class GravityRule:
    """
    Gravity rule.
    """

    def __call__(
        self,
        game_state: GameState,
        events: list[pygame.event.Event],
    ) -> GameState:
        """
        Applies the gravity rule to all matters in the game state.

        Args:
            game_state (GameState): The game state to apply the gravity rule to.
            events (list[pygame.event.Event]): The events occurred in the current frame.

        Returns:
            GameState: The new game state with the gravity rule applied.
        """

        def apply_gravity(matter: Matter) -> Matter:
            acceleration = matter.get_acceleration()
            new_acceleration = pygame.Vector2(
                acceleration.x, GRAVITY_ACCELERATION_CONST
            )
            return matter.replace_acceleration(new_acceleration)

        return apply_on_game_state_matters(
            apply_gravity,
            game_state,
        )


class AccelerationRule:
    """
    Acceleration rule.
    """

    def __call__(
        self,
        game_state: GameState,
        events: list[pygame.event.Event],
    ) -> GameState:
        """
        Applies the acceleration rule to all matters in the game state.

        Args:
            game_state (GameState): The game state to apply the acceleration rule to.
            events (list[pygame.event.Event]): The events occurred in the current frame.

        Returns:
            GameState: The new game state with the acceleration rule applied.
        """

        def apply_acceleration(matter: Matter) -> Matter:
            acceleration = matter.get_acceleration()
            new_velocity = matter.get_velocity() + acceleration
            return matter.replace_velocity(new_velocity)

        return apply_on_game_state_matters(
            apply_acceleration,
            game_state,
        )


class VelocityRule:
    """
    Velocity rule.
    """

    def __call__(
        self,
        game_state: GameState,
        events: list[pygame.event.Event],
    ) -> GameState:
        """
        Applies the velocity rule to all matters in the game state.

        Args:
            game_state (GameState): The game state to apply the velocity rule to.
            events (list[pygame.event.Event]): The events occurred in the current frame.

        Returns:
            GameState: The new game state with the velocity rule applied.
        """

        def apply_velocity(matter: Matter) -> Matter:
            velocity = matter.get_velocity()
            new_position = matter.get_position() + velocity
            return matter.replace_position(new_position)

        return apply_on_game_state_matters(
            apply_velocity,
            game_state,
        )


def apply_on_game_state_matters(
    f: Callable[[Matter], Matter],
    game_state: GameState,
) -> GameState:
    """
    Applies a function to each matter in the game state.

    Args:
        f (Callable[[Matter], Matter]): The function to apply to each matter.
        game_state (GameState): The game state to apply the function to.

    Returns:
        GameState: The new game state with the function applied to each matter.
    """
    matters = game_state.get_matters()
    attr_to_new_matter: dict[str, Matter] = {}
    for attr, matter in matters:
        new_matter = f(matter)
        attr_to_new_matter[attr] = new_matter

    return replace(
        game_state,
        **attr_to_new_matter,
    )
