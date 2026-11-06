import pygame
import pymunk

class Conteneur:
    wall_thickness = 10
    def __init__(self,space,width,height,color,x,y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.creer_murs(space)


    def creer_murs(self,space):
        thickness = self.wall_thickness
        left = self.x - thickness
        right = self.x + self.width
        top = self.y - thickness
        bottom = self.y + self.height

        walls = [
           ((left, top), (left, bottom)),  # Left wall
           ((right, top), (right, bottom)),  # Right wall
           ((left, bottom), (right, bottom))  # Bottom wall
        ]

        for start, end in walls:
            wall = pymunk.Segment(space.static_body, start, end, thickness)
            wall.elasticity = 0.1
            wall.friction = 0.8
            space.add(wall)

    def draw(self, screen):
        wall = self.wall_thickness*2
        pygame.draw.rect(screen,self.color,(self.x-wall,self.y,wall,self.height+wall))
        pygame.draw.rect(screen,self.color,(self.x-wall,self.y+self.height,self.width+wall*2,wall))
        pygame.draw.rect(screen,self.color,(self.x+self.width,self.y,wall,self.height+wall))



