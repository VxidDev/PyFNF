import pygame


class AnimatedSprite:
    def __init__(self, frame_layers: list[list[pygame.Surface]], fps: int) -> None:
        self.dt_accumulator: float = 0.0
        self.fps: int = fps
        self.frame_interval: float = 1.0 / self.fps

        self.curr_frame: int = 0

        self.frame_layers = frame_layers
        self.len_frames = len(frame_layers[0])

        self.playing: bool = True
        self.loop: bool = True

    def update(self, dt: float) -> None:
        if not self.playing:
            return

        self.dt_accumulator += dt

        while self.dt_accumulator >= self.frame_interval:
            self.dt_accumulator -= self.frame_interval
            self.curr_frame += 1

            if self.curr_frame >= self.len_frames:
                if self.loop:
                    self.curr_frame = 0
                else:
                    self.curr_frame = self.len_frames - 1
                    self.playing = False
                    break

    def reset(self) -> None:
        self.curr_frame = 0
        self.dt_accumulator = 0.0
        self.playing = True

    def set_loop(self, value: bool) -> None:
        self.loop = value

    def set_playing(self, value: bool) -> None:
        self.playing = value

    def get_curr_frames(self) -> list[pygame.Surface]:
        return [
            layer[self.curr_frame]
            for layer in self.frame_layers
        ]

    def get_curr_frame(self) -> pygame.Surface:
        return self.frame_layers[0][self.curr_frame]