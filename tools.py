from header import Header
from settings import *
import pygame
from random import randint

class Event():
    def __init__(self, header):
        self.isRunning = True
        self.shuffle = False
        self.go = False
        self.header = header

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.shuffle_step = 0
                    self.shuffle = True
                if event.key == pygame.K_SPACE:
                    self.go = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.header.get_position(pos, self.header.button1):
                    self.header.button1_bool = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                self.header.button1_bool = False

class Set:
    def __init__(self, n = 100):
        self.set = [i + 1 for i in range(n)]
        self.n = n
    
    def shuffle(self, i):
        j = randint(i + 1, self.n - 1)
        self.set[i], self.set[j] = self.set[j], self.set[i]


class Draw:
    def __init__(self, n):
        self.screen = pygame.display.get_surface()
        self.n = n
        self.rect_amp = AMPLE // self.n
        self.offset = (AMPLE - self.n * self.rect_amp) // 2
        self.rect_alt = (ALTURA - HEADER) / self.n

    def draw_set(self, set):
        for index, value in enumerate(set):
            pygame.draw.rect(self.screen, white, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
    
    def draw_algorithm(self, set, swap1, swap2 = None):
        for index, value in enumerate(set):
            if index == swap1 or index == swap2:
                pygame.draw.rect(self.screen, red, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
            else:
                pygame.draw.rect(self.screen, white, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])

    def draw_background(self):
        self.screen.fill(grey)
        pygame.draw.rect(self.screen, black, [0, HEADER, AMPLE, ALTURA-HEADER])

    def draw_check(self, set, pos, valid):
        for index, value in enumerate(set):
            pygame.draw.rect(self.screen, white, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
            if valid and pos == index:
                pygame.draw.rect(self.screen, green, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
            if pos == index and not valid:
                pygame.draw.rect(self.screen, red, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])



