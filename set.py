from settings import *
from sort.exchanging import *
import pygame
from random import randint

class Set:
    def __init__(self, n=100):
        self.n = n
        self.set = [SetElement(i) for i in range(n)]
        self.shuffle = False
        self.shuffle_step = 0
        self.algorithm = Bubble()
        self.go = False

        self.screen = pygame.display.get_surface()
        self.rect_amp = AMPLE // self.n
        self.offset = (AMPLE - self.n * self.rect_amp) // 2
        self.rect_alt = (ALTURA - HEADER) / self.n

    def update(self):
        if self.shuffle:
            if self.shuffle_step < self.n - 1:
                self.action_shuffle(self.shuffle_step)
                self.shuffle_step += 1
            else:
                self.shuffle_step = 0
                self.shuffle = False
        if self.go:
            pass
        self.draw_background()
        self.draw_set()

    def action_shuffle(self, i):
        j = randint(i + 1, self.n - 1)
        self.set[i].height, self.set[j].height = self.set[j].height, self.set[i].height

    def draw_set(self):
        for element in self.set:
            pygame.draw.rect(
                self.screen,
                element.color,
                [
                    self.offset + self.rect_amp * element.pos, 
                    ALTURA - self.rect_alt * element.height, 
                    self.rect_amp, 
                    self.rect_alt * element.height + 1
                ]
            )

    def draw_background(self):
        self.screen.fill(grey)
        pygame.draw.rect(self.screen, black, [0, HEADER, AMPLE, ALTURA-HEADER])


class SetElement:
    def __init__(self, i):
        self.pos = i
        self.height = i
        self.state = "neutral"
        self.color = white


