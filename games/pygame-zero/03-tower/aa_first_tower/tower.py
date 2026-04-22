import pgzrun

# referência:
# https://pygame-zero.readthedocs.io/en/stable/introduction.html

# sorteia a força de cada inimigo
import random
forca1 = random.randint(1, 5)
forca2 = random.randint(1, 5)

# criando inimigos do lado esquerdo e do lado direito
enemies_left = [Actor('ball'+str(forca1))]
enemies_right = [Actor('ball'+str(forca2))]

# posicionando os inimigos
enemies_left[0].pos = 50, 156
enemies_right[0].pos = 1450, 156

# define a força nos inimigos
enemies_left[0].strength = forca1
enemies_right[0].strength = forca2

# definindo o tamanho da tela
WIDTH = 1500 # largura
HEIGHT = 800 # altura

# pontuações do lado esquerdo e direito
score_left = 0
score_right = 0

#  função para desenhar a tela
def draw():
    # limpando a tela
    screen.clear()
    # desenhando os inimigos
    for enemy in enemies_left:
        enemy.draw()
    for enemy in enemies_right:
        enemy.draw()
    
    # desenha a pontuação
    screen.draw.text(f'Score Left: {score_left}', (10, 10), color='white')
    screen.draw.text(f'Score Right: {score_right}', (WIDTH - 150, 10), color='white')
    screen.draw.text(f'Height L: {enemies_left[0].height}', (10, 50), color='yellow')
    screen.draw.text(f'Height R: {enemies_right[0].height}', (WIDTH - 150, 50), color='yellow')


# função que atualiza a tela,
# executada a cada frame (60 vezes por segundo)
def update():
    # avança o inimigo do lado esquerdo
    enemies_left[0].left += 1

    # avança o inimigo do lado direito
    enemies_right[0].left -= 1
    
    # se os inimigos se encontrarem...
    if enemies_left[0].colliderect(enemies_right[0]):
        
        global score_left, score_right

        # se o inimigo do lado esquerdo for mais fraco
        if enemies_left[0].strength < enemies_right[0].strength:
            # o inimigo do lado direito perde força proporcional à diferença de forças
            enemies_right[0].strength -= enemies_right[0].strength - enemies_left[0].strength
            # atualiza o desenho do inimigo do lado direito
            enemies_right[0].image = 'ball'+str(enemies_right[0].strength)

            # o inimigo do lado esquerdo volta pro começo
            enemies_left[0].right = 0
            # sorteia uma nova força para o inimigo do lado esquerdo
            enemies_left[0].strength = random.randint(1, 5)
            # atualiza o desenho do inimigo do lado esquerdo
            enemies_left[0].image = 'ball'+str(enemies_left[0].strength)
        else:
            # o inimigo do lado esquerdo perde força proporcional à diferença de forças
            enemies_left[0].strength -= enemies_left[0].strength - enemies_right[0].strength
            # atualiza o desenho do inimigo do lado esquerdo
            enemies_left[0].image = 'ball'+str(enemies_left[0].strength)

            # o inimigo do lado direito volta pro começo
            enemies_right[0].left = WIDTH
            # sorteia uma nova força para o inimigo do lado direito
            enemies_right[0].strength = random.randint(1, 5)
            # atualiza o desenho do inimigo do lado direito
            enemies_right[0].image = 'ball'+str(enemies_right[0].strength)
            
    

pgzrun.go()