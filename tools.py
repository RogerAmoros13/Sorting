from settings import *
import pygame
from random import randint

class Event():
    def __init__(self, header, set):
        self.isRunning = True
        self.shuffle = False
        self.go = False
        self.header = header
        self.set = set

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.set.shuffle = True
                if event.key == pygame.K_SPACE:
                    self.set.go = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in self.header.buttons:
                    if self.header.get_position(pos, button):
                        button.pressed = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                for button in self.header.buttons:
                    if button.pressed:
                        button.active = True
                    button.pressed = False

class Set:
    def __init__(self, n=100):
        self.n = n
        self.set = [{"pos": i, "state": "neutral"} for i in range(n)]
        print(self.set)
        self.shuffle = False
        self.shuffle_step = 0
        self.algorithm = False
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
        self.set[i], self.set[j] = self.set[j], self.set[i]
        self.draw_set()        

    def draw_set(self):
        for index, value in enumerate(self.set):
            pygame.draw.rect(self.screen, white, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
    
    def draw_algorithm(self, swap1, swap2 = None):
        for index, value in enumerate(self.set):
            if index == swap1 or index == swap2:
                pygame.draw.rect(self.screen, red, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
            else:
                pygame.draw.rect(self.screen, white, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])

    def draw_background(self):
        self.screen.fill(grey)
        pygame.draw.rect(self.screen, black, [0, HEADER, AMPLE, ALTURA-HEADER])

    def draw_check(self, pos, valid):
        for index, value in enumerate(self.set):
            pygame.draw.rect(self.screen, white, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
            if valid and pos == index:
                pygame.draw.rect(self.screen, green, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])
            if pos == index and not valid:
                pygame.draw.rect(self.screen, red, [self.offset + self.rect_amp * index, ALTURA - self.rect_alt * value, self.rect_amp, self.rect_alt * value + 1])



