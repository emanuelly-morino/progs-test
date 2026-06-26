import math
import random
import pgzrun

WIDTH = 800
HEIGHT = 600

GRAVITY = 0.35
BOUNCE = 0.15
FRICTION = 0.995

balls = []
spawn_timer = 0

# Sloped platforms
platforms = [
    (100, 140, 350, 190),
    (400, 220, 180, 310),
    (250, 390, 650, 450),
    (650, 520, 350, 570),
]


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

        for x1, y1, x2, y2 in platforms:

            cx, cy = closest_point(ball["x"], ball["y"], x1, y1, x2, y2)

            dx = ball["x"] - cx
            dy = ball["y"] - cy
            dist = math.hypot(dx, dy)

            if dist < ball["r"]:

                if dist == 0:
                    nx, ny = 0, -1
                else:
                    nx = dx / dist
                    ny = dy / dist

                overlap = ball["r"] - dist

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
        screen.draw.line((p[0], p[1]), (p[2], p[3]), (220, 220, 255))

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