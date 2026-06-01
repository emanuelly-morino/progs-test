import pgzrun
from random import randint

apple = Actor('apple')

# placar
score = 0

# duração do jogo
game_time = 10

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text(f'Score: {score}', (10, 10), color='white')
    screen.draw.text(f'Time: {game_time}', (10, 30), color='white')
    
def place_apple():
    apple.x = randint(0, 800)
    apple.y = randint(0, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global score
        score += 1

def decrease_time():
    global game_time
    game_time -= 1

def exit_game():
    print("Fim de jogo! Seu placar: ", score)
    exit()

# alterar o local da maçã a cada segundo
clock.schedule_interval(place_apple, 1.0)   
# diminuir o tempo a cada segundo
clock.schedule_interval(decrease_time, 1.0)   
# sair do jogo quando o tempo acabar
clock.schedule_unique(exit_game, game_time)

pgzrun.go()