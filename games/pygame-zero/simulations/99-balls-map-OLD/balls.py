# biblioteca adicional para o comando seguinte
import os

map = input("which map do you want? (press ENTER to load map001.json)")
if not map:
    map = "map001.json"

# encontrar a pasta na qual este programa está executando
from pathlib import Path

# Returns a Path object of the script's directory
caminho = Path(__file__).parent.resolve()

# adicionar o caminho ao mapa
map = os.path.join(caminho, map)

# comando para centralizar a janela
os.environ['SDL_VIDEO_CENTERED'] = '1'

import math
import random
import pgzrun
import json

WIDTH = 1000
HEIGHT = 700

GRAVITY = 0.35
BOUNCE = 0.15
FRICTION = 0.995

PLATFORM_THICKNESS = 16

balls = []
spawn_timer = 0

with open(map) as f:
    platforms = json.load(f)


def spawn_ball():
    balls.append({
        "x": random.randint(20, WIDTH - 20),
        "y": -20,
        "vx": random.uniform(-1, 1),
        "vy": 0,
        "r": random.randint(8, 15),
        "color": (
            random.randint(80, 255),
            random.randint(80, 255),
            random.randint(80, 255),
        )
    })


def closest_point(px, py, ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay
    length2 = dx * dx + dy * dy

    if length2 == 0:
        return ax, ay

    t = ((px - ax) * dx + (py - ay) * dy) / length2
    t = max(0, min(1, t))

    return ax + dx * t, ay + dy * t


def update():
    global spawn_timer

    spawn_timer += 1

    # Spawn a new ball every 8 frames
    if spawn_timer >= 8:
        spawn_ball()
        spawn_timer = 0

    # Keep at most 120 balls
    if len(balls) > 120:
        balls.pop(0)

    for ball in balls:

        ball["vy"] += GRAVITY
        ball["x"] += ball["vx"]
        ball["y"] += ball["vy"]

        collided = False

        for e in platforms:

            x1 = e["x1"]
            y1 = e["y1"]
            x2 = e["x2"]
            y2 = e["y2"]

            cx, cy = closest_point(ball["x"], ball["y"], x1, y1, x2, y2)

            dx = ball["x"] - cx
            dy = ball["y"] - cy
            dist = math.hypot(dx, dy)

            if dist < ball["r"] + PLATFORM_THICKNESS / 2:

                if dist == 0:
                    nx, ny = 0, -1
                else:
                    nx = dx / dist
                    ny = dy / dist

                overlap = ball["r"] + PLATFORM_THICKNESS / 2 - dist

                ball["x"] += nx * overlap
                ball["y"] += ny * overlap

                tx = x2 - x1
                ty = y2 - y1

                length = math.hypot(tx, ty)
                tx /= length
                ty /= length

                speed = ball["vx"] * tx + ball["vy"] * ty
                speed += GRAVITY * ty

                ball["vx"] = tx * speed
                ball["vy"] = ty * speed

                ball["vx"] -= nx * BOUNCE
                ball["vy"] -= ny * BOUNCE

                collided = True

        if not collided:
            ball["vx"] *= FRICTION

        # Bounce off walls
        if ball["x"] < ball["r"]:
            ball["x"] = ball["r"]
            ball["vx"] *= -0.7

        if ball["x"] > WIDTH - ball["r"]:
            ball["x"] = WIDTH - ball["r"]
            ball["vx"] *= -0.7

        # Remove balls that fall off the screen
        if ball["y"] > HEIGHT + 50:
            ball["y"] = HEIGHT + 100


def draw():
    screen.fill((25, 25, 35))

    # Draw platforms
    for p in platforms:
        x1 = p["x1"]
        y1 = p["y1"]
        x2 = p["x2"]
        y2 = p["y2"]

        for i in range(-PLATFORM_THICKNESS // 2, PLATFORM_THICKNESS // 2 + 1):
            screen.draw.line((x1,y1+i), (x2, y2+i), (220, 220, 255))

    # Draw balls
    for ball in balls:
        screen.draw.filled_circle(
            (int(ball["x"]), int(ball["y"])),
            ball["r"],
            ball["color"]
        )

    screen.draw.text(
        f"Balls: {len(balls)}",
        (10, 10),
        color="white",
        fontsize=30
    )

pgzrun.go()