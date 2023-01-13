import pygame
import time

class Sort:
    def __init__(self, header, name):
        self.n = header.set.n
        self.name = name
        self.header = header

    # def control(self):
    #     self.event.event_manager()
    #     self.set.draw_background()
    
    # def update(self):
    #     pygame.display.update()
    #     time.sleep(0.01)

    def check(self, array):
        if self.i:
            array.set[self.i - 1].color = (255,255,255)
        if array.set[self.i] < array.set[self.i + 1]:
            array.set[self.i].color = (124,252,0)
            array.set[self.i + 1].color = (124,252,0)
        else:
            array.set[self.i].color = (220,20,60)
            array.set[self.i + 1].color = (220,20,60)
        self.i += 1
        if self.i - self.n + 1 == 0:
            return True
        return False

        # for i in range(self.n - 1):
        #     if self.arr[i] < self.arr[i + 1]:
        #         self.set.draw_check(self.arr, i, True)
                
        #     else:
        #         self.set.draw_check(self.arr, i, False)
        #         return True
        #     self.update()
        #     time.sleep(0.01)

    #     self.set.draw_check(self.arr, self.n, True)                
    #     self.update()
    #     return False
