import pygame

from window import Window

pygame.mixer.init()

class AssetHandler:
    def __init__(self, window: Window) -> None:
        self.window = window

        self.bg_raw: pygame.Surface = pygame.image.load("bg.png").convert()
        self.bg = pygame.transform.scale(self.bg_raw, (self.window.width, self.window.height)) 

        self.down_arr: pygame.Surface = pygame.image.load("images/down-arr.png").convert_alpha()
        self.down_arr_hitbox: pygame.rect.Rect = self.down_arr.get_rect(center=(self.window.width // 2 - 100, self.window.height - 935))

        self.left_arr: pygame.Surface = pygame.image.load("images/left-arr.png").convert_alpha()
        self.left_arr_hitbox: pygame.rect.Rect = self.left_arr.get_rect(center=(self.window.width // 2 - 300, self.window.height - 935))

        self.right_arr: pygame.Surface = pygame.image.load("images/right-arr.png").convert_alpha()
        self.right_arr_hitbox: pygame.rect.Rect = self.right_arr.get_rect(center=(self.window.width // 2 + 300, self.window.height - 935))

        self.up_arr: pygame.Surface = pygame.image.load("images/up-arr.png").convert_alpha()
        self.up_arr_hitbox: pygame.rect.Rect = self.up_arr.get_rect(center=(self.window.width // 2 + 100, self.window.height - 935))

        self.down_arr_on: pygame.Surface = pygame.image.load("images/down-arr-on.png").convert_alpha()
        self.down_arr_on: pygame.Surface = pygame.transform.scale(self.down_arr_on, (150, 150))

        self.left_arr_on: pygame.Surface = pygame.image.load("images/left-arr-on.png").convert_alpha()
        self.left_arr_on: pygame.Surface = pygame.transform.scale(self.left_arr_on, (150, 150))

        self.right_arr_on: pygame.Surface = pygame.image.load("images/right-arr-on.png").convert_alpha()
        self.right_arr_on: pygame.Surface = pygame.transform.scale(self.right_arr_on, (150, 150))

        self.up_arr_on: pygame.Surface = pygame.image.load("images/up-arr-on.png").convert_alpha()
        self.up_arr_on: pygame.Surface = pygame.transform.scale(self.up_arr_on, (150, 150))

        self.tutorial_song: pygame.mixer.Sound = pygame.mixer.Sound("tutorial.mp3")