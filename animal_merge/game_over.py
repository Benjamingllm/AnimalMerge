import pygame
from .config import ASSETS_DIR, WINDOW_WIDTH, WINDOW_HEIGHT
from .scores import save_score

BLINK_PERIOD = 0.5  # secondes visible, puis autant de secondes caché


class GameOver:
    def __init__(self,session):
        self.next_scene = None
        self.session = session
        save_score(session["name"], session["score"])
        self.bg_image = ASSETS_DIR / "loose.png"
        self.text_image = ASSETS_DIR / "game_over.png"
        self.text_sprite = pygame.image.load(self.text_image).convert_alpha()
        self.text_rect = self.text_sprite.get_rect(centerx=WINDOW_WIDTH // 2, top=150)
        self.bg_sprite = pygame.image.load(self.bg_image).convert()
        width, height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.bg_sprite = pygame.transform.scale(self.bg_sprite, (width, width))
        self.bg_pos = (0, (height - width) // 2)
        font = pygame.font.Font(None, 36)
        message = "Espace pour revenir au menu"
        self.hint_text = font.render(message, True, (255, 248, 230))
        self.hint_shadow = font.render(message, True, (60, 35, 20))
        self.hint_rect = self.hint_text.get_rect(midbottom=(width // 2, height - 40))
        self.blink_timer = 0.0

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN:
            self.inputs(event.key)

    def update(self,delta_time):
        self.blink_timer += delta_time

    def draw(self,screen):
        screen.blit(self.bg_sprite, self.bg_pos)
        screen.blit(self.text_sprite, self.text_rect)
        if int(self.blink_timer / BLINK_PERIOD) % 2 == 0:
            screen.blit(self.hint_shadow, self.hint_rect.move(2, 2))
            screen.blit(self.hint_text, self.hint_rect)

    def inputs(self,key):
        if key == pygame.K_SPACE:
            
            self.next_scene = "menu"