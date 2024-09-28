import pygame

from typing import Callable
from dataclasses import replace

from ..state.game_state import GameState
from ..state.tile import TileState
from ..state.collidable import Collidable


class CollideTileRule:
    def __init__(self, tile_margin: int = 2) -> None:
        self.tile_margin = tile_margin

    def __call__(self, game_state: GameState) -> GameState:
        """
        Applies the collide tile rule to the game state.
        This rule controls interactions between collidables and tiles.

        Args:
            game_state (GameState): The game state to apply the collide tile rule to.

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

        velocity = collidable.get_velocity()
        if rect.bottom <= tile.rect.bottom and velocity.y >= 0:
            return pygame.Vector2(
                rect.x,
                tile.rect.top - rect.height + self.tile_margin,
            )
        else:
            return pygame.Vector2(rect.x, rect.y + 2)

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

        velocity = collidable.get_velocity()
        return pygame.Vector2(velocity.x, 0)

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
