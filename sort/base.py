import pygame
import time

class Sort:
    def __init__(self, set, name):
        self.n = len(set.n)
        self.set = set
        self.name = name

    def control(self):
        self.event.event_manager()
        self.set.draw_background()
    
    def update(self):
        pygame.display.update()
        time.sleep(0.01)

    def check(self):
        for i in range(self.n - 1):
            self.control()
            if self.arr[i] < self.arr[i + 1]:
                self.set.draw_check(self.arr, i, True)
                
            else:
                self.set.draw_check(self.arr, i, False)
                return True
            self.update()
            time.sleep(0.01)

        self.set.draw_check(self.arr, self.n, True)                
        self.update()
        return False
