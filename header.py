import pygame
from settings import *


class Header:
    def __init__(self):
        self.screen = pygame.display.get_surface()
    
    def change_algorithm_button(self):
        button = Button('Cambiar Algoritmo', [20, 20, 300, 55], 35, offset = [5, 5])
        button.show(False)
    
    def manager(self):
        self.change_algorithm_button()




class Button:
    def __init__(self, text, button_list, size_text, color1 = white_dirty, color2 = blue, border_radius = 10, offset = [0,0]):
        self.screen = pygame.display.get_surface()
        self.text = text
        self.button_list = button_list
        self.size_text = size_text
        self.color1 = color1
        self.color2 = color2
        self.border_radius = border_radius
        self.offset = offset

    def show(self, pressed):
        font = pygame.font.SysFont('Arial', self.size_text)
        code = font.render(self.text, True, black)
        if pressed:
            pygame.draw.rect(self.screen, self.color2, self.button_list, )
        else:
            pygame.draw.rect(self.screen, self.color1, self.button_list, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, black, self.button_list, border_radius=self.border_radius, width=2)
        text_posx, text_posy = self.button_list[0] + self.offset[0], self.button_list[1] + self.offset[1]
        self.screen.blit(code, (text_posx, text_posy))
