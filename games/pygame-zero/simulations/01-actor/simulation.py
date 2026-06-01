# importar o módulo pgzrun para rodar o jogo
import pgzrun

# criar um "ator"
quad = Actor('quadrado2.png')
# definir posição do ator (x, y)
quad.pos = 300, 56

# criar uma "base"
base = Actor('base.png')
# definir a posição da base
base.pos = 400, 300

# definir largura e altura da janela
WIDTH = 800
HEIGHT = 600

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.clear()
    # desenhar os atores
    quad.draw()
    base.draw()

# método que vai atualizar a posição dos atores
def update():
    # se o ator NÃO colidiu com a base...
    if not quad.colliderect(base):
        # o ator continua "caindo"
        quad.top += 1        

# executar o jogo
pgzrun.go()