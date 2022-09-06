import pygame 
from settings import *
from set import Set
from event import Event
from header import Header

class Aplicacion:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Sort algorithms')
        self.screen = pygame.display.set_mode((AMPLE, ALTURA))
        self.set = Set()
        self.header = Header(self.set)
        self.event = Event(self.header)
        self.isRunning = True
        
    
    def run(self):
        while self.isRunning:
            self.event.event_manager()
            pygame.display.update()

if __name__ == '__main__':
    app = Aplicacion()
    app.run()