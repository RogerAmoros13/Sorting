import pygame
from settings import *

"""
Button1: Cambio de algoritmo
"""


class Header:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.buttons = []
        self.button1 =  Button('Cambiar Algoritmo', [21, 20, 300, 50], 35, offset = [5, 5])
        self.button1_bool = False
        self.current_algorithm = 'ahhh'

    
    def manager(self):
        act = self.button1.show(self.button1_bool)
        if act:
            self.display_menu()
        self.display_current_algorithm()
    
    def create_button(self):
        button = Button('Cambiar Algoritmo', [21, 20, 300, 50], 35, offset = [5, 5])
        self.buttons.append(button)

    def get_position(self, pos, button):
        cond1 = pos[0] > button.coord[0] and pos[1] > button.coord[1]
        cond2 = pos[0] < button.coord[0] + button.coord[2] and pos[0] < button.coord[0] + button.coord[2]
        return  cond1 and cond2
    
    def display_current_algorithm(self):
        font = pygame.font.SysFont('Arial', int(HEADER / 2.5))
        text = font.render('Algoritmo: ' + self.current_algorithm, True, black)
        self.screen.blit(text, (AMPLE / 5, HEADER / 4.6))

    def display_menu(self):
        self.menu1 = Menu('Algorimos disponibles', [AMPLE / 4, ALTURA / 4, AMPLE / 2, ALTURA / 2], 40).background()



class Button:
    def __init__(self, text, coord, size_text, color1 = white_dirty, color2 = blue, border_radius = 10, offset = [0,0]):
        self.screen = pygame.display.get_surface()
        self.text = text
        self.coord = coord
        self.size_text = size_text
        self.color1 = color1
        self.color2 = color2
        self.border_radius = border_radius
        self.offset = offset

    def show(self, pressed):
        font = pygame.font.SysFont('Arial', self.size_text)
        code = font.render(self.text, True, black)
        if pressed:
            pygame.draw.rect(self.screen, self.color2, self.coord, border_radius=self.border_radius)
        else:
            pygame.draw.rect(self.screen, self.color1, self.coord, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, black, self.coord, border_radius=self.border_radius, width=2)
        text_posx, text_posy = self.coord[0] + self.offset[0], self.coord[1] + self.offset[1]
        self.screen.blit(code, (text_posx, text_posy))
        return pressed
    
    # def 


class Menu:
    def __init__(self, title, coord, size_text, color = grey_menu, border_radius = 10):
        self.screen = pygame.display.get_surface()
        self.text = title
        self.coord = coord
        self.size_text = size_text
        self.color = color
        self.border_radius = border_radius

    def background(self):
        pygame.draw.rect(self.screen, self.color, self.coord, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, black, self.coord, border_radius=self.border_radius, width=2)


    


