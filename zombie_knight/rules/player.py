import pygame

from dataclasses import replace

from ..state.game_state import GameState
from ..state.player import PlayerState, PlayerMode
from ..state.direction import HorizontalDirection


class PlayerMoveRule:
    def __init__(
        self,
        horizontal_acceleration: float,
        horizontal_friction: float,
    ) -> None:
        """
        Initializes the player move rule.

        Args:
            horizontal_acceleration (float): The horizontal acceleration of the player.
            horizontal_friction (float): The horizontal friction of the player.

        Returns:
            None
        """
        self.horizontal_acceleration = horizontal_acceleration
        self.horizontal_friction = horizontal_friction

    def __call__(
        self,
        game_state: GameState,
        events: list[pygame.event.Event],
    ) -> GameState:
        """
        Applies the player move rule to the game state.

        Args:
            game_state (GameState): The game state to apply the player move rule to.
            events (list[pygame.event.Event]): The events occurred in the current frame.

        Returns:
            GameState: The new game state with the player move rule applied.
        """
        key_to_horizontal_acceleration = {
            pygame.K_LEFT: -self.horizontal_acceleration,
            pygame.K_RIGHT: self.horizontal_acceleration,
        }

        def get_horizontal_acceleration() -> float:
            for key, horizontal_acceleration in key_to_horizontal_acceleration.items():
                if pygame.key.get_pressed()[key]:
                    return horizontal_acceleration
            return 0.0

        horizontal_acceleration = get_horizontal_acceleration()
        new_acceleration = self.get_new_acceleration(
            game_state.player,
            horizontal_acceleration,
        )
        new_mode = self.get_player_mode(
            game_state.player,
            horizontal_acceleration,
        )
        new__horizontal_direction = self.get_new_horizontal_direction(
            game_state.player,
            horizontal_acceleration,
        )

        return replace(
            game_state,
            player=replace(
                game_state.player,
                acceleration=new_acceleration,
                mode=new_mode,
                horizontal_direction=new__horizontal_direction,
            ),
        )

    def get_new_acceleration(
        self,
        player_state: PlayerState,
        horizontal_acceleration: float,
    ) -> pygame.Vector2:
        """
        Returns the new acceleration of the player.

        Args:
            player_state (PlayerState): The state of the player.
            horizontal_acceleration (float): The horizontal acceleration of the player.

        Returns:
            pygame.Vector2: The new acceleration of the player.
        """
        acc_x = (
            horizontal_acceleration - self.horizontal_friction * player_state.velocity.x
        )

        return pygame.Vector2(
            acc_x,
            player_state.acceleration.y,
        )

    def get_player_mode(
        self,
        player_state: PlayerState,
        horizontal_acceleration: float,
    ) -> PlayerMode:
        """
        Returns the new mode of the player.

        Args:
            player_state (PlayerState): The state of the player.
            horizontal_acceleration (float): The horizontal acceleration of the player.

        Returns:
            PlayerMode: The new mode of the player.
        """
        if horizontal_acceleration == 0.0:
            if player_state.mode == PlayerMode.RUNNING:
                return PlayerMode.IDLE
            else:
                return player_state.mode

        return PlayerMode.RUNNING

    def get_new_horizontal_direction(
        self,
        player_state: PlayerState,
        horizontal_acceleration: float,
    ) -> HorizontalDirection:
        """
        Returns the new horizontal direction of the player.

        Args:
            player_state (PlayerState): The state of the player.
            horizontal_acceleration (float): The horizontal acceleration of the player.

        Returns:
            HorizontalDirection: The new horizontal direction of the player.
        """
        if horizontal_acceleration == 0.0:
            return player_state.horizontal_direction
        elif horizontal_acceleration < 0.0:
            return HorizontalDirection.LEFT
        else:
            return HorizontalDirection.RIGHT


class PlayerJumpRule:
    def __init__(
        self,
        jump_velocity: float,
    ) -> None:
        """
        Initializes the player jump rule.

        Args:
            jump_velocity (float): The jump velocity of the player.

        Returns:
            None
        """
        self.jump_velocity = jump_velocity

    def __call__(
        self,
        game_state: GameState,
        events: list[pygame.event.Event],
    ) -> GameState:
        """
        Applies the player jump rule to the game state.

        Args:
            game_state (GameState): The game state to apply the player jump rule to.
            events (list[pygame.event.Event]): The events occurred in the current frame.

        Returns:
            GameState: The new game state with the player jump rule applied.
        """
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                new_velocity = pygame.Vector2(
                    game_state.player.velocity.x,
                    -self.jump_velocity,
                )
                return replace(
                    game_state,
                    player=replace(
                        game_state.player,
                        velocity=new_velocity,
                        mode=PlayerMode.JUMPING,
                    ),
                )

        return game_state
