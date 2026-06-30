import os
import json
import math
import random
from pathlib import Path

# --------------------------------------------------
# Choose the map
# --------------------------------------------------

map_file = input("Which map do you want? (Press ENTER to load map001.json): ")

if not map_file:
    map_file = "map001.json"

# Folder where this script is located
script_path = Path(__file__).parent.resolve()

# Complete path to the map
map_path = script_path / map_file

# --------------------------------------------------
# Load the map
# --------------------------------------------------

with open(map_path, "r", encoding="utf-8") as f:
    platforms = json.load(f)

# --------------------------------------------------
# Center the window
# --------------------------------------------------

os.environ["SDL_VIDEO_CENTERED"] = "1"

import pgzrun

# --------------------------------------------------
# Window
# --------------------------------------------------

WIDTH = 1000
HEIGHT = 700

# --------------------------------------------------
# Physics
# --------------------------------------------------

GRAVITY = 0.35
BOUNCE = 0.15
FRICTION = 0.995
PLATFORM_THICKNESS = 16

# --------------------------------------------------
# Game objects
# --------------------------------------------------

balls = []
spawn_timer = 0

from pgzero.actor import Actor

WIDTH = 1000
HEIGHT = 800

GRAVITY = 0.5
BOUNCE = 0.85
BALL_RADIUS = 16

FLOOR_Y = HEIGHT - 60

# --------------------------------------------------
# Floor
# --------------------------------------------------

floor = Actor("floor")
floor.left = 0
floor.top = FLOOR_Y

# --------------------------------------------------
# Ball class
# --------------------------------------------------

class Ball:

    def __init__(self, x, y):

        self.actor = Actor("ball")
        self.actor.pos = (x, y)

        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-2, 2)

    def update(self):

        self.vy += GRAVITY

        self.actor.x += self.vx
        self.actor.y += self.vy

        self.wall_collision()
        self.floor_collision()
        self.platform_collision()

    def wall_collision(self):

        if self.actor.left <= 0:
            self.actor.left = 0
            self.vx *= -1

        if self.actor.right >= WIDTH:
            self.actor.right = WIDTH
            self.vx *= -1

    def floor_collision(self):

        if self.actor.bottom >= FLOOR_Y:

            self.actor.bottom = FLOOR_Y

            self.vy = -self.vy * BOUNCE
            self.vx *= 0.98

            if abs(self.vx) < 0.05:
                self.vx = 0

            if abs(self.vy) < 1:
                self.vy = 0

    def platform_collision(self):

        for p in platforms:

            x1 = p["x1"]
            y1 = p["y1"]
            x2 = p["x2"]
            y2 = p["y2"]

            dx = x2 - x1
            dy = y2 - y1

            length2 = dx*dx + dy*dy

            if length2 == 0:
                continue

            # Projection of the ball center onto the line
            t = ((self.actor.x - x1)*dx +
                 (self.actor.y - y1)*dy) / length2

            t = max(0, min(1, t))

            nearest_x = x1 + t*dx
            nearest_y = y1 + t*dy

            dist_x = self.actor.x - nearest_x
            dist_y = self.actor.y - nearest_y

            dist = math.hypot(dist_x, dist_y)

            if dist < BALL_RADIUS:

                nx = dist_x / (dist + 1e-6)
                ny = dist_y / (dist + 1e-6)

                overlap = BALL_RADIUS - dist

                self.actor.x += nx * overlap
                self.actor.y += ny * overlap

                dot = self.vx * nx + self.vy * ny

                self.vx -= 2 * dot * nx
                self.vy -= 2 * dot * ny

                self.vx *= 0.98
                self.vy *= BOUNCE

    def draw(self):
        self.actor.draw()


# --------------------------------------------------
# Create several balls
# --------------------------------------------------

balls = []

for i in range(10):

    x = random.randint(100, WIDTH - 100)
    y = random.randint(50, 250)

    balls.append(Ball(x, y))


# --------------------------------------------------
# Update
# --------------------------------------------------

def update():

    for ball in balls:
        ball.update()


# --------------------------------------------------
# Draw
# --------------------------------------------------

def draw():

    screen.fill("skyblue")

    # Draw platforms
    for p in platforms:

        screen.draw.line(
            (p["x1"], p["y1"]),
            (p["x2"], p["y2"]),
            "darkgreen"
        )

    floor.draw()

    for ball in balls:
        ball.draw()


pgzrun.go()