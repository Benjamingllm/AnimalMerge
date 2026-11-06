import pygame
import pymunk
from .conteneur import Conteneur
from .animal import Souris, Hamster, Renard, Chien, Mouton, Vache
import random
PHYSICS_TIME_STEP = 1 / 120.0
class App:
    def __init__(self,settings):
        self.settings = settings
        self.animals = []
        self.screen = pygame.display.set_mode((self.settings.window_width,self.settings.window_height))
        self.fps = self.settings.fps
        #crer la boucle du jeu
        self.running = True
        self.accumulated_time = 0.0
        self.background_color = settings.background_color

        self.space = pymunk.Space()
        self.space.gravity = (0, 900)
        self.conteneur = Conteneur(self.space,350, 400, (255, 0, 0), 200, 150)
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            delta_time = clock.tick(self.fps) / 1000.
            self.handle_events()
            self.update(delta_time)

    

            self.draw()
        pygame.quit()

    def draw(self):
        self.screen.fill(self.background_color)
        self.conteneur.draw(self.screen)
        for animal in self.animals:
            animal.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.inputs(event.key)

    def update(self, delta_time):
        self.accumulated_time += delta_time
        while self.accumulated_time >= PHYSICS_TIME_STEP:
            self.space.step(PHYSICS_TIME_STEP)
            self.accumulated_time -= PHYSICS_TIME_STEP


    def pick_random_animal(self):
        animal_classes = [Souris, Hamster, Renard, Chien, Mouton, Vache]
        selected_class = random.choice(animal_classes)
        x = random.randint(200, 550)
        y = random.randint(150, 400)
        return selected_class(x, y,self.space)

    def inputs(self,key):
        if key == pygame.K_SPACE:
            animal = self.pick_random_animal()
            self.add_animal(animal)


    def add_animal(self, animal):
        self.animals.append(animal)