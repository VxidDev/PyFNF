import pygame

from window import Window

pygame.mixer.init()
pygame.font.init()

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

        self.left_arr_target: pygame.Surface = pygame.image.load("images/left-arr-target.png").convert_alpha()
        self.left_arr_target = pygame.transform.scale(self.left_arr_target, (150, 150))
        self.left_arr_target.set_colorkey((0, 0, 0))

        self.down_arr_target: pygame.Surface = pygame.image.load("images/down-arr-target.png").convert_alpha()
        self.down_arr_target = pygame.transform.scale(self.down_arr_target, (150, 150))
        self.down_arr_target.set_colorkey((0, 0, 0))

        self.up_arr_target: pygame.Surface = pygame.image.load("images/up-arr-target.png").convert_alpha()
        self.up_arr_target = pygame.transform.scale(self.up_arr_target, (150, 150))
        self.up_arr_target.set_colorkey((0, 0, 0))

        self.right_arr_target: pygame.Surface = pygame.image.load("images/right-arr-target.png").convert_alpha()
        self.right_arr_target = pygame.transform.scale(self.right_arr_target, (150, 150))
        self.right_arr_target.set_colorkey((0, 0, 0))

        self.tutorial_song: pygame.mixer.Sound = pygame.mixer.Sound("sounds/tutorial.mp3")
        self.main_menu_song: pygame.mixer.Sound = pygame.mixer.Sound("sounds/main-menu.mp3")

        self.big_font: pygame.font.Font = pygame.font.Font("fonts/big-font.ttf", size=90)
        self.giant_font: pygame.font.Font = pygame.font.Font("fonts/big-font.ttf", size=125)

        self.press_enter_text = self.giant_font.render("Press Enter to Begin", True, (0, 255, 255))

        self.intro_messages: list = [
            (2000, self.big_font.render("Inspired by Friday Night Funkin'", True, (255, 255, 255)), (-300, -50)),
            (0, self.big_font.render("Made in PyGame", True, (255, 255, 255)), (100, -50)),
            (2000, self.big_font.render("Welcome to PyFNF!", True, (255, 255, 255)), (80, -50))
        ]

        self.gf_main_menu_sprites: list = []

        for i in range(0, 20):
            img: pygame.Surface = pygame.image.load(f"images/gf-main-menu-anim/{i + 1}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5))

            self.gf_main_menu_sprites.append(img)

        self.logo_main_menu_sprites: list = []

        for i in range(0, 4):
            img: pygame.Surface = pygame.image.load(f"images/logo-main-menu-anim/{i + 1}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width() * 1.45, img.get_height() * 1.45))

            self.logo_main_menu_sprites.append(img)
