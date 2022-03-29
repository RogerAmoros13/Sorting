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
        self.draw = Draw(self.set.n)
        self.isRunning = True
        self.header = Header()
        self.event = Event(self.header)
        
    
    def run(self):
        while self.isRunning:
            self.event.event_manager()

            if self.event.shuffle:
                self.set.shuffle(self.event.shuffle_step)
                self.event.shuffle_step += 1
                time.sleep(0.001)
                if self.event.shuffle_step == self.set.n - 1:
                    self.event.shuffle = False

            self.draw.draw_background()
            self.draw.draw_set(self.set.set)
            if self.event.go and not self.event.shuffle:
                self.solver = ex.Bubble(self.set.set)
                test = self.solver.sort()
                self.event.go = False

            self.header.manager()
            pygame.display.update()

if __name__ == '__main__':
    app = Aplicacion()
    app.run()