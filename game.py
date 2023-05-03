import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

pygame.init()
font = pygame.font.Font('arial.ttf', 25)


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple('Point', 'x, y')

# RGB - Värit
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)
BROWN = (165, 42, 42)

BLOCK_SIZE = 20
ENEMY_BLOCK_SIZE = 40

# Pelin nopeus
SPEED = 100


class MatopeliAI:

    # Canvas
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Matopeli')
        self.clock = pygame.time.Clock()
        self.reset()

    # Pelin aloitus(tila)
    def reset(self):
        self.direction = Direction.RIGHT

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head,
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.redScore = 0
        self.greenScore = 0
        self.food = None
        self.food2 = None
        self.enemy = None
        self._place_food()
        self._place_food2()
        self._place_enemy()
        self.frame_iteration = 0

    # Punaisen omenan lisäys
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x, y)

        if self.food in self.snake or self.food == self.food2:
            self._place_food()

    # Vihreän omenan lisäys
    def _place_food2(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food2 = Point(x, y)

        if self.food2 in self.snake or self.food2 == self.food:
            self._place_food2()

    # Vihollispalikan lisäys
    def _place_enemy(self):
        x1 = random.randint(0, (self.w-ENEMY_BLOCK_SIZE) //
                            ENEMY_BLOCK_SIZE)*ENEMY_BLOCK_SIZE
        y1 = random.randint(0, (self.w-ENEMY_BLOCK_SIZE) //
                            ENEMY_BLOCK_SIZE)*ENEMY_BLOCK_SIZE
        self.enemy = Point(x1, y1)

        x2 = random.randint(0, (self.w-ENEMY_BLOCK_SIZE) //
                            ENEMY_BLOCK_SIZE)*ENEMY_BLOCK_SIZE
        y2 = random.randint(0, (self.w-ENEMY_BLOCK_SIZE) //
                            ENEMY_BLOCK_SIZE)*ENEMY_BLOCK_SIZE
        self.enemy2 = Point(x2, y2)

        if self.enemy in self.snake or self.enemy == self.food or self.enemy == self.food2 or self.enemy == self.enemy2:
            self._place_enemy()

    def play_step(self, action):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 1. Liikkuminen
        self._move(action)
        self.snake.insert(0, self.head)

        # 2. Tarkista onko peli päättynyt
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score, self.redScore, self.greenScore

        # 3. Omenoiden keräys
        if self.head == self.food:
            self.score += 1
            self.redScore += 1
            reward = 10
            self._place_food()
        elif self.head == self.food2:
            self.score += 1
            self.greenScore += 1
            reward = 10
            self._place_food2()
        else:
            self.snake.pop()

        self._update_ui()
        self.clock.tick(SPEED)
        # 4. Pelin päättyminen
        return reward, game_over, self.score, self.redScore, self.greenScore

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # Törmäys vihollisen kanssa
        if (pt == self.enemy) or (pt == self.enemy2):
            return True
        # Osuu itseensä
        if pt in self.snake[1:]:
            return True

        return False

    # Pelin grafiikat
    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            # Käärme
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(
                pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2,
                             pygame.Rect(pt.x+4, pt.y+4, 12, 12))

            # Omenat
            pygame.draw.rect(self.display, RED, pygame.Rect(
                self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, GREEN, pygame.Rect(
                self.food2.x, self.food2.y, BLOCK_SIZE, BLOCK_SIZE))

            # Vihollispalikat
            pygame.draw.rect(self.display, BROWN, pygame.Rect(
                self.enemy.x, self.enemy.y, ENEMY_BLOCK_SIZE, ENEMY_BLOCK_SIZE))
            pygame.draw.rect(self.display, BROWN, pygame.Rect(
                self.enemy2.x, self.enemy2.y, ENEMY_BLOCK_SIZE, ENEMY_BLOCK_SIZE))

        text = font.render("Score: " + str(self.score) + " Reds: " +
                           str(self.redScore) + " Greens: " + str(self.greenScore), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, action):
        # [suoraan, oikea, vasen]

        clock_wise = [Direction.RIGHT, Direction.DOWN,
                      Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]  # Ei muutosta
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]  # Käännös oikeaan
        else:  # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]  # Käännös vasempaan

        self.direction = new_dir

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
            if x >= self.w:
                x = 0
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
            if x < 0:
                x = self.w - BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
            if y >= self.h:
                y = 0
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
            if y < 0:
                y = self.h - BLOCK_SIZE

        self.head = Point(x, y)
