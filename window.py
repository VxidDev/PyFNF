import pygame

class Window:
    def __init__(self) -> None:
        self.width: int | None = None 
        self.height: int | None = None 
        self.name: str | None = None 

        self._window = None

    def init(self, width: int, height: int, name: str | None = None) -> None:
        self.width = width 
        self.height = height
        self.name = name

        self._window = pygame.display.set_mode((width, height))

        if name is not None:
            pygame.display.set_caption(name)

    def flip(self) -> None:
        pygame.display.flip()

    def draw_rect(self, color: tuple[int, int, int], rect: pygame.rect.Rect, width: int = 0, border_radius: int = 0) -> None:
        pygame.draw.rect(self._window, color, rect, width, border_radius)

    def blit(self, *args, **kwargs) -> None:
        self._window.blit(*args, **kwargs)

    def fill(self, *args, **kwargs) -> None:
        self._window.fill(*args, **kwargs)