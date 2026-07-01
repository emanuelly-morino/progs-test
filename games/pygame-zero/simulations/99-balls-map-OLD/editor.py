# encontrar a pasta na qual este programa está executando
from pathlib import Path

# Returns a Path object of the script's directory
caminho = Path(__file__).parent.resolve()


import json
import glob
import os
import pgzrun

WIDTH = 1000
HEIGHT = 700

platforms = []

start_point = None
mouse_pos = (0, 0)

message = "Press I to choose start point"


def draw():
    screen.fill((30, 30, 40))

    # Draw platforms
    for p in platforms:
        screen.draw.line(
            (p["x1"], p["y1"]),
            (p["x2"], p["y2"]),
            (220, 220, 255),
        )

        screen.draw.filled_circle((p["x1"], p["y1"]), 5, "green")
        screen.draw.filled_circle((p["x2"], p["y2"]), 5, "red")

    # Preview
    if start_point is not None:
        screen.draw.filled_circle(start_point, 6, "yellow")
        screen.draw.line(start_point, mouse_pos, "yellow")

    screen.draw.text(
        "I = Start   F = Finish   N = New   S = Save   L = Load",
        (10, 10),
        fontsize=30,
        color="white",
    )

    screen.draw.text(message, (10, 45), fontsize=28, color="cyan")


def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos


def on_key_down(key):
    global start_point
    global platforms
    global message

    if key == keys.N:
        platforms = []
        start_point = None
        message = "New map"

    elif key == keys.I:
        start_point = mouse_pos
        message = f"Start point = {start_point}"

    elif key == keys.F:
        if start_point is None:
            message = "Press I first."
            return

        platforms.append(
            {
                "x1": start_point[0],
                "y1": start_point[1],
                "x2": mouse_pos[0],
                "y2": mouse_pos[1],
            }
        )

        message = f"Platform #{len(platforms)} created"
        start_point = None

    elif key == keys.S:
        save_map()

    elif key == keys.L:
        load_map()


def save_map():
    global message

    files = sorted(caminho.glob("map*.json"))

    if not files:
        number = 1
    else:
        last = os.path.splitext(files[-1])[0]
        number = int(last[-3:]) + 1

    filename = f"map{number:03d}.json"

    # adicionar o caminho ao mapa
    filename = os.path.join(caminho, filename)


    with open(filename, "w") as f:
        json.dump(platforms, f, indent=4)

    message = f"Saved {filename}"


def load_map():
    global platforms
    global message

    print()
    print("Existing maps:")
    for f in sorted(glob.glob("map*.json")):
        print("   ", f)

    print()

    name = input("Map name: ")

    try:
        with open(name) as f:
            platforms = json.load(f)

        message = f"Loaded {name}"

    except Exception:
        message = "Cannot load map."

pgzrun.go()