import pygame 
from settings import *
from sort import exchanging as ex
import time
from tools import *
from header import Header

class Aplicacion:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Sort algorithms')
        self.screen = pygame.display.set_mode((AMPLE, ALTURA))
        self.set = Set()
        self.isRunning = True
        self.header = Header()
        self.event = Event(self.header, self.set)
        
    
    def run(self):
        while self.isRunning:
            self.event.event_manager()
            self.set.update()
            self.header.manager()
            pygame.display.update()

if __name__ == '__main__':
    app = Aplicacion()
    app.run()