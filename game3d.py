import pygame
import sys
import random
import math
import numpy as np

class Man:
    def __init__(self):
        self.pos = np.asmatrix(np.array([[300], [300], [-300]]))
    def step(self, direction):
        self.pos += np.asmatrix(np.array(direction))

def main():
    pygame.init()

    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    green = (0,200,112)
    white = (255, 255, 255)
    b = (0, 0, 255)
    g = (0, 255, 0)
    red = (235, 0, 0)
    trans = np.asmatrix(np.array([[1, 0, 0], [0, 1, 0]]))
    corns = [np.asmatrix(np.array([[0], [500], [0]])), np.asmatrix(np.array([[500], [500], [0]])), 
             np.asmatrix(np.array([[500], [0], [0]])), np.asmatrix(np.array([[0], [0], [0]]))]
    #corns3 = [np.asmatrix(np.array([[100], [500], [-300]])), np.asmatrix(np.array([[500], [500], [-300]])), np.asmatrix(np.array([[500], [100], [-300]])),
    #          np.asmatrix(np.array([[500], [100], [-302]])), np.asmatrix(np.array([[500], [500], [-310]])), np.asmatrix(np.array([[100], [500], [-308]]))]

    corns2 = [np.asmatrix(np.array([[100], [500], [-100]])), np.asmatrix(np.array([[500], [500], [-100]])), np.asmatrix(np.array([[500], [100], [-100]])), np.asmatrix(np.array([[100], [100], [-100]]))]

    man = Man()
    rotations = [0, 0, 0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pygame.key.set_repeat(5)
                    man.step([[-1], [0], [0]])
                if event.key == pygame.K_RIGHT:
                    pygame.key.set_repeat(5)
                    man.step([[1], [0], [0]])
                if event.key == pygame.K_DOWN:
                    pygame.key.set_repeat(5)
                    man.step([[0], [1], [0]])
                if event.key == pygame.K_UP:
                   pygame.key.set_repeat(5)
                   man.step([[0], [-1], [0]])
                if event.key == pygame.K_SPACE:
                    pygame.key.set_repeat()
                    if man.pos.item(2) == -100:
                        man.step([[0], [0], [-200]])
                    else:
                        man.step([[0], [0], [200]])
                if event.key == pygame.K_a:
                    pygame.key.set_repeat()
                    rotations[0] -= 1
                    trans = np.dot(trans, rotate_x(-1))
                if event.key == pygame.K_d:
                    pygame.key.set_repeat()
                    rotations[0] += 1
                    trans = np.dot(trans, rotate_x(1))
                if event.key == pygame.K_s:
                    pygame.key.set_repeat()
                    rotations[1] -= 1
                    trans = np.dot(trans, rotate_y(-1))
                if event.key == pygame.K_w:
                    pygame.key.set_repeat()
                    rotations[1] += 1
                    trans = np.dot(trans, rotate_y(1))
                if event.key == pygame.K_z:
                    pygame.key.set_repeat()
                    rotations[2] -= 1
                    trans = np.dot(trans, rotate_z(-1))
                if event.key == pygame.K_x:
                    pygame.key.set_repeat()
                    rotations[2] += 1
        po = []
        po2 = []
        #po3 = []
        for i in range(4):
            pos =  np.dot(trans, corns[i])
            po += [(pos.item(0)+300, pos.item(1)+400)]
            pos2 =  np.dot(trans, corns2[i])
            po2 += [(pos2.item(0)+300, pos2.item(1)+400)]
        #for i in range(6):
        #    pos3 =  np.dot(trans, corns3[i])
        #    po3 += [(pos3.item(0)+300, pos3.item(1))]

        screen.fill(white)
        pygame.draw.polygon(screen, g, po)
        pygame.draw.polygon(screen, b, po2)
        #pygame.draw.polygon(screen, green, po3)
        mp = np.dot(trans, man.pos)
        pygame.draw.circle(screen, red, (mp.item(0)+300, mp.item(1)), .02 * man.pos.item(1)+3)


        pygame.display.update()


    pygame.display.quit()

# Returns a 3x3 rotation matrix rotating (rots * pi/12) radians around desired axis
def rotate_z(rots):
    return np.asmatrix(np.array([[math.cos(rots*math.pi/12), -1*math.sin(rots*math.pi/12), 0], [math.sin(rots*math.pi/12), math.cos(rots*math.pi/12), 0], [0, 0, 1]]))

def rotate_x(rots):    
    return np.asmatrix(np.array([[1, 0, 0], [0, math.cos(rots*math.pi/12), -1*math.sin(rots*math.pi/12)], [0, math.sin(rots*math.pi/12), math.cos(rots*math.pi/12)]]))

def rotate_y(rots):    
    return np.asmatrix(np.array([[math.cos(rots*math.pi/12), 0, math.sin(rots*math.pi/12)], [0, 1, 0], [-1*math.sin(rots*math.pi/12), 0, math.cos(rots*math.pi/12)]]))



if __name__ == '__main__':
    main()
