import pygame

from event_handler import EventHandler
from window import Window
from game import Game
from assets import AssetHandler
from input_handler import InputHandler

def close_window(ev: pygame.event.Event, ev_handler: EventHandler) -> None:
    ev_handler.running = False

def main() -> None:
    window: Window = Window()
    window.init(1920, 1080, "PyFNF")

    print(f"DRIVER: {pygame.display.get_driver()}")

    asset_handler: AssetHandler = AssetHandler(window)
    input_handler: InputHandler = InputHandler()

    game: Game = Game(window, asset_handler)

    event_handler: EventHandler = EventHandler(
        game,
        [
            (pygame.QUIT, close_window),
            (pygame.KEYDOWN, input_handler.keydown),
            (pygame.KEYUP, input_handler.keyup)
        ]
    )

    event_handler.start()

main()