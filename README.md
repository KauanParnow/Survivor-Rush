# 🎮 Survivor Rush

Um jogo de sobrevivência feito com **Python** e **Pygame**. O objetivo é desviar dos inimigos que caem do topo da tela e sobreviver por 30 segundos para vencer!

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)

---

## 📸 Como funciona

- Inimigos caem do topo da tela em posições e velocidades aleatórias
- O jogador se move para a esquerda e direita para desviar
- Se um inimigo encostar no jogador, é **Game Over**
- Se sobreviver **30 segundos**, você vence!

---

## 🕹️ Controles

| Ação           | Teclas                     |
|----------------|----------------------------|
| Mover esquerda | `A` ou `←` (seta esquerda) |
| Mover direita  | `D` ou `→` (seta direita)  |
| Iniciar jogo   | `ENTER`                    |
| Jogar novamente| `ENTER` (na tela final)    |
| Sair do jogo   | `ESC` (na tela final)      |

---

## 📁 Estrutura do Projeto

```
Survivor Rush/
├── main.py              # Arquivo principal - inicia o jogo
├── code/
│   ├── __init__.py      # Torna a pasta um pacote Python
│   ├── const.py         # Constantes centralizadas (tela, cores, velocidades, etc.)
│   ├── game.py          # Classe Game - lógica principal e game loop
│   ├── player.py        # Classe Player - movimentação do jogador
│   ├── enemy.py         # Classe Enemy - inimigos que caem do topo
│   └── menu.py          # Classe Menu - tela inicial do jogo
├── asset/
│   ├── images/
│   │   ├── background.png
│   │   ├── player.png
│   │   └── enemy.png
│   └── sounds/
│       ├── background_music.mp3
│       └── hit.mp3
├── requirements.txt
└── README.md
```

---

## 🚀 Como Rodar

### Pré-requisitos

- Python 3.x instalado
- Pygame instalado

### Instalação

1. Clone o repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/survivor-rush.git
   cd survivor-rush
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o jogo:
   ```bash
   python main.py
   ```

---

## ⚙️ Configurações

Todas as constantes do jogo ficam centralizadas no arquivo `code/const.py`. Se quiser ajustar algo, basta alterar lá:

| Constante           | Valor Padrão | Descrição                          |
|----------------------|-------------|------------------------------------|
| `SCREEN_WIDTH`       | 800         | Largura da janela                  |
| `SCREEN_HEIGHT`      | 600         | Altura da janela                   |
| `FPS`                | 60          | Frames por segundo                 |
| `PLAYER_SPEED`       | 7           | Velocidade do jogador              |
| `ENEMY_SPEED_MIN`    | 4           | Velocidade mínima dos inimigos     |
| `ENEMY_SPEED_MAX`    | 7           | Velocidade máxima dos inimigos     |
| `ENEMY_SPAWN_CHANCE` | 30          | Chance de spawn (1 em N por frame) |
| `VICTORY_TIME`       | 30          | Segundos para vencer               |
| `MUSIC_VOLUME`       | 0.5         | Volume da música (0.0 a 1.0)      |

---

## 🛠️ Tecnologias

- **Python 3** — Linguagem de programação
- **Pygame** — Biblioteca para desenvolvimento de jogos 2D

---

## 📝 Licença

Este projeto foi desenvolvido para fins de trabalho.
