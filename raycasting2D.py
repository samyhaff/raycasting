import pygame
from pygame.locals import *

class Source:
    def __init__(self):
        self.position = pygame.mouse.get_pos()

    def update(self):
        self.position = pygame.mouse.get_pos()

    def show(self):
        pygame.draw.circle(user_interface.window, (255, 255, 255), self.position, 5)

class Ray:
    def __init__(self, position, direction):
        self.position = position 
        self.direction = direction

    #def showSource(self):
    #    pygame.draw.circle(user_interface.window, (255, 255, 255), self.position, 5) 

    def update(self):
        self.position = source.position

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
        source.update()
        source.show()
        for boundary in boundaries:
            boundary.show()
        for ray in rays:
            ray.update()
            ray.show()
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
source = Source()
boundary = Boundary((600, 500), (600, 600))
boundary2 = Boundary((400, 500), (400, 600))
ray = Ray((200, 400), (1, 0))
boundaries = [boundary, boundary2, Boundary((800, 0), (800, 800)), Boundary((0, 0), (800, 0)), Boundary((0, 0), (0, 800)), Boundary((0, 800), (800, 800))]
rays = [ray]
user_interface.run()
pygame.quit()
