import pygame

from .render.renderer import Renderer
from .state.game_state import GameState
from .state import PlayerState, PlayerMode, create_tiles_from_tile_map
from .constants.tile import TILE_MAP


def main():
    pygame.init()

    display = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()

    renderer = Renderer(display)
    game_state = GameState(
        player=PlayerState(
            rect=pygame.Rect(0, 0, 32, 100),
            mode=PlayerMode.walking,
            lives=3,
            score=0,
            velocity=pygame.Vector2(0, 0),
            acceleration=pygame.Vector2(0, 0),
        ),
        tiles=create_tiles_from_tile_map(TILE_MAP),
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        renderer.render(game_state)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
