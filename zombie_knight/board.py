import pygame

from .render.renderer import Renderer
from .state import (
    GameState,
    PlayerState,
    PlayerMode,
    HorizontalDirection,
    create_tiles_from_tile_map,
)
from .rules.physics.movement import (
    GravityRule,
    AccelerationRule,
    VelocityRule,
)
from .constants.tile import TILE_MAP


def main():
    pygame.init()

    display = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()

    renderer = Renderer(display)
    game_state = GameState(
        player=PlayerState(
            rect=pygame.Rect(0, 0, 32, 100),
            mode=PlayerMode.IDLE,
            horizontal_direction=HorizontalDirection.RIGHT,
            animation_index=0,
            lives=3,
            score=0,
            velocity=pygame.Vector2(0, 0),
            acceleration=pygame.Vector2(0, 0),
        ),
        tiles=create_tiles_from_tile_map(TILE_MAP),
    )

    rules = [
        GravityRule(),
        AccelerationRule(),
        VelocityRule(),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        renderer.render(game_state)
        pygame.display.update()

        game_state = apply_rules(game_state, rules)

        clock.tick(60)


def apply_rules(
    game_state: GameState,
    rules: list,
) -> GameState:
    for rule in rules:
        game_state = rule(game_state)
    return game_state


if __name__ == "__main__":
    main()
