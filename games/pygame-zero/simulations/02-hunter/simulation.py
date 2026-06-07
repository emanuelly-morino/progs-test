# importar o módulo pgzrun para rodar o jogo
import pgzrun
from random import randint
import pygame

# definir largura e altura da janela
WIDTH = 1200
HEIGHT = 800

# criar um caçador
quad = Actor('cacador.png')
# definir posição do caçador (x, y)
quad.pos = 300, 200

# velocidade inicial do caçador
quad.vx = 0
quad.vy = 0

# definir a "passada" do caçador
passo_cacador = 3

# definir uma lista de alvos
alvos = []

# cria alguns alvos em posições aleatórias
for i in range(3):
    # criar um novo alvo
    ob = Actor('obstaculo2.png')
    # definir posição aleatória do alvo
    ob.pos = (randint(0, WIDTH), randint(0, HEIGHT))
    # adicionar o alvo na lista
    alvos.append(ob)

# método que vai desenhar os atores na tela
def draw():
    # limpar a tela
    screen.clear()
    # preencher o fundo com a cor verde escuro
    screen.fill((0, 100, 0))
    # desenhar os atores
    quad.draw()
    # desenhar os alvos
    for i in range(len(alvos)):
        # "pega" o alvo atual
        alvo = alvos[i]
        # desenha o alvo
        alvo.draw()
        # se for o primeiro alvo...
        if i == 0:
            # ... desenha um círculo vermelho ao redor dele
            screen.draw.circle(alvo.pos, 40, (255, 0, 0))

# método de atualização da tela
def update():

    # se houver algum alvo
    if alvos:
        # pegar o primeiro alvo da lista
        alvo = alvos[0]

        # se o caçador está "longe" do alvo em relação à "X"
        if abs(quad.x - alvo.x) > 10:
            # pára o caçador verticalmente
            quad.vy = 0            
            # se o caçador está à direita do alvo
            if quad.x > alvo.x:
                # o caçador vai ter uma velocidade "para a esquerda"
                quad.vx = -passo_cacador
            else:
                # o caçador vai se mover em breve para a direita
                quad.vx = passo_cacador
        else:
            # pára o movimento em X, pois ele está "alinhado" com o alvo em "X"
            quad.vx = 0
            # o caçador está abaixo do alvo?
            if quad.y > alvo.y:
                # o caçador vai subir em breve
                quad.vy = -passo_cacador
            else:
                # o caçador vai descer em breve
                quad.vy = passo_cacador
            
    # movimentar o ator de acordo com as velocidades atuais deles
    quad.x += quad.vx
    quad.y += quad.vy

    # percorre os alvos...
    for alvo in alvos:
        # se o caçador colidiu com algum alvo...
        if quad.colliderect(alvo):
            # remove o alvo da lista
            alvos.remove(alvo)  
            # manda o caçador ficar parado, 
            # pois este poderia ser o último alvo
            # se precisar começar a andar de novo, ele irá
            # com a outra lógica de movimentação que está mais acima
            quad.vx = 0
            quad.vy = 0 

    # pegar a posição do mouse
    x, y = pygame.mouse.get_pos()
    
    # retornar o estado dos botões (left_click, middle_click, right_click)
    botoes = pygame.mouse.get_pressed()
    
    # verifica se o botão esquero está apertado
    if botoes[0]: 
        # cria um alvo ali na posição do mouse
        ob = Actor('obstaculo2.png')
        ob.pos = (x,y)
        # adiciona o alvo na lista de alvos
        alvos.append(ob)
        
# executar o jogo
pgzrun.go()

'''

Ao clicar na tela, novos alvos surgirão na posição do mouse

EXERCÍCIOS:

a) trocar as imagens (por exemplo, pode usar o tema do PacMan)
b) aumentar a velocidade do caçador
c) mudar a busca do caçador: em vez de pegar o "primeiro" alvo da lista, ele
deverá pegar o "último"
d) em vez de pegar o primeiro ou o último alvo da lista, pegar o alvo que estiver mais perto dele :-)

PESQUISE NA internet para descobrir como fazer este exercício abaixo:

e) mudar a imagem do caçador dependendo do lado para o qual ele está indo
'''