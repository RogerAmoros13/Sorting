from settings import *
import pygame
from random import randint

class Event():
    def __init__(self, header, set):
        self.isRunning = True
        self.shuffle = False
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
        self.header.manager()
