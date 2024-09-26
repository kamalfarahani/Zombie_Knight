import pygame

from ..state.tile import (
    TileState,
    GrassTileState,
    DirtTileState,
    LeftTileState,
    RightTileState,
)
from ..constants.paths import (
    DIRT_TILE_IMAGE_PATH,
    GRASS_TILE_IMAGE_PATH,
    LEFT_TILE_IMAGE_PATH,
    RIGHT_TILE_IMAGE_PATH,
)
from ..constants.tile import TILE_SIZE


dirt_tile_image = pygame.image.load(DIRT_TILE_IMAGE_PATH)
grass_tile_image = pygame.image.load(GRASS_TILE_IMAGE_PATH)
left_tile_image = pygame.image.load(LEFT_TILE_IMAGE_PATH)
right_tile_image = pygame.image.load(RIGHT_TILE_IMAGE_PATH)


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        state: TileState,
        image: pygame.Surface,
    ) -> None:
        """
        Initializes the tile.

        Args:
            state (TileState): The state of the tile.
            image (pygame.Surface): The image of the tile.

        Returns:
            None
        """
        super().__init__()

        self.rect = state.rect
        self.image = pygame.transform.scale(image, TILE_SIZE)


class DirtTile(Tile):
    def __init__(
        self,
        state: DirtTileState,
    ) -> None:
        """
        Initializes the dirt tile.

        Args:
            state (DirtTileState): The state of the tile.

        Returns:
            None
        """
        super().__init__(state, dirt_tile_image)


class GrassTile(Tile):
    def __init__(
        self,
        state: GrassTileState,
    ) -> None:
        """
        Initializes the grass tile.

        Args:
            state (GrassTileState): The state of the tile.

        Returns:
            None
        """
        super().__init__(state, grass_tile_image)


class RightTile(Tile):
    def __init__(
        self,
        state: RightTileState,
    ) -> None:
        """
        Initializes the right tile.

        Args:
            state (RightTileState): The state of the tile.

        Returns:
            None
        """
        super().__init__(state, right_tile_image)


class LeftTile(Tile):
    def __init__(
        self,
        state: LeftTileState,
    ) -> None:
        """
        Initializes the left tile.

        Args:
            state (LeftTileState): The state of the tile.

        Returns:
            None
        """
        super().__init__(state, left_tile_image)


def create_tile_sprites(tiles: list[TileState]) -> list[Tile]:
    """
    Creates a list of tile sprites from a list of tile states.

    Args:
        tiles (list[TileState]): The list of tile states.

    Returns:
        list[Tile]: The list of tile sprites.
    """
    state_to_sprite = {
        TileState: GrassTile,
        GrassTileState: GrassTile,
        DirtTileState: DirtTile,
        RightTileState: RightTile,
        LeftTileState: LeftTile,
    }

    tile_sprites = []
    for tile in tiles:
        tile_sprites.append(state_to_sprite[type(tile)](tile))

    return tile_sprites
