# Importo o pygame pra parte gráfica e o math pra usar a função seno no efeito pulsante.
import pygame
import math
from code.const import (
    FPS, TITLE_FONT_SIZE, SMALL_FONT_SIZE,
    MENU_LINE_LEFT_X, MENU_LINE_RIGHT_X, MENU_LINE_TOP_Y, MENU_LINE_BOTTOM_Y,
    MENU_TITLE_POS, MENU_SUBTITLE_POS, MENU_START_POS, MENU_CONTROLS_POS,
    COLOR_GOLD, COLOR_MENU_BG, COLOR_MENU_SUBTITLE, COLOR_MENU_CONTROLS
)

# Essa é a classe do menu inicial. Eu criei ela separada pra deixar o código mais organizado.
class Menu:

    # No construtor eu recebo a tela e a fonte padrão que já foram criadas na classe Game.
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        # Crio uma fonte maior pro título ficar destacado.
        self.title_font = pygame.font.SysFont(None, TITLE_FONT_SIZE)

        # E uma fonte menor pros textos secundários, como subtítulo e controles.
        self.small_font = pygame.font.SysFont(None, SMALL_FONT_SIZE)

        # Uso o Clock pra controlar o FPS do menu também.
        self.clock = pygame.time.Clock()

    # Esse é o método principal do menu. Ele fica em loop até o jogador apertar ENTER.
    def run(self):

        while True:

            # Limito a 60 FPS pra não consumir processamento desnecessário.
            self.clock.tick(FPS)

            # Pego o tempo em milissegundos desde que o pygame iniciou. Uso isso pro efeito pulsante.
            ticks = pygame.time.get_ticks()

            # Preencho a tela com um azul bem escuro pra dar um visual mais bonito.
            self.screen.fill(COLOR_MENU_BG)

            # Desenho uma linha dourada decorativa acima do título.
            pygame.draw.line(self.screen, COLOR_GOLD, (MENU_LINE_LEFT_X, MENU_LINE_TOP_Y), (MENU_LINE_RIGHT_X, MENU_LINE_TOP_Y), 2)

            # Renderizo o título do jogo com cor dourada e centralizo na tela.
            title = self.title_font.render("SURVIVOR RUSH", True, COLOR_GOLD)
            title_rect = title.get_rect(center=MENU_TITLE_POS)
            self.screen.blit(title, title_rect)

            # Coloco um subtítulo explicando o objetivo do jogo, com cor mais discreta.
            subtitle = self.small_font.render("Desvie dos inimigos e sobreviva!", True, COLOR_MENU_SUBTITLE)
            sub_rect = subtitle.get_rect(center=MENU_SUBTITLE_POS)
            self.screen.blit(subtitle, sub_rect)

            # Outra linha dourada embaixo do subtítulo, pra fechar o visual.
            pygame.draw.line(self.screen, COLOR_GOLD, (MENU_LINE_LEFT_X, MENU_LINE_BOTTOM_Y), (MENU_LINE_RIGHT_X, MENU_LINE_BOTTOM_Y), 2)

            # Aqui eu fiz um efeito pulsante usando math.sin(). O brilho varia entre 200 e 255,
            # então o texto do botão fica "piscando" suavemente pra chamar atenção.
            pulse = int(200 + 55 * math.sin(ticks / 300))
            start = self.font.render("[ ENTER - Jogar ]", True, (pulse, pulse, 255))
            start_rect = start.get_rect(center=MENU_START_POS)
            self.screen.blit(start, start_rect)

            # Mostro os controles do jogo numa cor bem discreta na parte de baixo.
            controls = self.small_font.render("A / D  ou  SETAS  para mover", True, COLOR_MENU_CONTROLS)
            ctrl_rect = controls.get_rect(center=MENU_CONTROLS_POS)
            self.screen.blit(controls, ctrl_rect)

            # Atualizo a tela pra mostrar tudo que desenhei nesse frame.
            pygame.display.update()

            # Verifico os eventos pra saber se o jogador fez alguma ação.
            for event in pygame.event.get():

                # Se fechou a janela, encerro o jogo.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # Se apertou uma tecla, verifico qual foi.
                if event.type == pygame.KEYDOWN:
                    # Se foi ENTER, saio do menu e o jogo começa. O return encerra esse método.
                    if event.key == pygame.K_RETURN:
                        return
