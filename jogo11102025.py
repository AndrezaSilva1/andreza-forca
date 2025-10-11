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
        print("\nIniciando jogo da forca...")
        self.running = False
        # Executa o jogo da forca no terminal
        Jogo.forca_principal()
        # Após o jogo terminar, volta ao menu
        self.run()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.running = True  # Garante que o menu sempre reabra corretamente
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

    def adivinhar(self, letra):
        if letra in self.linguagem and letra not in self.escrita_certas:
            self.escrita_certas.append(letra)
        elif letra not in self.linguagem and letra not in self.escrita_erradas:
            self.escrita_erradas.append(letra)
        else:
            return False
        return True

    def forca_acima(self):
        return self.forca_vencida() or (len(self.escrita_erradas) == 6)

    def forca_vencida(self):
        return '_' not in self.ocultar_palavra()

    def ocultar_palavra(self):
        return ''.join([i if i in self.escrita_certas else '_' for i in self.linguagem])

    def imprimir_status_do_jogo(self):
        print(base[len(self.escrita_erradas)])
        print('\nPalavra: ' + self.ocultar_palavra())
        print('\nLetras erradas: ', ' '.join(self.escrita_erradas))
        print('Letras corretas: ', ' '.join(self.escrita_certas))
        print()

    @staticmethod
    def palavra_aleatoria():
        with open("Palavras.txt", "rt", encoding="utf-8") as f:
            banco = [linha.strip() for linha in f if linha.strip()]
        return random.choice(banco)

    @staticmethod
    def forca_principal():
        game = Jogo(Jogo.palavra_aleatoria())
        while not game.forca_acima():
            game.imprimir_status_do_jogo()
            entrada_usuario = input('\nDigite uma letra: ').strip().lower()
            game.adivinhar(entrada_usuario)
        game.imprimir_status_do_jogo()
        if game.forca_vencida():
            print('\nParabéns! Você venceu :)')
        else:
            print('Fim de jogo! Você perdeu :(')
            print('A palavra era: ' + game.linguagem)
        input("\nPressione ENTER para voltar ao menu...")  # <- pausa antes de retornar

# ----------------- Execução -----------------
if __name__ == "__main__":
    Game().run()
