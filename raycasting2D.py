import pygame
from pygame.locals import *

class Ray:
    def __init__(self, position, direction):
        self.position = position 
        self.direction = direction

    def showSource(self):
        pygame.draw.circle(user_interface.window, (255, 255, 255), self.position, 5) 

    def getT1(self, obstacle):
        T2 = (self.direction[0] * (obstacle.position[1] - self.position[1]) + self.direction[1] * (self.position[0] - obstacle.position[0]) / (obstacle.direction[0] * self.direction[1] - obstacle.direction[1] * self.direction[0]))
        T1 = (obstacle.position[0] + obstacle.direction[0] * T2 - self.position[0]) / self.direction[0] 
        return T1

    def showRay(self):
        T1 = self.getT1(boundary)
        pygame.draw.line(user_interface.window, (255, 255, 0), self.position, (self.position[0] + T1 * self.direction[0], self.position[1] + T1 * self.direction[1]))

class Boundary:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.position = a 
        self.direction = (b[0] - a[0], b[1] - a[1]) 

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
        boundary.show()
        ray.showSource()
        ray.showRay()
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
boundary = Boundary((600, 200), (600, 600))
ray = Ray((200, 400), (1, 0))
user_interface.run()
