import pygame
from .config import ASSETS_DIR, WINDOW_WIDTH, WINDOW_HEIGHT
NAME_MAX_LENGTH = 12
from .scores import get_best_score
class Menu:
    def __init__(self,session):
        self.next_scene = None
        self.session = session
        self.bg_image = ASSETS_DIR / "start.png"
        self.btn_image = ASSETS_DIR / "play.png"
        self.logo_image = ASSETS_DIR / "logo.png"
        self.btn_sprite = pygame.image.load(self.btn_image).convert_alpha()
        self.btn_sprite = self.btn_sprite.subsurface(self.btn_sprite.get_bounding_rect())
        self.btn_rect = self.btn_sprite.get_rect(centerx=WINDOW_WIDTH // 2, top=250)
        self.logo_sprite = pygame.image.load(self.logo_image).convert_alpha()
        self.logo_rect = self.logo_sprite.get_rect(centerx=WINDOW_WIDTH // 2, top=50)


        self.bg_sprite = pygame.image.load(self.bg_image).convert()

        width, height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.bg_sprite = pygame.transform.scale(self.bg_sprite, (width, width))
        self.bg_pos = (0, (height - width) // 2)
        self.name = ""
        self.font = pygame.Font(None,40)
        self.name_rect = pygame.Rect(0,0,300,50)
        self.name_rect.midtop = (WINDOW_WIDTH // 2, 430)
    
        
    def handle_event(self, event):
        if event.type == pygame.TEXTINPUT:
            self.type_text(event.text)
        elif event.type == pygame.KEYDOWN:
            self.inputs(event.key)
        elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1
              and self.btn_rect.collidepoint(event.pos)):
            self.start_game()

    def update(self,delta_time):
        pass

    def draw(self,screen):
        screen.blit(self.bg_sprite, self.bg_pos)
        screen.blit(self.btn_sprite, self.btn_rect)
        screen.blit(self.logo_sprite,self.logo_rect)

        pygame.draw.rect(screen, (255, 248, 230), self.name_rect, border_radius=8)
        pygame.draw.rect(screen, (60, 35, 20), self.name_rect, width=3, border_radius=8)
        if self.name:
            text = self.font.render(self.name, True, (60, 35, 20))
        else:
            text = self.font.render("Ton pseudo", True, (160, 140, 120))
        screen.blit(text, text.get_rect(center=self.name_rect.center))


    def inputs(self,key):
        if key == pygame.K_BACKSPACE:
            
            self.name = self.name[:-1]
        elif key in (pygame.K_RETURN,pygame.K_KP_ENTER):
            self.start_game()

    def start_game(self):
        if self.name.strip():
            self.session["name"] = self.name
            self.session["best"] = get_best_score(self.name)
            self.next_scene = "game"
            
            

    def type_text(self, text):
        if len(self.name) + len(text) <= NAME_MAX_LENGTH:
            self.name += text