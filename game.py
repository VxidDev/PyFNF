import pygame 
from window import Window
from assets import AssetHandler

from colors import BLUE, RED

class Game:
    def __init__(self, window: Window, asset_handler: AssetHandler) -> None:
        self.window: Window = window 
        self.asset_handler = asset_handler

        self.left_arr_pressed = False
        self.right_arr_pressed = False
        self.up_arr_pressed = False
        self.down_arr_pressed = False

        self.notes: list[tuple[int, pygame.rect.Rect]] = [
            #(0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 3800, 150, 150)), gf
            #(3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 4300, 150, 150)), gf
            #(0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 5000, 150, 150)), gf
            #(3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 5500, 150, 150)), gf

            (0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 6000, 150, 150)), 
            (3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 6600, 150, 150)), 
            (0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 7400, 150, 150)), 
            (3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 8000, 150, 150)),
        ]

        self.note_speed = 500

        self.asset_handler.tutorial_song.play()

    def update(self, dt: int, ev_handler: "EventHandler") -> None:
        notes: list[pygame.rect.Rect] = []

        for note in self.notes:
            note[1].y -= self.note_speed * dt

            if note[1].bottom < 0:
                continue 

            notes.append(note)


        self.notes = notes 

        if len(self.notes) == 0:
            ev_handler.running = False

    def render(self) -> None:
        self.window.blit(self.asset_handler.bg, (0, 0))

        self.window.blit(
            self.asset_handler.left_arr if not self.left_arr_pressed else self.asset_handler.left_arr_on, 
            self.asset_handler.left_arr_hitbox
        )

        # self.window.draw_rect(RED, self.asset_handler.left_arr_hitbox)

        self.window.blit(
            self.asset_handler.down_arr if not self.down_arr_pressed else self.asset_handler.down_arr_on, 
            self.asset_handler.down_arr_hitbox
        )

        # self.window.draw_rect(RED, self.asset_handler.down_arr_hitbox)

        self.window.blit(
            self.asset_handler.up_arr if not self.up_arr_pressed else self.asset_handler.up_arr_on, 
            self.asset_handler.up_arr_hitbox
        )

        # self.window.draw_rect(RED, self.asset_handler.up_arr_hitbox)

        self.window.blit(
            self.asset_handler.right_arr if not self.right_arr_pressed else self.asset_handler.right_arr_on, 
            self.asset_handler.right_arr_hitbox
        )

        # self.window.draw_rect(RED, self.asset_handler.right_arr_hitbox)

        for note in self.notes:
            self.window.draw_rect(BLUE, note[1])
            print(f"NOTE COORDINATES: x: {note[1].x} y: {note[1].y}")

        self.window.flip()