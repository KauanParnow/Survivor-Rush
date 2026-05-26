# Importações que eu preciso pra rodar o jogo
import pygame       # Biblioteca principal do jogo
import random       # Pra gerar números aleatórios no spawn dos inimigos
import sys          # Pra encerrar o programa com sys.exit()

# Importo as classes que eu criei nos outros arquivos
from code.player import Player
from code.enemy import Enemy
from code.menu import Menu
from code.const import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONT_SIZE, SMALL_FONT_SIZE,
    VICTORY_TIME, ENEMY_SPAWN_CHANCE, MUSIC_VOLUME,
    COLOR_WHITE, COLOR_BLACK, COLOR_RED, COLOR_GREEN, COLOR_HINT
)

# Essa é a classe principal do jogo. É aqui que tudo é controlado.
class Game:

    # No construtor eu configuro tudo que o jogo precisa pra funcionar.
    def __init__(self):

        # Inicio todos os módulos do pygame (vídeo, áudio, etc.)
        pygame.init()

        # Defino o tamanho da janela usando as constantes do settings.
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        # Crio a janela do jogo com essas dimensões.
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Coloco o título na barra da janela.
        pygame.display.set_caption("Survivor Rush")

        # O Clock eu uso pra controlar a velocidade do jogo em 60 FPS.
        self.clock = pygame.time.Clock()
        self.fps = FPS

        # Crio duas fontes: uma principal e uma menor pra textos secundários.
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.small_font = pygame.font.SysFont(None, SMALL_FONT_SIZE)

        # Carrego a imagem de fundo e redimensiono pro tamanho da tela.
        self.background = pygame.image.load("asset/images/background.png")
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Carrego o som de quando o jogador é atingido por um inimigo.
        self.hit_sound = pygame.mixer.Sound("asset/sounds/hit.mp3")

        # Carrego a música de fundo e coloco pra tocar em loop infinito (-1).
        # O set_volume() controla o volume (0.0 a 1.0). Deixei em 0.5 pra não ficar alto demais.
        pygame.mixer.music.load("asset/sounds/background_music.mp3")
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play(-1)

        # O jogador precisa sobreviver 30 segundos pra vencer.
        self.victory_time = VICTORY_TIME

        # A cada frame, tem 1 chance em 30 de aparecer um inimigo novo.
        self.enemy_spawn_chance = ENEMY_SPAWN_CHANCE

        # Chamo o reset() pra inicializar as variáveis do jogo.
        self.reset()

    # Esse método reinicia o estado do jogo. Uso ele no início e quando o jogador quer jogar de novo.
    def reset(self):
        # Crio um novo jogador centralizado na tela.
        self.player = Player(self.width, self.height)

        # Limpo a lista de inimigos.
        self.enemies = []

        # Marco o tempo de início pra calcular quanto tempo passou.
        self.start_time = pygame.time.get_ticks()

        # Reseto as flags de estado: ninguém perdeu nem venceu ainda.
        self.game_over = False
        self.victory = False

    # Esse método tenta criar um inimigo novo. Ele é chamado todo frame.
    def spawn_enemy(self):

        # Gero um número aleatório e, se der 1, crio um inimigo.
        # Quanto menor o enemy_spawn_chance, mais inimigos aparecem.
        if random.randint(1, self.enemy_spawn_chance) == 1:
            self.enemies.append(Enemy(self.width))

    # Aqui eu atualizo todos os inimigos: movo eles e verifico se houve colisão.
    def update_enemies(self):

        for enemy in self.enemies:
            # Movo cada inimigo pra baixo.
            enemy.move()

            # Uso colliderect() pra verificar se o jogador encostou no inimigo.
            # Se os retângulos se sobrepõem, significa que houve colisão.
            if self.player.rect.colliderect(enemy.rect):
                self.hit_sound.play()    # Toco o som de colisão
                self.game_over = True    # Marco que o jogo acabou

        # Removo os inimigos que já saíram da tela pra não ficar ocupando memória à toa.
        # Uso list comprehension: só mantenho os que ainda estão visíveis.
        self.enemies = [e for e in self.enemies if e.rect.y < self.height]

    # Retorna quantos segundos se passaram desde o início da partida.
    def get_elapsed_time(self):
        return (pygame.time.get_ticks() - self.start_time) / 1000

    # Esse método desenha tudo na tela: fundo, jogador, inimigos e o cronômetro.
    def draw(self):

        # Primeiro desenho o fundo, que cobre tudo que tinha antes.
        self.screen.blit(self.background, (0, 0))

        # Desenho o jogador.
        self.player.draw(self.screen)

        # Desenho cada inimigo da lista.
        for enemy in self.enemies:
            enemy.draw(self.screen)

        # Mostro o cronômetro no canto superior esquerdo.
        time_now = self.get_elapsed_time()
        timer = self.font.render(f"Tempo: {int(time_now)}s", True, COLOR_WHITE)
        self.screen.blit(timer, (10, 10))

        # Atualizo a tela pra exibir tudo que desenhei.
        pygame.display.update()

    # Verifico se o jogador já sobreviveu tempo suficiente pra vencer.
    def check_victory(self):

        if self.get_elapsed_time() >= self.victory_time:
            self.victory = True

    # Essa é a tela final, que aparece tanto na vitória quanto na derrota.
    # Recebe o texto e a cor pra eu poder reutilizar nos dois casos.
    def final_screen(self, text, color):

        # Preencho a tela com preto.
        self.screen.fill(COLOR_BLACK)

        # Renderizo a mensagem principal (tipo "GAME OVER" ou "VOCE VENCEU!") e centralizo.
        msg = self.font.render(text, True, color)
        msg_rect = msg.get_rect(center=(self.width // 2, self.height // 2 - 30))
        self.screen.blit(msg, msg_rect)

        # Mostro as opções pro jogador: ENTER pra jogar de novo ou ESC pra sair.
        hint = self.small_font.render("ENTER - Jogar novamente  |  ESC - Sair", True, COLOR_HINT)
        hint_rect = hint.get_rect(center=(self.width // 2, self.height // 2 + 30))
        self.screen.blit(hint, hint_rect)

        pygame.display.update()

        # Fico num loop esperando o jogador decidir o que fazer.
        while True:
            for event in pygame.event.get():

                # Se fechar a janela, encerro tudo.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    # Se apertar ENTER, retorno True pro jogo reiniciar.
                    if event.key == pygame.K_RETURN:
                        return True
                    # Se apertar ESC, encerro o jogo.
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    # Esse é o método principal que roda o jogo inteiro.
    def run(self):

        # Primeiro mostro o menu inicial e espero o jogador apertar ENTER.
        menu = Menu(self.screen, self.font)
        menu.run()

        # Esse é o game loop. Ele roda continuamente enquanto o jogo estiver aberto.
        while True:

            # Limito a 60 FPS pra manter a velocidade constante.
            self.clock.tick(self.fps)

            # Processo os eventos do pygame (fechar janela, teclas, etc.)
            for event in pygame.event.get():

                # Se o jogador fechar a janela, encerro o jogo.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Atualizo a posição do jogador com base nas teclas pressionadas.
            self.player.move()

            # Tento criar novos inimigos.
            self.spawn_enemy()

            # Movo os inimigos e verifico colisões.
            self.update_enemies()

            # Verifico se o tempo de vitória foi atingido.
            self.check_victory()

            # Desenho tudo na tela.
            self.draw()

            # Se o jogador perdeu, mostro a tela de Game Over.
            # Se ele apertar ENTER, o reset() reinicia tudo.
            if self.game_over:
                if self.final_screen("GAME OVER", COLOR_RED):
                    self.reset()

            # Se o jogador venceu, mostro a tela de vitória.
            if self.victory:
                if self.final_screen("VOCE VENCEU!", COLOR_GREEN):
                    self.reset()
