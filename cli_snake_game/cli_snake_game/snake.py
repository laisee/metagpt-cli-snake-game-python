import pygame
from typing import List, Tuple

class Snake:
    def __init__(self):
        self.body: List[Tuple[int, int]] = [(50, 50), (40, 50), (30, 50)]
        self.direction: str = 'RIGHT'
        self.block_size: int = 10

    def head_position(self) -> Tuple[int, int]:
        return self.body[0]

    def move(self):
        x, y = self.head_position()
        if self.direction == 'UP':
            y -= self.block_size
        elif self.direction == 'DOWN':
            y += self.block_size
        elif self.direction == 'LEFT':
            x -= self.block_size
        elif self.direction == 'RIGHT':
            x += self.block_size
        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        self.body.append((0, 0))

    def change_direction(self, direction: str):
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != opposite_directions[self.direction]:
            self.direction = direction

    def check_collision(self, screen_width: int, screen_height: int) -> bool:
        x, y = self.head_position()
        return x < 0 or y < 0 or x >= screen_width or y >= screen_height or (x, y) in self.body[1:]

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, (255, 255, 255), (x, y, self.block_size, self.block_size))
