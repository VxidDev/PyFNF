import pygame 
from window import Window
from assets import AssetHandler
from hp_bar import HpBar

import math

from colors import BLUE, RED, PURPLE

def lerp(a, b, t):
    return a + (b - a) * t

class Game:
    def __init__(self, window: Window, asset_handler: AssetHandler) -> None:
        self.window = window 
        self.asset_handler = asset_handler

        self.state = "menu"

        self.left_arr_pressed = False
        self.right_arr_pressed = False
        self.up_arr_pressed = False
        self.down_arr_pressed = False

        self.hp = 50
        self.hp_step = 5
        self.bar = HpBar(self.hp, self.window)

        self.notes: list[tuple[int, pygame.rect.Rect]] = [
            #(0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 1000, 150, 150)), test 
            #(1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 1500, 150, 150)), test
            #(2, pygame.rect.Rect(self.window.width // 2, self.window.height + 2000, 150, 150)),       test
            #(3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 2500, 150, 150)), test

            #(0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 3800, 150, 150)), gf
            #(3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 4300, 150, 150)), gf
            #(0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 5000, 150, 150)), gf
            #(3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 5500, 150, 150)), gf

            (0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 6000, 150, 150)), 
            (3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 6600, 150, 150)), 
            (0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 7400, 150, 150)), 
            (3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 8000, 150, 150)),

            (2, pygame.rect.Rect(self.window.width // 2, self.window.height + 11000, 150, 150)), 
            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 11600, 150, 150)), 
            (2, pygame.rect.Rect(self.window.width // 2, self.window.height + 12000, 150, 150)), 
            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 12700, 150, 150)),

            (0, pygame.rect.Rect(self.window.width // 2 - 400, self.window.height + 15500, 150, 150)),
            (2, pygame.rect.Rect(self.window.width // 2, self.window.height + 16250, 150, 150)),
            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 17000, 150, 150)),
            (3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 17500, 150, 150)),

            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 20500, 150, 150)),
            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 20750, 150, 150)),
            (2, pygame.rect.Rect(self.window.width // 2, self.window.height + 21000, 150, 150)),
            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 21500, 150, 150)),
            (1, pygame.rect.Rect(self.window.width // 2 - 200, self.window.height + 21750, 150, 150)),
            (3, pygame.rect.Rect(self.window.width // 2 + 200, self.window.height + 22000, 150, 150)),
        ]
        self.note_speed = 500

        self.asset_handler.main_menu_song.play()

        self.current_message = 0

        self.menu_phase = "wait_before"
        self.phase_start = pygame.time.get_ticks()

        self.show_time = 500 

        self.gf_main_menu_anim_curr_frame: int = 0
        self.gf_main_menu_frame_accumulator = 0.0
        self.gf_main_menu_fps: int = 18
        self.gf_main_menu_frame_interval: int = 1.0 / self.gf_main_menu_fps

        self.logo_main_menu_anim_curr_frame: int = 0
        self.logo_main_menu_frame_accumulator = 0.0
        self.logo_main_menu_fps: int = 6
        self.logo_main_menu_frame_interval: int = 1.0 / self.logo_main_menu_fps

        self.t = 0.0
        self.speed = 1.0

    def update(self, dt: int, ev_handler: "EventHandler") -> None:
        if self.state == "game":
            notes: list[tuple[int, pygame.Rect]] = []

            for lane, rect in self.notes:
                rect.y -= self.note_speed * dt

                if rect.bottom < 0:
                    self.hp = max(0, self.hp - self.hp_step)
                    continue

                notes.append((lane, rect))

            self.notes = notes

            if len(self.notes) == 0 or self.hp <= 0:
                ev_handler.running = False

            self.bar.update(self.hp)

        elif self.state == "menu":
            current_ticks = pygame.time.get_ticks()
            elapsed = current_ticks - self.phase_start

            delay = self.asset_handler.intro_messages[self.current_message][0]

            if self.menu_phase == "wait_before":
                if elapsed >= delay:
                    self.menu_phase = "show"
                    self.phase_start = current_ticks

            elif self.menu_phase == "show":
                if elapsed >= self.show_time:
                    self.menu_phase = "wait_after"
                    self.phase_start = current_ticks

            elif self.menu_phase == "wait_after":
                if elapsed >= delay:
                    self.current_message += 1

                    if self.current_message >= len(self.asset_handler.intro_messages):
                        self.state = "waiting"
                        
                    else:
                        self.menu_phase = "wait_before"
                        self.phase_start = current_ticks

        elif self.state == "waiting":
            self.gf_main_menu_frame_accumulator += dt
            self.logo_main_menu_frame_accumulator += dt

            if self.gf_main_menu_anim_curr_frame >= 19:
                self.gf_main_menu_anim_curr_frame = 0

            if self.logo_main_menu_anim_curr_frame >= 3:
                self.logo_main_menu_anim_curr_frame = 0

            if self.gf_main_menu_frame_accumulator >= self.gf_main_menu_frame_interval:
                self.gf_main_menu_frame_accumulator -= self.gf_main_menu_frame_interval
                self.gf_main_menu_anim_curr_frame += 1

            if self.logo_main_menu_frame_accumulator >= self.logo_main_menu_frame_interval:
                self.logo_main_menu_frame_accumulator -= self.logo_main_menu_frame_interval
                self.logo_main_menu_anim_curr_frame += 1

            self.t = (math.sin(pygame.time.get_ticks() * 0.0015) + 1) / 2

            r = int(lerp(BLUE[0], PURPLE[0], self.t))
            g = int(lerp(BLUE[1], PURPLE[1], self.t))
            b = int(lerp(BLUE[2], PURPLE[2], self.t))

            color = (r, g, b)

            self.asset_handler.press_enter_text = self.asset_handler.giant_font.render("Press Enter to Begin", True, color)

    def render(self) -> None:
        if self.state == "game":
            self.window.blit(self.asset_handler.bg, (0, 0))

            self.window.blit(
                self.asset_handler.left_arr if not self.left_arr_pressed else self.asset_handler.left_arr_on,
                self.asset_handler.left_arr_hitbox
            )

            self.window.blit(
                self.asset_handler.down_arr if not self.down_arr_pressed else self.asset_handler.down_arr_on,
                self.asset_handler.down_arr_hitbox
            )

            self.window.blit(
                self.asset_handler.up_arr if not self.up_arr_pressed else self.asset_handler.up_arr_on,
                self.asset_handler.up_arr_hitbox
            )

            self.window.blit(
                self.asset_handler.right_arr if not self.right_arr_pressed else self.asset_handler.right_arr_on,
                self.asset_handler.right_arr_hitbox
            )

            self.bar.draw()

            for lane, rect in self.notes:
                if lane == 0:
                    self.window.blit(self.asset_handler.left_arr_target, (rect.x + 25, rect.y))
                elif lane == 1:
                    self.window.blit(self.asset_handler.down_arr_target, (rect.x + 25, rect.y))
                elif lane == 2:
                    self.window.blit(self.asset_handler.up_arr_target, (rect.x + 25, rect.y))
                elif lane == 3:
                    self.window.blit(self.asset_handler.right_arr_target, (rect.x + 25, rect.y))
                else:
                    self.window.draw_rect(BLUE, rect)

        elif self.state == "menu":
            self.window.fill((0, 0, 0))

            if self.menu_phase == "show":
                message: tuple[int, pygame.Surface, tuple[int, int]] = self.asset_handler.intro_messages[self.current_message]
                
                self.window.blit(
                    message[1],
                    (self.window.width // 2 - 500 + message[2][0], self.window.height // 2 + message[2][1])
                )

        elif self.state == "waiting":
            self.window.fill((0, 0, 0))

            self.window.blit(
                self.asset_handler.gf_main_menu_sprites[self.gf_main_menu_anim_curr_frame],
                (self.window.width - 1180, self.window.height - 980)
            )

            self.window.blit(
                self.asset_handler.logo_main_menu_sprites[self.logo_main_menu_anim_curr_frame],
                (-50 , 0)
            )

            self.window.blit(
                self.asset_handler.press_enter_text,
                (self.window.width // 2 - 800, self.window.height - 200)
            )

        self.window.flip()