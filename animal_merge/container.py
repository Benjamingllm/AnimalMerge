import pygame
import pymunk
from .config import ASSETS_DIR
class Container:
    wall_thickness = 10
    def __init__(self,space,width,height,color,x,y):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.create_walls(space)

        self.texture_image = ASSETS_DIR / "recipient_texture.png"
        self.texture_sprite = pygame.image.load(self.texture_image).convert()
        self.wall_size = self.wall_thickness * 2                
        side_height = self.height + self.wall_size             
        bottom_length = self.width + self.wall_size * 2        
        texture_height = max(side_height, bottom_length)       
        self.texture_sprite = pygame.transform.scale(self.texture_sprite,(400,texture_height))
        self.left_wall = self.texture_sprite.subsurface(0,0,self.wall_size,side_height)
        self.left_wall.fill("brown",special_flags=pygame.BLEND_RGB_MULT)
        self.right_wall = self.texture_sprite.subsurface(200,0,self.wall_size,side_height)
        self.right_wall.fill("brown",special_flags=pygame.BLEND_RGB_MULT)
        self.bottom_wall = self.texture_sprite.subsurface(200,0,self.wall_size,bottom_length)
        self.bottom_wall = pygame.transform.rotate(self.bottom_wall,90)
        self.bottom_wall.fill("brown",special_flags=pygame.BLEND_RGB_MULT)

    def create_walls(self,space):
        thickness = self.wall_thickness
        left = self.x - thickness
        right = self.x + self.width +thickness
        top = self.y 
        bottom = self.y + self.height + thickness

        walls = [
           ((left, top), (left, bottom)),  
           ((right, top), (right, bottom)),  
           ((left, bottom), (right, bottom))  
        ]

        for start, end in walls:
            wall = pymunk.Segment(space.static_body, start, end, thickness)
            wall.elasticity = 0.1
            wall.friction = 0.8
            space.add(wall)

    def draw(self, screen):
        pygame.draw.line(screen,"red",(self.x,self.y), (self.x+self.width,self.y),3)
        screen.blit(self.left_wall,(self.x - self.wall_size,self.y))
        screen.blit(self.bottom_wall,(self.x - self.wall_size,self.y + self.height))
        screen.blit(self.right_wall,(self.x + self.width,self.y))
        


