# Aqui eu importo o pygame, que é a biblioteca que usei para fazer o jogo.
import pygame
from code.const import PLAYER_SIZE, PLAYER_SPEED, PLAYER_OFFSET_Y

# Essa é a classe do jogador. Eu separei em uma classe própria para ficar mais organizado.
class Player:

    # Esse é o construtor. Ele recebe a largura e altura da tela para eu poder posicionar o jogador certo.
    def __init__(self, screen_width, screen_height):

        # Carrego a imagem do jogador que eu coloquei na pasta asset/images.
        self.image = pygame.image.load("asset/images/player.png")

        # Redimensiono a imagem para 60x60 pixels, que é o tamanho que achei bom pro jogo.
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))

        # Uso o get_rect() para criar um retângulo baseado na imagem. Esse rect eu uso pra posição e colisão.
        self.rect = self.image.get_rect()

        # Coloco o jogador no centro horizontal da tela usando divisão inteira.
        self.rect.centerx = screen_width // 2

        # Posiciono ele perto da parte de baixo da tela, com uma margem de 100 pixels.
        self.rect.y = screen_height - PLAYER_OFFSET_Y

        # Defino a velocidade de movimento usando a constante do settings.
        self.speed = PLAYER_SPEED

        # Guardo a largura da tela pra usar depois no limite de movimento.
        self.screen_width = screen_width

    # Esse método cuida da movimentação. Ele é chamado todo frame no game loop.
    def move(self):

        # Pego todas as teclas que estão pressionadas no momento.
        keys = pygame.key.get_pressed()

        # Se o jogador apertar seta esquerda ou a tecla A, eu movo pra esquerda.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed

        # Se apertar seta direita ou D, movo pra direita.
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed

        # Aqui eu trato os limites da tela. Se o jogador tentar sair pela esquerda, eu trava ele na borda.
        if self.rect.left < 0:
            self.rect.left = 0

        # Mesma coisa pro lado direito.
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    # Esse método desenha o jogador na tela. O blit() "cola" a imagem na posição do rect.
    def draw(self, screen):
        screen.blit(self.image, self.rect)
