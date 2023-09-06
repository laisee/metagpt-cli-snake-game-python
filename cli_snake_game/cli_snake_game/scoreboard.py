## scoreboard.py
import pygame

class ScoreBoard:
    def __init__(self, font_size: int = 32):
        self.score: int = 0
        self.high_score: int = 0
        self.font = pygame.font.Font(None, font_size)

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.update_high_score()

    def update_high_score(self):
        self.high_score = self.score

    def reset_score(self):
        self.score = 0

    def draw(self, surface):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, (255, 255, 255))
        surface.blit(score_text, (10, 10))
        surface.blit(high_score_text, (10, 40))
