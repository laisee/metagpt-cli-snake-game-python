import pygame
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

class Game:
    def __init__(self, screen_width: int = 800, screen_height: int = 600):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_over = False
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.screen_width, self.screen_height)
        self.scoreboard = ScoreBoard()

    def start_game(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)

            self.snake.move()
            if self.snake.head_position() == self.food.position:
                self.snake.grow()
                self.food.generate()
                self.scoreboard.update_score()

            if self.snake.check_collision(self.screen_width, self.screen_height):
                self.end_game()

            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.scoreboard.draw(self.screen)
            pygame.display.update()
            self.clock.tick(30)

    def handle_keydown(self, key):
        direction_map = {
            pygame.K_UP: 'UP',
            pygame.K_DOWN: 'DOWN',
            pygame.K_LEFT: 'LEFT',
            pygame.K_RIGHT: 'RIGHT'
        }
        if key in direction_map:
            self.snake.change_direction(direction_map[key])

    def end_game(self):
        self.game_over = True
        self.scoreboard.update_high_score()
        pygame.quit()
