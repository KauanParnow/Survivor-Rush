# Importo o pygame para a parte gráfica e o random para gerar valores aleatórios.
import pygame
import random

# Essa é a classe do inimigo. Cada inimigo que aparece no jogo é um objeto dessa classe.
class Enemy:

    # No construtor, eu recebo a largura da tela pra saber onde o inimigo pode aparecer.
    def __init__(self, screen_width):

        # Carrego a imagem do inimigo da pasta de assets.
        self.image = pygame.image.load("asset/images/enemy.png")

        # Redimensiono pra 60x60, mesmo tamanho do jogador.
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Crio o retângulo pra controlar a posição e detectar colisão.
        self.rect = self.image.get_rect()

        # A posição X é aleatória, assim cada inimigo aparece em um lugar diferente da tela.
        self.rect.x = random.randint(0, screen_width - self.rect.width)

        # Começo com Y negativo pra ele nascer fora da tela e ir descendo aos poucos.
        self.rect.y = -self.rect.height

        # A velocidade é aleatória entre 4 e 7, então cada inimigo desce num ritmo diferente.
        self.speed = random.randint(4, 7)

    # Esse método move o inimigo pra baixo, somando a velocidade no eixo Y.
    def move(self):
        self.rect.y += self.speed

    # Desenha o inimigo na tela usando blit().
    def draw(self, screen):
        screen.blit(self.image, self.rect)
