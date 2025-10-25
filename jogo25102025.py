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
RED = (220, 20, 60)
GREEN = (50, 205, 50)

pygame.init()
pygame.display.set_caption("Menu Inicial - Jogo da Forca")
FONT = pygame.font.SysFont(None, 48)
SMALL_FONT = pygame.font.SysFont(None, 36)

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
            Button("Sair", (mid_x, start_y + gap), self.exit_game),
        ]
        self.running = True

    def start_game(self):
        print("\nIniciando jogo da forca...")
        self.running = False
        Jogo.forca_principal(self.screen)
        self.run()

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.running = True
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

# ----------------- Jogo da Forca -----------------
base = ['''
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
/|\\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
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

    def imprimir_status_do_jogo(self, screen):
        screen.fill(BLACK)

        # Palavra oculta
        palavra_render = FONT.render(" ".join(self.ocultar_palavra()), True, WHITE)
        screen.blit(palavra_render, (SCREEN_WIDTH // 2 - palavra_render.get_width() // 2, 400))

        # Letras erradas
        erradas_text = SMALL_FONT.render("Erros: " + " ".join(self.escrita_erradas), True, RED)
        screen.blit(erradas_text, (50, 500))

        # Desenhar boneco da forca
        self.desenhar_forca(screen, len(self.escrita_erradas))

        pygame.display.flip()

    def desenhar_forca(self, screen, erros):
        # Desenhar estrutura da forca
        pygame.draw.line(screen, WHITE, (150, 500), (350, 500), 5)
        pygame.draw.line(screen, WHITE, (250, 500), (250, 150), 5)
        pygame.draw.line(screen, WHITE, (250, 150), (400, 150), 5)
        pygame.draw.line(screen, WHITE, (400, 150), (400, 200), 5)

        # Desenhar boneco conforme erros
        if erros > 0:  # cabeça
            pygame.draw.circle(screen, WHITE, (400, 230), 30, 5)
        if erros > 1:  # corpo
            pygame.draw.line(screen, WHITE, (400, 260), (400, 350), 5)
        if erros > 2:  # braço esquerdo
            pygame.draw.line(screen, WHITE, (400, 280), (370, 320), 5)
        if erros > 3:  # braço direito
            pygame.draw.line(screen, WHITE, (400, 280), (430, 320), 5)
        if erros > 4:  # perna esquerda
            pygame.draw.line(screen, WHITE, (400, 350), (370, 400), 5)
        if erros > 5:  # perna direita
            pygame.draw.line(screen, WHITE, (400, 350), (430, 400), 5)

    @staticmethod
    def palavra_aleatoria():
        with open("Palavras.txt", "rt", encoding="utf-8") as f:
            banco = [linha.strip() for linha in f if linha.strip()]
        return random.choice(banco)

    @staticmethod
    def forca_principal(screen):
        clock = pygame.time.Clock()
        game = Jogo(Jogo.palavra_aleatoria())
        input_letra = ""
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and input_letra:
                        game.adivinhar(input_letra.lower())
                        input_letra = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_letra = input_letra[:-1]
                    elif event.unicode.isalpha():
                        input_letra += event.unicode.lower()

            game.imprimir_status_do_jogo(screen)

            # Mostra letra digitada
            letra_txt = SMALL_FONT.render(f"Digite uma letra: {input_letra}", True, WHITE)
            screen.blit(letra_txt, (50, 50))

            # Verifica vitória ou derrota
            if game.forca_vencida():
                msg = FONT.render("Parabéns! Você venceu :)", True, GREEN)
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, 300))
                pygame.display.flip()
                pygame.time.delay(2500)
                running = False
            elif len(game.escrita_erradas) >= 6:
                msg = FONT.render("Fim de jogo! Você perdeu :(", True, RED)
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, 300))
                palavra_txt = SMALL_FONT.render(f"A palavra era: {game.linguagem}", True, WHITE)
                screen.blit(palavra_txt, (SCREEN_WIDTH // 2 - palavra_txt.get_width() // 2, 350))
                pygame.display.flip()
                pygame.time.delay(3000)
                running = False

            pygame.display.flip()
            clock.tick(FPS)

# ----------------- Execução -----------------
if __name__ == "__main__":
    Game().run()