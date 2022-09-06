from sort.base import Sort

class Bubble(Sort):
    def __init__(self, header):
        Sort.__init__(self, header, "Bubble")

    def sort(self):
        for i in range(self.n):
            for j in range(self.n - i - 1):
                self.header.set.set[j].color = (220,20,60)
                self.header.set.set[j + 1].color = (220,20,60)
                if self.header.set.set[j].height > self.header.set.set[j + 1].height:
                    self.header.set.set[j].height, self.header.set.set[j + 1].height = self.header.set.set[j + 1].height, self.header.set.set[j].height
                    self.header.set.update()
# class CocktailShake(Sort):
#     def __init__(self, array):
#         Sort.__init__(self, array, "CocktailShake")

#     def sort(self):
#         iters, swaps = 0, 0
#         swapped = True
#         while swapped:
#             swapped = False
#             for i in range(self.n - 2):
#                 iters += 1
#                 if self.arr[i] > self.arr[i + 1]:
#                     swaps += 1
#                     self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
#                     swapped = True
#                     self.control()
#                     self.draw.draw_algorithm(self.arr, i, i + 1)
#                     self.update()
#             if not swapped:
#                 break

#             for i in range(self.n - 2, 0, -1):
#                 iters += 1
#                 if self.arr[i] > self.arr[i + 1]:
#                     swaps += 1
#                     self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
#                     swapped = True
#                     self.control()
#                     self.draw.draw_algorithm(self.arr, i, i + 1)
#                     self.update()

#         test = self.check()
#         return test

# class Gnome(Sort):
#     def __init__(self, array):
#         Sort.__init__(self, array, "Gnome")

#     def sort(self):
#         i = 1
#         while i < self.n:
#             if self.arr[i - 1] < self.arr[i]:
#                 i += 1
#             else:
#                 self.arr[i], self.arr[i - 1] = self.arr[i - 1], self.arr[i]
#                 i -= 1
#                 if i == 0:
#                     i = 1
#                 self.control()
#                 self.draw.draw_algorithm(self.arr, i)
#                 self.update()

#         test = self.check()
#         return test

# class OddEven(Sort):
#     def __init__(self, array):
#         Sort.__init__(self, array, "OddEven")

#     def sort(self):
#         sorted = False
#         while not sorted:
#             sorted = True
#             for i in range(1, self.n - 1, 2):
#                 if self.arr[i] > self.arr[i + 1]:
#                     self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
#                     sorted = False
#                     self.control()
#                     self.draw.draw_algorithm(self.arr, i)
#                     self.update()

#             for i in range(0, self.n - 1, 2):
#                 if self.arr[i] > self.arr[i + 1]:
#                     self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
#                     sorted = False
#                     self.control()
#                     self.draw.draw_algorithm(self.arr, i, i + 1)
#                     self.update()
            
#         test = self.check()
#         return test
    
# class Comb11(Sort):
#     def __init__(self, array):
#         Sort.__init__(self, array, "Comb11")

#     def sort(self):
#         gap = self.n

#         swapped = True
#         while gap > 1 or swapped:
#             if gap > 1:
#                 gap = int(gap // 1.3)
#                 if gap == 10 or gap == 9:
#                     gap = 11
#                 if gap < 1:
#                     gap = 1
#             i = 0
#             swapped = False
#             while i + gap < self.n:
#                 if self.arr[i] > self.arr[i + gap]:
#                     self.arr[i], self.arr[i + gap] = self.arr[i + gap], self.arr[i]
#                     swapped = True
#                 i += 1
#                 self.control()
#                 self.draw.draw_algorithm(self.arr, i, i + gap)
#                 self.update()
        
#         test = self.check()
#         return test