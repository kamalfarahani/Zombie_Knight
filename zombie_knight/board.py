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
from .rules.tile import CollideTileRule
from .rules.player import PlayerMoveRule, PlayerJumpRule
from .constants.tile import TILE_MAP
from .constants.player import HORIZONTAL_ACCELERATION, HORIZONTAL_FRICTION


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
        PlayerMoveRule(
            horizontal_acceleration=HORIZONTAL_ACCELERATION,
            horizontal_friction=HORIZONTAL_FRICTION,
        ),
        PlayerJumpRule(jump_velocity=10),
        CollideTileRule(),
    ]

    while True:
        events = list(pygame.event.get())
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        renderer.render(game_state)
        pygame.display.update()

        game_state = apply_rules(game_state, rules, events)

        clock.tick(40)


def apply_rules(
    game_state: GameState,
    rules: list,
    events: list[pygame.event.Event],
) -> GameState:
    for rule in rules:
        game_state = rule(game_state, events)
    return game_state


if __name__ == "__main__":
    main()
