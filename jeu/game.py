import pygame


class Game:

    def __init__(self):

        # cree la fenetre du jeu
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("passe temps")

    def run(self):

        #boucle du jeu
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()