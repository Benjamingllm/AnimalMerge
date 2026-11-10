import pygame
from .game import Game
from .game_over import GameOver
from .menu import Menu
from .config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
class App:
    def __init__(self):
        pygame.init()
        self.session = {"name": "", "score": 0,"best" : 0}
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.scene = Menu(self.session)
        self.running = True
        self.scenes = {
            "game_over" : GameOver,
            "game" : Game,
            "menu" : Menu
        }
        

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            delta_time = clock.tick(FPS) / 1000.
            self.handle_events()
            self.scene.update(delta_time)
            self.scene.draw(self.screen)
            pygame.display.flip()
            if self.scene.next_scene != None:
                self.scene = self.scenes[self.scene.next_scene](self.session)
        pygame.quit()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scene.handle_event(event)


  

    
    

    
