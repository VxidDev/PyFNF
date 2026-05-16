import pygame 

from window import Window
from colors import RED, BLUE

class HpBar:
    def __init__(self, hp: int, window: Window) -> None:
        self.window = window
        self.hp = hp

        self.enemy_hp_bar = pygame.rect.Rect(self.window.width // 2 - 400, self.window.height - 200, 8 * self.hp, 50)
        self.player_hp_bar = pygame.rect.Rect(self.window.width // 2 - 400, self.window.height - 200, 800, 50)

    def draw(self) -> None:
        self.window.draw_rect(BLUE, self.player_hp_bar)
        self.window.draw_rect(RED, self.enemy_hp_bar)

    def update(self, hp: int) -> None:
        self.hp = hp
        self.enemy_hp_bar.width = (800 - 8 * self.hp)