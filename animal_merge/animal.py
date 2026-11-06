

import pymunk
import pygame
ANIMAL_COLLISION = 1

class Animal:
    size = 0
    color = (0, 0, 0)
    points = 0
    image = None
    level = 0
    def __init__(self, x, y,space):
        mass =self.size * 0.01
        moment = pymunk.moment_for_circle(mass, 0, self.size)
        self.body = pymunk.Body(mass, moment)
        self.body.position = (x, y)

        self.shape = pymunk.Circle(self.body, self.size)
        self.shape.elasticity = 0.5
        self.shape.friction = 1
        self.shape.collision_type = ANIMAL_COLLISION
        space.add(self.body, self.shape)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.shape.body.position.x), int(self.shape.body.position.y)), self.size)


class Souris(Animal):
    size = 14
    points = 1
    sprite = "none"
    color = "gray"


class Hamster(Animal):
    size = 18
    points = 3
    sprite = "none"
    color = "brown"


class Renard(Animal):
    size = 36
    points = 15
    sprite = "none"
    color = "orange"


class Chien(Animal):
    size = 44
    points = 21
    sprite = "none"
    color = "black"

class Mouton(Animal):
    size = 53
    points = 28
    sprite = "none"
    color = "white"

class Vache(Animal):
    size = 63
    points = 36
    sprite = "none"
    color = "blue"