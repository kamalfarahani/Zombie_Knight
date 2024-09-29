import pygame

from typing import Callable
from dataclasses import replace

from ..state.game_state import GameState
from ..state.tile import TileState
from ..state.collidable import Collidable


class CollideTileRule:
    def __init__(self, tile_margin: int = 2) -> None:
        self.tile_margin = tile_margin

    def __call__(
        self,
        game_state: GameState,
        events: list[pygame.event.Event],
    ) -> GameState:
        """
        Applies the collide tile rule to the game state.
        This rule controls interactions between collidables and tiles.

        Args:
            game_state (GameState): The game state to apply the collide tile rule to.
            events (list[pygame.event.Event]): The events occurred in the current frame.

        Returns:
            GameState: The new game state with the collide tile rule applied.
        """

        def apply_collide_tile(collidable: Collidable) -> Collidable:
            tile_states = game_state.tiles
            new_position = self.get_new_position(collidable, tile_states)
            new_velocity = self.get_new_velocity(collidable, tile_states)

            return collidable.replace_collision_rect_position(
                new_position
            ).replace_collidable_velocity(new_velocity)

        return apply_on_game_state_collidables(
            apply_collide_tile,
            game_state,
        )

    def get_new_position(
        self,
        collidable: Collidable,
        tile_states: list[TileState],
    ) -> pygame.Vector2:
        rect = collidable.get_collision_rect()
        tile = self.get_colliding_tile(collidable, tile_states)
        if tile is None:
            return pygame.Vector2(rect.x, rect.y)

        if self.is_colliding_from_top(collidable, tile):
            return pygame.Vector2(
                rect.x,
                tile.rect.top - rect.height + self.tile_margin,
            )
        elif self.is_colliding_from_bottom(collidable, tile):
            return pygame.Vector2(
                rect.x,
                tile.rect.bottom + self.tile_margin,
            )
        elif self.is_colliding_from_left(collidable, tile):
            return pygame.Vector2(
                tile.rect.left - rect.width - self.tile_margin,
                rect.y,
            )
        elif self.is_colliding_from_right(collidable, tile):
            return pygame.Vector2(
                tile.rect.right + self.tile_margin,
                rect.y,
            )
        else:
            return pygame.Vector2(rect.x, rect.y)

    def get_new_velocity(
        self,
        collidable: Collidable,
        tile_states: list[TileState],
    ) -> pygame.Vector2:
        """
        Gets the new velocity of the collidable.

        Args:
            collidable (Collidable): The collidable to get the new velocity of.
            tile_states (list[TileState]): The list of tile states.

        Returns:
            pygame.Vector2: The new velocity of the collidable.
        """
        tile = self.get_colliding_tile(collidable, tile_states)
        if tile is None:
            return collidable.get_velocity()

        if self.is_colliding_from_top(collidable, tile):
            return pygame.Vector2(collidable.get_velocity().x, 0)
        elif self.is_colliding_from_bottom(collidable, tile):
            return pygame.Vector2(collidable.get_velocity().x, 0)
        elif self.is_colliding_from_left(collidable, tile):
            return pygame.Vector2(0, collidable.get_velocity().y)
        elif self.is_colliding_from_right(collidable, tile):
            return pygame.Vector2(0, collidable.get_velocity().y)
        else:
            return collidable.get_velocity()

    def get_colliding_tile(
        self,
        collidable: Collidable,
        tile_states: list[TileState],
    ) -> TileState | None:
        """
        Gets the colliding tile of the collidable.

        Args:
            collidable (Collidable): The collidable to get the colliding tile of.
            tile_states (list[TileState]): The list of tile states.

        Returns:
            TileState | None: The colliding tile of the collidable or None if no collision.
        """
        rect = collidable.get_collision_rect()
        for tile in tile_states:
            if rect.colliderect(tile.rect):
                return tile
        return None

    def is_colliding_from_top(
        self,
        collidable: Collidable,
        tile_state: TileState,
    ) -> bool:
        """
        Checks if the collidable is colliding from the top of the tile.

        Args:
            collidable (Collidable): The collidable to check.
            tile_state (TileState): The tile state to check against.

        Returns:
            bool: True if the collidable is colliding from the top of the tile, False otherwise.
        """
        rect = collidable.get_collision_rect()
        velocity = collidable.get_velocity()
        return (
            rect.colliderect(tile_state.rect)
            and rect.bottom <= tile_state.rect.centery
            and velocity.y >= 0
        )

    def is_colliding_from_bottom(
        self,
        collidable: Collidable,
        tile_state: TileState,
    ) -> bool:
        """
        Checks if the collidable is colliding from the bottom of the tile.

        Args:
            collidable (Collidable): The collidable to check.
            tile_state (TileState): The tile state to check against.

        Returns:
            bool: True if the collidable is colliding from the bottom of the tile, False otherwise.
        """
        rect = collidable.get_collision_rect()
        velocity = collidable.get_velocity()
        return (
            rect.colliderect(tile_state.rect)
            and rect.top >= tile_state.rect.centery
            and velocity.y <= 0
        )

    def is_colliding_from_left(
        self,
        collidable: Collidable,
        tile_state: TileState,
    ) -> bool:
        """
        Checks if the collidable is colliding from the left of the tile.

        Args:
            collidable (Collidable): The collidable to check.
            tile_state (TileState): The tile state to check against.

        Returns:
            bool: True if the collidable is colliding from the left of the tile, False otherwise.
        """
        rect = collidable.get_collision_rect()
        velocity = collidable.get_velocity()
        return (
            rect.colliderect(tile_state.rect)
            and rect.right <= tile_state.rect.centerx
            and velocity.x >= 0
        )

    def is_colliding_from_right(
        self,
        collidable: Collidable,
        tile_state: TileState,
    ) -> bool:
        """
        Checks if the collidable is colliding from the right of the tile.

        Args:
            collidable (Collidable): The collidable to check.
            tile_state (TileState): The tile state to check against.

        Returns:
            bool: True if the collidable is colliding from the right of the tile, False otherwise.
        """
        rect = collidable.get_collision_rect()
        velocity = collidable.get_velocity()
        return (
            rect.colliderect(tile_state.rect)
            and rect.left >= tile_state.rect.centerx
            and velocity.x <= 0
        )


def apply_on_game_state_collidables(
    f: Callable[[Collidable], Collidable],
    game_state: GameState,
) -> GameState:
    """
    Applies a function to each collidable in the game state.

    Args:
        f (Callable[[Collidable], Collidable]): The function to apply to each collidable.
        game_state (GameState): The game state to apply the function to.

    Returns:
        GameState: The new game state with the function applied to each collidable.
    """
    collidables = game_state.get_collidables()
    attr_to_new_collidables: dict[str, Collidable] = {}
    for attr, collidable in collidables:
        new_collidable = f(collidable)
        attr_to_new_collidables[attr] = new_collidable

    return replace(
        game_state,
        **attr_to_new_collidables,
    )
