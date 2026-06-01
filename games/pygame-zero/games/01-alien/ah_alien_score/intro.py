import pgzrun

# referência:
# https://pygame-zero.readthedocs.io/en/stable/introduction.html

# criando uma figura para colocar na tela
alien = Actor('alien')
# posicionando a figura (x, y)
alien.pos = 100, 56

# definindo o tamanho da tela
WIDTH = 500
# definindo a altura da tela:
# altura da figura + um espaço extra
HEIGHT = alien.height + 20

# variável para guardar a pontuação
score = 0

# função para desenhar a tela
def draw():
    # limpando a tela
    screen.clear()
    # desenhando a figura
    alien.draw()
    # desenha a pontuação
    # não precisa usar 'global' para ler variável global
    screen.draw.text(f'Score: {score}', (10, 10), color='white')


# função que atualiza a tela,
# executada a cada frame (60 vezes por segundo)
def update():
    # move a figura para a direita
    alien.left += 2
    # se a figura sair da tela...
    if alien.left > WIDTH:
        # ...volta para o início
        alien.right = 0
    
# função para detectar cliques do mouse
def on_mouse_down(pos):
    # se o mouse for clicado bem 
    # na posição do alien...
    if alien.collidepoint(pos):
        # ... coloca imagem do alien triste
        set_alien_hurt()

# função para colocar o alien triste
def set_alien_hurt():
    # informa que vai atualizar variável global
    global score
    # atualiza a pontuação
    score += 1
    # muda a imagem do alien
    alien.image = 'alien_hurt'
    # toca som de dor 
    sounds.eep.play()
    # depois de um tempo, 
    # volta para a imagem do alien normal
    clock.schedule_unique(set_alien_normal, 0.1)

# função para colocar o alien normal
def set_alien_normal():
    # volta para a imagem do alien normal
    alien.image = 'alien'

pgzrun.go()