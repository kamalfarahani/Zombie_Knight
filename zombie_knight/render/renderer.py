import pygame

from .tile import create_tile_sprites
from ..state.game_state import GameState
from ..state.tile import TileState
from ..constants.paths import BACKGROUND_IMAGE_PATH


class Renderer:
    def __init__(
        self,
        display: pygame.Surface,
    ) -> None:
        self.display = display
        self.background_image = pygame.transform.scale(
            pygame.image.load(BACKGROUND_IMAGE_PATH),
            self.display.get_size(),
        )

    def render(
        self,
        game_state: GameState,
    ) -> None:
        self.render_background()
        self.render_tiles(game_state.tiles)

    def render_background(self) -> None:
        self.display.blit(self.background_image, (0, 0))

    def render_tiles(
        self,
        tile_states: list[TileState],
    ) -> None:
        tile_sprites = create_tile_sprites(tile_states)
        for tile in tile_sprites:
            self.display.blit(tile.image, tile.rect)
