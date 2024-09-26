import pygame

from .render.renderer import Renderer
from .state.game_state import GameState
from .state.tile import GrassTileState
from .state.player import PlayerState, PlayerMode


def main():
    pygame.init()

    display = pygame.display.set_mode((800, 600))
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
        tiles=[
            GrassTileState(rect=pygame.Rect(0, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(32, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(64, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(96, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(128, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(160, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(192, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(224, 20, 32, 32)),
            GrassTileState(rect=pygame.Rect(256, 20, 32, 32)),
        ],
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
