import pygame
import sys
import random

# --------- Configurações ---------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (70, 130, 180)

pygame.init()
pygame.display.set_caption("Menu Inicial - Jogo da Forca")
FONT = pygame.font.SysFont(None, 48)

# ----------------- Classe Botão -----------------
class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.callback = callback
        self.default_color = WHITE
        self.highlight_color = HIGHLIGHT
        self.label = FONT.render(self.text, True, self.default_color)
        self.rect = self.label.get_rect(center=pos)

    def draw(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            label = FONT.render(self.text, True, self.highlight_color)
        else:
            label = self.label
        surface.blit(label, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.callback()

# ----------------- Classe Menu -----------------
class Menu:
    def __init__(self, screen):
        self.screen = screen
        mid_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2 - 50
        gap = 70

        self.buttons = [
            Button("Iniciar Jogo", (mid_x, start_y), self.start_game),
            Button("Sair",         (mid_x, start_y + gap), self.exit_game),
        ]
        self.running = True

    def start_game(self):
        print("Iniciando jogo da forca...")
        self.running = False
        main_forca()  # Chama o jogo da forca no terminal

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for btn in self.buttons:
                        btn.check_click(mouse_pos)

            self.screen.fill(BLACK)
            for btn in self.buttons:
                btn.draw(self.screen, mouse_pos)

            pygame.display.flip()
            clock.tick(FPS)

# ----------------- Classe Game -----------------
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        menu = Menu(self.screen)
        menu.run()

# ----------------- Jogo da Forca (terminal) -----------------
base = ['''
>>>>>>>>>>>>>>> FORCA <<<<<<<<<<<<<<<
 +---+
 |   |
     |
     |
     |
     |
 =========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Jogo:
    def __init__(self, linguagem):
        self.linguagem = linguagem
        self.escrita_erradas = []
        self.escrita_certas = []

    def adivinhar(self, palavra):
        if palavra in self.linguagem and palavra not in self.escrita_certas:
            self.escrita_certas.append(palavra)
        elif palavra not in self.linguagem and palavra not in self.escrita_erradas:
            self.escrita_erradas.append(palavra)
        else:
            return False
        return True