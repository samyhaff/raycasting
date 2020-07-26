import pygame
from pygame.locals import *

#class Source:

class Ray:
    def __init__(self, position, direction):
        self.position = position 
        self.direction = direction

    #def showSource(self):
    #    pygame.draw.circle(user_interface.window, (255, 255, 255), self.position, 5) 

    def getT1(self, obstacle):
        if (self.direction[0] * obstacle.direction[1]) - (self.direction[1] * obstacle.direction[0]) == 0:
            return None
        T2 = ((self.direction[0] * (obstacle.position[1] - self.position[1]) + self.direction[1] * (self.position[0] - obstacle.position[0])) / (obstacle.direction[0] * self.direction[1] - obstacle.direction[1] * self.direction[0]))
        T1 = (obstacle.position[0] + obstacle.direction[0] * T2 - self.position[0]) / self.direction[0] 
        if T1 <= 0 or T2 > 1 or T2 < 0:
            return None 
        return T1

    def show(self):
        l = [self.getT1(obstacle) for obstacle in boundaries] 
        T1 = min([self.getT1(obstacle) for obstacle in boundaries if self.getT1(obstacle) != None])
        pygame.draw.line(user_interface.window, (255, 255, 0), self.position, (self.position[0] + T1 * self.direction[0], self.position[1] + T1 * self.direction[1]))

"""
    def getT1(self, obstacle):
        x1, y1 = self.position 
        v1 = self.direction
        x2, y2 = obstacle.position
        v2 = obstacle.direction 
        denominator = v1[0] * v2[1] - (v1[1] * v2[0])
        if denominator == 0:
            return None 
        T1 = ((x1 - x2) * (-v2[1])) + ((y1 - y2) * v2[0]) / denominator 
        T2 = (v1[0] * (y1 - y2)) - (v1[1] * (x1 - x2)) / denominator 
        print(T1, T2)
        if T1 <= 0:
            return None
        return T1
"""

class Boundary:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.position = a 
        self.direction = (self.b[0] - self.a[0], self.b[1] - self.a[1]) 

    def show(self):
        pygame.draw.line(user_interface.window, (255, 255, 255), self.a, self.b, 3)

class UserInterface:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.running = True 

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break

    def update(self):
        pass

    def render(self):
        self.window.fill((0, 0, 0))
        for boundary in boundaries:
            boundary.show()
        for ray in rays:
            ray.show()
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
boundary = Boundary((600, 500), (600, 600))
boundary2 = Boundary((400, 500), (400, 600))
ray = Ray((200, 400), (1, 0))
boundaries = [boundary, boundary2, Boundary((800, 0), (800, 800)), Boundary((0, 0), (800, 0)), Boundary((0, 0), (0, 800)), Boundary((0, 800), (800, 800))]
rays = [ray]
user_interface.run()
pygame.quit()
