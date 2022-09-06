import pygame
from settings import *

"""
Button1: Cambio de algoritmo
"""

class Header:
    def __init__(self, set):
        self.screen = pygame.display.get_surface()
        self.set = set
        self.buttons = self._create_buttons()
        self.algorithm = Bubble(self)
    
    def update(self):
        self.set.update()
        self.display_current_algorithm()
    
    def _create_buttons(self):
        button_list = self.create_button(
            [
                {
                    "name": "menu_algoritm",
                    "text": "Cambiar Algoritmo",
                    "coordenates": [21, 20, 300, 50],
                    "type": "menu",
                    "menu": Menu(
                        'Algorimos disponibles', 
                        [AMPLE / 4, ALTURA / 4, AMPLE / 2, ALTURA / 2], 
                        40
                    )
                },
                {
                    "name": "start_algorithm",
                    "text": "Start",
                    "color1": green,
                    "coordenates": [900, 20, 100, 50],
                    "type": "activate",
                    "bool_field": "go",
                    "_class": self.set
                },
                {
                    "name": "end_algorithm",
                    "text": "Shuffle",
                    "coordenates": [770, 20, 120, 50],
                    "type": "activate",
                    "bool_field": "shuffle",
                    "_class": self.set
                }
            ]
        )
        return button_list
        
    def create_button(self, vals_dict):
        button_list = []
        for vals in vals_dict:
            button_list.append(Button(vals))
        return button_list

    def get_position(self, pos, button):
        cond1 = pos[0] > button.coord[0] and pos[1] > button.coord[1]
        cond2 = pos[0] < button.coord[0] + button.coord[2] and pos[0] < button.coord[0] + button.coord[2]
        return  cond1 and cond2
    
    def display_current_algorithm(self):
        font = pygame.font.SysFont('Arial', int(HEADER / 2.5))
        text = font.render('Algoritmo: ' + self.algorithm.name, True, black)
        self.screen.blit(text, (AMPLE / 5, HEADER / 4.6))


class Button:
    def __init__(self, vals):
        self.screen = pygame.display.get_surface()
        self.name = vals.get("name")
        self.text = vals.get("text", "")
        self.coord = vals.get("coordenates", [0,0,0,0])
        self.size_text = vals.get("text_size", 35)
        self.color1 = vals.get("color1", white_dirty)
        self.color2 = vals.get("color2", blue)
        self.border_radius = vals.get("border_radius", 10)
        self.offset = vals.get("offset", [5,5])
        self.active = False
        self.pressed = False
        self.type = vals.get("type", "null")
        self.menu = vals.get("menu", False)
        self._class = vals.get("_class", False)
        self.bool_field = vals.get("bool_field", False)


    def show(self):
        font = pygame.font.SysFont('Arial', self.size_text)
        code = font.render(self.text, True, black)
        if self.pressed:
            pygame.draw.rect(self.screen, self.color2, self.coord, border_radius=self.border_radius)
        else:
            pygame.draw.rect(self.screen, self.color1, self.coord, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, black, self.coord, border_radius=self.border_radius, width=2)
        text_posx, text_posy = self.coord[0] + self.offset[0], self.coord[1] + self.offset[1]
        self.screen.blit(code, (text_posx, text_posy))
    
    def activate_button(self):
        if self.type == "menu":
            self.menu.update()
        elif self.type == "activate":
            setattr(self._class, self.bool_field, True)

class Menu:
    def __init__(self, title, coord, size_text, color = grey_menu, border_radius = 10):
        self.screen = pygame.display.get_surface()
        self.text = title
        self.coord = coord
        self.size_text = size_text
        self.color = color
        self.border_radius = border_radius

    def update(self):
        self.draw_background()

    def draw_background(self):
        pygame.draw.rect(self.screen, self.color, self.coord, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, black, self.coord, border_radius=self.border_radius, width=2)


    


