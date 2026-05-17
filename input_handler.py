import pygame

class InputHandler:
    def __init__(self) -> None:
        self.keymap = {
            pygame.KEYDOWN: {},
            pygame.KEYUP: {}
        }

        self.keymap[pygame.KEYDOWN] = {
            pygame.K_d: self.d_keydown,
            pygame.K_f: self.f_keydown,
            pygame.K_j: self.j_keydown,
            pygame.K_k: self.k_keydown,
            pygame.K_EQUALS: self.equals_keydown,
            pygame.K_MINUS: self.minus_keydown,
            pygame.K_RETURN: self.enter_keydown,
            pygame.K_UP: self.up_keydown,
            pygame.K_DOWN: self.down_keydown
        }

        self.keymap[pygame.KEYUP] = {
            pygame.K_d: self.d_keyup,
            pygame.K_f: self.f_keyup,
            pygame.K_j: self.j_keyup,
            pygame.K_k: self.k_keyup,
        }

    def keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        handler = self.keymap[pygame.KEYDOWN].get(ev.key)
        
        if handler is not None:
            handler(ev, ev_handler)

    def keyup(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        handler = self.keymap[pygame.KEYUP].get(ev.key)
        
        if handler is not None:
            handler(ev, ev_handler)

    def d_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.left_arr_pressed = True

        notes = ev_handler.game.notes
        hit_y = ev_handler.game.asset_handler.left_arr_hitbox.centery

        new_notes = []

        for note in notes:
            if abs(note[1].centery - hit_y) < 100 and note[0] == 0:
                print("EVENT: Note hit!")
                ev_handler.game.hp = min(ev_handler.game.hp + ev_handler.game.hp_step, 100)
                continue

            new_notes.append(note)

        ev_handler.game.notes = new_notes 

    def d_keyup(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.left_arr_pressed = False

    def f_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.down_arr_pressed = True

        notes = ev_handler.game.notes
        hit_y = ev_handler.game.asset_handler.up_arr_hitbox.centery

        new_notes = []

        for note in notes:
            if abs(note[1].centery - hit_y) < 100 and note[0] == 1:
                print("EVENT: Note hit!")
                ev_handler.game.hp = min(ev_handler.game.hp + ev_handler.game.hp_step, 100)
                continue

            new_notes.append(note)

        ev_handler.game.notes = new_notes 

    def f_keyup(self, ev: pygame.event.Eventt, ev_handler: EventHandler) -> None:
        ev_handler.game.down_arr_pressed = False

    def j_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.up_arr_pressed = True

        notes = ev_handler.game.notes
        hit_y = ev_handler.game.asset_handler.up_arr_hitbox.centery

        new_notes = []

        for note in notes:
            if abs(note[1].centery - hit_y) < 100 and note[0] == 2:
                print("EVENT: Note hit!")
                ev_handler.game.hp = min(ev_handler.game.hp + ev_handler.game.hp_step, 100)
                continue

            new_notes.append(note)

        ev_handler.game.notes = new_notes 

    def j_keyup(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.up_arr_pressed = False

    def k_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.right_arr_pressed = True

        notes = ev_handler.game.notes
        hit_y = ev_handler.game.asset_handler.right_arr_hitbox.centery

        new_notes = []

        for note in notes:
            if abs(note[1].centery - hit_y) < 100 and note[0] == 3:
                print("EVENT: Note hit!")
                ev_handler.game.hp = min(ev_handler.game.hp + ev_handler.game.hp_step, 100)
                continue

            new_notes.append(note)

        ev_handler.game.notes = new_notes 

    def k_keyup(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.game.right_arr_pressed = False

    def equals_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        ev_handler.fps += 5

    def minus_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        if ev_handler.fps <= 5:
            return

        ev_handler.fps -= 5

    def enter_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        if ev_handler.game.state == "waiting" and ev_handler.game.s_channel_1 is None:
            ev_handler.game.s_channel_1 = ev_handler.game.asset_handler.notif_sound.play()

        if ev_handler.game.state == "menu" and ev_handler.game.s_channel_1 is None:
            ev_handler.game.s_channel_1 = ev_handler.game.asset_handler.notif_sound.play()

            if ev_handler.game.main_menu_choice == 0:
                ev_handler.game.main_menu_can_switch = False
                ev_handler.game.story_mode_main_menu_clicked = True
            else:
                ev_handler.game.main_menu_can_switch = False
                ev_handler.game.freeplay_main_menu_clicked = True

        if ev_handler.game.state == "intro":
            ev_handler.game.state = "waiting"

    def up_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        if ev_handler.game.state == "menu" and ev_handler.game.main_menu_can_switch:
            if ev_handler.game.main_menu_choice <= 0:
                ev_handler.game.main_menu_choice = ev_handler.game.main_menu_last_possible_choice
            else:
                ev_handler.game.main_menu_choice -= 1

    def down_keydown(self, ev: pygame.event.Event, ev_handler: EventHandler) -> None:
        if ev_handler.game.state == "menu" and ev_handler.game.main_menu_can_switch:
            if ev_handler.game.main_menu_choice >= ev_handler.game.main_menu_last_possible_choice:
                ev_handler.game.main_menu_choice = 0
            else:
                ev_handler.game.main_menu_choice += 1