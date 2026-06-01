import pgzrun

ball = Actor('bola.jpg')
ball.pos = 100, 56

wall = Actor('wall.jpeg')
wall.pos = 400, 300

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    ball.draw()
    wall.draw()

def update():
    if not ball.colliderect(wall):
        ball.left += 1
        ball.top += 0.5        

pgzrun.go()