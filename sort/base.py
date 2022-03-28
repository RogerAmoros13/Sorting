from tools import Draw, Event
import pygame
import time

class Sort:
    def __init__(self, array):
        self.arr = array
        self.n = len(array)
        self.draw = Draw(len(array))
        self.event = Event()

    def control(self):
        self.event.event_manager()
        self.draw.draw_background()
    
    def update(self):
        pygame.display.update()
        time.sleep(0.01)

    def check(self):
        for i in range(self.n - 1):
            self.control()
            if self.arr[i] < self.arr[i + 1]:
                self.draw.draw_check(self.arr, i, True)
                
            else:
                self.draw.draw_check(self.arr, i, False)
                return True
            self.update()
            time.sleep(0.01)

        self.draw.draw_check(self.arr, self.n, True)                
        self.update()
        return False
