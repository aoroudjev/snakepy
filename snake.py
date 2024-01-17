from typing import Tuple

import pygame


class Snake:
    def __init__(self, position: tuple):
        self.snake_list = [position]  # position format: (x, y)
        self.direction = "down"

    def __len__(self):
        return len(self.snake_list)

    def update(self):
        head_x, head_y = self.snake_list[-1]
        if self.direction == "down":
            self.snake_list.append((head_x, head_y))
            self.snake_list.pop(-1)

    def grow(self):
        pass

    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction
