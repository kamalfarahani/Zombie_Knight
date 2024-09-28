import pygame

from ..state.player import PlayerState, PlayerMode
from ..state.direction import HorizontalDirection
from ..constants.paths import (
    PLAYER_ATTACK_IMAGE_PATHS,
    PLAYER_IDLE_IMAGE_PATHS,
    PLAYER_JUMP_IMAGE_PATHS,
    PLAYER_RUN_IMAGE_PATHS,
)


player_mode_to_images = {
    PlayerMode.ATTACKING: PLAYER_ATTACK_IMAGE_PATHS,
    PlayerMode.IDLE: PLAYER_IDLE_IMAGE_PATHS,
    PlayerMode.JUMPING: PLAYER_JUMP_IMAGE_PATHS,
    PlayerMode.RUNNING: PLAYER_RUN_IMAGE_PATHS,
}


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        player_state: PlayerState,
    ) -> None:
        """
        Initializes the player.

        Args:
            player_state (PlayerState): The state of the player.

        Returns:
            None
        """
        super().__init__()

        self.rect = player_state.rect
        self.image = self.load_image(
            player_state.mode,
            player_state.horizontal_direction,
            player_state.animation_index,
            self.rect.width,
            self.rect.height,
        )

    def load_image(
        self,
        player_mode: PlayerMode,
        horizontal_direction: HorizontalDirection,
        animation_index: int,
        width: int,
        height: int,
    ) -> pygame.Surface:
        """
        Loads the image of the player.

        Args:
            player_mode (PlayerMode): The mode of the player.
            animation_index (int): The index of the animation.
            width (int): The width of the image.
            height (int): The height of the image.

        Returns:
            pygame.Surface: The image of the player.
        """
        image_path = player_mode_to_images[player_mode][animation_index]
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (width, height))

        if horizontal_direction == HorizontalDirection.LEFT:
            image = pygame.transform.flip(image, True, False)

        return image
