import pygame
import pymunk
from .container import Container
from .ui import UI
from .merge import MergeManager
from .animal import Mouse, Hamster, Fox
from .config import (
    ASSETS_DIR, PHYSICS_TIME_STEP, GRAVITY, LOSE_DELAY, DROP_COOLDOWN,
    CONTAINER_X, CONTAINER_Y, CONTAINER_WIDTH, CONTAINER_HEIGHT, PENDING_Y,WINDOW_HEIGHT,WINDOW_WIDTH
)

import random

class Game:

    def __init__(self,session):
        self.bg_image = ASSETS_DIR / "bg.png"
        self.session = session
        self.bg_sprite = pygame.image.load(self.bg_image).convert()
        self.bg_sprite = pygame.transform.scale(self.bg_sprite,(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.ui = UI()
        self.drop_cooldown = 0
        self.animals = {}
        self.score = 0
        self.accumulated_time = 0.0
        self.next_scene = None
        self.space = pymunk.Space()
        self.space.gravity = GRAVITY
        self.container = Container(self.space, CONTAINER_WIDTH, CONTAINER_HEIGHT, (255, 0, 0), CONTAINER_X, CONTAINER_Y)
        self.merge_manager = MergeManager(self.space, self.animals)
        self.pending= self.pick_random_animal()
        self.best = session["best"]

    def draw(self,screen):
        screen.blit(self.bg_sprite,(0,0))
        self.container.draw(screen)
        self.pending.draw(screen)
        for animal in self.animals.values():
            animal.draw(screen)
        self.ui.draw_score(screen,self.score,self.best)



    def handle_event(self,event):

        if event.type == pygame.KEYDOWN and self.drop_cooldown <=0 :
            self.inputs(event.key)
            self.drop_cooldown = DROP_COOLDOWN




    def update(self, delta_time):
 
        self.drop_cooldown -= delta_time
        mouse_x = pygame.mouse.get_pos()[0]
        self.pending.body.position =( max(self.container.x + self.container.wall_thickness, min(mouse_x, self.container.x + self.container.width - self.container.wall_thickness)), PENDING_Y)
        self.accumulated_time += delta_time
        while self.accumulated_time >= PHYSICS_TIME_STEP:
            self.space.step(PHYSICS_TIME_STEP)
            self.accumulated_time -= PHYSICS_TIME_STEP
            self.score += self.merge_manager.resolve_merges()
            self.check_lose()

            

    def pick_random_animal(self):
        selected_class = random.choices([Mouse, Hamster, Fox], weights=[60, 30, 10])[0]


        mouse_x = pygame.mouse.get_pos()[0]
        x = max(self.container.x + self.container.wall_thickness, min(mouse_x, self.container.x + self.container.width - self.container.wall_thickness))
        return selected_class(x, PENDING_Y)

    def inputs(self,key):
        if key == pygame.K_SPACE:
            
            self.merge_manager.add_animal(self.pending)
            self.pending = self.pick_random_animal()

    def check_lose(self):
        for animal in self.animals.values():
            if animal.body.position.y - animal.size < self.container.y:

                animal.time_above_line += PHYSICS_TIME_STEP
            else:
                animal.time_above_line = 0.0
            if animal.time_above_line >= LOSE_DELAY:
                self.session["score"] = self.score
                self.next_scene = "game_over"

