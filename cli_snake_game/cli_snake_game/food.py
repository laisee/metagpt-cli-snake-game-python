import pygame
import random
from typing import Tuple

class Food:
    def __init__(self, screen_width: int, screen_height: int, block_size: int = 10):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.block_size = block_size
        self.position: Tuple[int, int] = (0, 0)
        self.generate()

    def generate(self):
        x = random.randint(0, self.screen_width - self.block_size)
        y = random.randint(0, self.screen_height - self.block_size)
        self.position = (x//self.block_size * self.block_size, y//self.block_size * self.block_size)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], self.block_size, self.block_size))
