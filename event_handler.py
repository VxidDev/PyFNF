import pygame 
from game import Game
from window import Window

class EventHandler:
    def __init__(self, game: Game, event_handlers: list[tuple[int, callable[pygame.event.Event, EventHandler]]] | None = None) -> None:
        self.event_handlers = event_handlers if event_handlers is not None else []
        self.running = False 
        self.game: Game = game
        self.fps: int = 60

        for handler in self.event_handlers:
            if len(handler) != 2:
                raise ValueError("Event handler must be in this form: list[tuple[int, callable[pygame.event.Event, EventHandler]]].")

    def start(self) -> None:
        self.running = True 

        clock = pygame.time.Clock()

        while self.running: 
            dt: float = clock.tick(self.fps) / 1000

            for event in pygame.event.get():
                self.process_event(event)

            self.game.update(dt, self)
            self.game.render()

            print(f"FPS: {clock.get_fps():.2f}")

        pygame.quit()

    def process_event(self, event) -> None:
        for handler in self.event_handlers:
            if handler[0] != event.type:
                continue

            handler[1](event, self)