import pygame
import pygame_gui
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.manager = pygame_gui.UIManager((800, 600))
        
        
        # Charger l'image de fond
        self.background_image = pygame.image.load('menu.gif').convert()
        # Redimensionner l'image de fond pour qu'elle prenne tout l'écran
        self.background_image = pygame.transform.scale(self.background_image, self.screen.get_size())
        # Ajouter un champ de saisie de texte
        self.text_input = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((300, 200), (200, 50)), 
            manager=self.manager
        )
        self.submit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((300, 300), (200, 50)), 
            text='start', 
            manager=self.manager
        )
        
        self.clock = pygame.time.Clock()
        self.name = ""

    def run(self):
        running = True
        while running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.submit_button:
                            self.name = self.text_input.get_text()
                            print("Nom saisi:", self.name)
                            running = False

                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.screen.blit(self.background_image, (0, 0))  # Afficher l'image de fond
            self.manager.draw_ui(self.screen)
            pygame.display.flip()

# Tester le menu séparément
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    menu = Menu(screen)
    menu.run()
