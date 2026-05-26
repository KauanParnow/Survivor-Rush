# Este é o arquivo principal do meu jogo, professor. É por aqui que tudo começa.
# Aqui eu importo a classe Game, que é onde toda a lógica do jogo está organizada.
from code.game import Game

# Crio um objeto do tipo Game, que já inicializa o pygame e configura a janela.
game = Game()

# Chamo o método run() para rodar o jogo. A partir daqui, o game loop assume o controle.
game.run()
