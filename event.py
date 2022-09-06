import pygame

class Event():
    def __init__(self, header):
        self.shuffle = False
        self.header = header

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.header.set.shuffle = True
                if event.key == pygame.K_SPACE:
                    self.header.set.go = True
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
        for button in self.header.buttons:
            button.show()
        if button.active:
            if button.type == "activate":
                button.active = False
            button.activate_button()
        if self.header.set.go:
            self.header.algorithm.sort()
