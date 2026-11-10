import pygame
from .config import ASSETS_DIR

class UI:

    def __init__(self):
        self.font = pygame.font.Font(None,32)
        self.start_image = ASSETS_DIR / "start.png"
        self.start_sprite = pygame.image.load(self.start_image)
        self.score_sign_image = ASSETS_DIR / "sign.png"
        self.score_sign_sprite = pygame.image.load(self.score_sign_image).convert_alpha()
        self.score_sign_sprite = pygame.transform.scale(self.score_sign_sprite,(150,150))

    def draw_score(self,screen,score,best):
        score = self.font.render(f"score : {score}",True,"White")
        best = self.font.render(f"best : {best}",True,"White")
        screen.blit(self.score_sign_sprite,(0,0))
        screen.blit(score,(30,75))
        screen.blit(best,(30,100))


    def start_display(self,screen,image):
        screen.blit("start_image",0,0)