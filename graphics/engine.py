import pygame
import sys

class GameEngine:
    
    def __init__(self, screen_width=800, screen_height=600):
        
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("La tour")
        self.clock = pygame.time.clock()
        self.running = True
        
        self.background = pygame.image.load("graphics/resources/background.png")
        self.font = pygame.font.Font("graphics/resources/font.ttf", 26)
        pygame.mixer.music.load("graphics/resources/ambiance.mp3")
        
    def draw_text(self, text, x, y):
        
        rendered_text = self.font.render(text, True, (255,255,255))
        self.screen.blit(rendered_text, (x, y))
        pygame.display.flip()
        
    def display_scene(self, scene_text, choices):
        
        self.screen.fill((0,0,0))
        self.screen.blit(self.background,(0,0))
        
        y = 450
        
        for line in scene_text:
            self.draw_text(line, 50, y)
            y += 40
            
        y += 30
        
        for i, choice in enumerate(choices):
            self.draw_text(f"{i+1}. {choice['text']}", 50, y)
        
        pygame.display.flip()
    
    
    def run(self, scene_callback):
        
        current_scene = scene_callback
        
        while self.running:
            self.display_scene(current_scene['text'], current_scene['choices'])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_1 and len(current_scene['choices']) > 0:
                        current_scene = scene_callback(0)  # Premier choix
                    if event.key == pygame.K_2 and len(current_scene['choices']) > 1:
                        current_scene = scene_callback(1)  # Deuxième choix
    
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()
    
    def fade_screen(self):
        fade = pygame.Surface((800, 600))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.screen.blit(fade, (0,0))
            pygame.display.flip()
            pygame.time.delay(5)
        
        
