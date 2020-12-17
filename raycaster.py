import pygame
import sys
import random
import math
import numpy as np

class Man:
    def __init__(self):
        self.pos = np.asmatrix(np.array([[400.0], [300.0]]))
        self.view = np.asmatrix(np.array([[1.0], [0.0]]))
    def step(self, direction):
        self.pos += np.asmatrix(np.array(direction))
    def look(self, rots):
        self.view = np.dot(np.asmatrix(np.array([[math.cos(rots*math.pi/12), -1*math.sin(rots*math.pi/12)], [math.sin(rots*math.pi/12), math.cos(rots*math.pi/12)]])), self.view)
    def all(self):
        output = []
        offset = np.dot(np.asmatrix(np.array([[math.cos(-400*math.pi/2400), -1*math.sin(-400*math.pi/2400)], [math.sin(-400*math.pi/2400), math.cos(-400*math.pi/2400)]])), self.view)
        for i in range(800):
            output += [(np.dot(np.asmatrix(np.array([[math.cos(i*math.pi/2400), -1*math.sin(i*math.pi/2400)], [math.sin(i*math.pi/2400), math.cos(i*math.pi/2400)]])), offset), i-400)]
        return output            

def main():
    pygame.init()
    pygame.key.set_repeat(5)
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    man = Man()
    green = (0,200,112)
    white = (255, 255, 255)
    b = (0, 0, 255)
    g = (0, 255, 0)
    red = (235, 0, 0)
    map = [[1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 1, 0, 1],           
           [1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1]]
    rotations = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    man.look(-.1)
                    rotations += 1/12
                if event.key == pygame.K_RIGHT:
                    man.look(.1)
                    rotations -= 1/12
                if event.key == pygame.K_DOWN:
                    man.pos -= man.view
                if event.key == pygame.K_UP:
                    man.pos += man.view
        screen.fill((0, 75, 0))
        #for i in range(6):
        #    for j in range(8):
        #        if map[i][j] == 1:
        #            pygame.draw.rect(screen, (0, 0, 0), (100*j+2, 100*i+2, 96, 96)) 
        #pygame.draw.line(screen, red, (man.pos.item(0), man.pos.item(1)), (man.pos.item(0)+100*man.view.item(0), man.pos.item(1)+100*man.view.item(1)))
        #pygame.draw.circle(screen, green, (man.pos.item(0), man.pos.item(1)), 10)
        dists = []
        for angle in man.all():
            dists += [check_ray(man.pos.item(0), man.pos.item(1), angle[0].item(0), angle[0].item(1), angle[1], map)]
        x = 0
        pygame.draw.rect(screen, (98, 221, 240), (0, 0, width, 200))
        for dist in dists:
            if dist[0] > 0:
                line = 50*(width**2 + height**2)**.5/dist[0]
            else:
                line = 650
            if line > 650:
                line = 650
            if dist[1] == 0:
                pygame.draw.line(screen, (100, 100, 100), (x, 200 - line/2), (x, 200+line/2))
            elif dist[1] ==1:
                pygame.draw.line(screen, (75, 75, 75), (x, 200 - line/2), (x, 200+line/2))
            else:
                pygame.draw.line(screen, (0, 0, 0), (x, 200 - line/2), (x, 200+line/2))            
            x += 1
        pygame.display.update()


    pygame.display.quit()

def check_ray(x, y, dx, dy, angle, map):
    distance = 0
    while map[int(y//100)][int(x//100)] == 0:
        x += dx
        y += dy
        distance += 1
    a = x - dx
    b = y - dy
    if a//100 == x//100 and b//100 != y//100:
        color = 1
    elif a//100 != x//100 and b//100 == y//100:
        color = 0
    else:
        color = 3
    return (distance*math.cos(angle*math.pi/2400), color)


if __name__ == '__main__':
    main()
