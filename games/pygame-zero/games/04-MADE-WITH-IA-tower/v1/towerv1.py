import random
import math
import pgzrun

WIDTH = 1000
HEIGHT = 600

# =========================
# GAME DATA
# =========================
money = 300
lives = 20
wave_timer = 0
spawn_timer = 0

# =========================
# UNIT TYPES
# =========================
UNIT_TYPES = {
    "soldier": {
        "color": (50, 200, 50),
        "hp": 50,
        "speed": 2,
        "damage": 5,
        "range": 50,
        "cooldown": 40,
        "special": "balanced"
    },
    "archer": {
        "color": (50, 150, 255),
        "hp": 30,
        "speed": 2.5,
        "damage": 4,
        "range": 120,
        "cooldown": 30,
        "special": "long range"
    },
    "tank": {
        "color": (180, 180, 180),
        "hp": 120,
        "speed": 1,
        "damage": 8,
        "range": 40,
        "cooldown": 60,
        "special": "high hp"
    },
    "ninja": {
        "color": (180, 50, 255),
        "hp": 25,
        "speed": 4,
        "damage": 7,
        "range": 35,
        "cooldown": 20,
        "special": "fast attack"
    },
    "mage": {
        "color": (255, 100, 50),
        "hp": 35,
        "speed": 2,
        "damage": 10,
        "range": 100,
        "cooldown": 50,
        "special": "splash damage"
    }
}

# =========================
# CLASSES
# =========================
class Unit:
    def __init__(self, x, y, kind, team="player"):
        self.x = x
        self.y = y
        self.kind = kind
        self.team = team
        self.stats = UNIT_TYPES[kind].copy()
        self.hp = self.stats["hp"]
        self.cooldown = 0
        self.target = None

    def update(self):
        enemies = enemy_units if self.team == "player" else player_units

        # Find nearest target
        self.target = None
        nearest = 99999
        for e in enemies:
            d = math.hypot(e.x - self.x, e.y - self.y)
            if d < nearest:
                nearest = d
                self.target = e

        # Attack if in range
        if self.target and nearest <= self.stats["range"]:
            if self.cooldown <= 0:
                self.attack()
                self.cooldown = self.stats["cooldown"]
        else:
            # Move
            direction = 1 if self.team == "player" else -1
            self.x += self.stats["speed"] * direction

        if self.cooldown > 0:
            self.cooldown -= 1

    def attack(self):
        if self.target:
            if self.kind == "mage":
                # splash
                for e in enemy_units[:]:
                    if math.hypot(e.x - self.x, e.y - self.y) < 60:
                        e.hp -= self.stats["damage"]
            else:
                self.target.hp -= self.stats["damage"]

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 12, self.stats["color"])
        screen.draw.filled_rect(Rect((self.x-15, self.y-20), (30, 4)), "red")
        hpw = max(0, 30 * self.hp / self.stats["hp"])
        screen.draw.filled_rect(Rect((self.x-15, self.y-20), (hpw, 4)), "green")


class Tower:
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.spawn_cd = 0

    def update(self):
        if self.spawn_cd <= 0:
            player_units.append(Unit(self.x + 20, self.y, self.kind))
            self.spawn_cd = 180
        else:
            self.spawn_cd -= 1

    def draw(self):
        screen.draw.filled_rect(Rect((self.x-15, self.y-25), (30, 50)), UNIT_TYPES[self.kind]["color"])
        screen.draw.text(self.kind[0].upper(), center=(self.x, self.y), color="black")


class Enemy:
    def __init__(self):
        self.x = WIDTH - 50
        self.y = random.randint(100, HEIGHT - 100)
        self.hp = 40
        self.speed = 1.5
        self.damage = 1

    def update(self):
        self.x -= self.speed
        if self.x < 50:
            global lives
            lives -= 1
            if self in enemy_units:
                enemy_units.remove(self)

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 10, "red")
        screen.draw.filled_rect(Rect((self.x-10, self.y-18), (20, 3)), "black")
        hpw = max(0, 20 * self.hp / 40)
        screen.draw.filled_rect(Rect((self.x-10, self.y-18), (hpw, 3)), "yellow")


# =========================
# GAME OBJECTS
# =========================
player_units = []
enemy_units = []
towers = []

# Starting towers
towers.append(Tower(100, 120, "soldier"))
towers.append(Tower(100, 220, "archer"))
towers.append(Tower(100, 320, "tank"))
towers.append(Tower(100, 420, "ninja"))
towers.append(Tower(100, 520, "mage"))

# =========================
# GAME LOOP
# =========================
def update():
    global spawn_timer

    spawn_timer += 1
    if spawn_timer > 60:
        enemy_units.append(Enemy())
        spawn_timer = 0

    for tower in towers:
        tower.update()

    for u in player_units[:]:
        u.update()
        if u.hp <= 0 or u.x > WIDTH:
            player_units.remove(u)

    for e in enemy_units[:]:
        if isinstance(e, Enemy):
            e.update()
        else:
            e.update()

        if hasattr(e, "hp") and e.hp <= 0:
            enemy_units.remove(e)

    # enemy soldiers occasionally
    if random.randint(0, 120) == 1:
        enemy_units.append(Unit(WIDTH - 100, random.randint(100, HEIGHT-100), "soldier", "enemy"))

def draw():
    screen.clear()
    screen.fill((40, 40, 60))

    # lanes
    for y in range(100, HEIGHT, 100):
        screen.draw.line((0, y), (WIDTH, y), (70, 70, 90))

    # base
    screen.draw.filled_rect(Rect((0, 0), (50, HEIGHT)), "blue")
    screen.draw.filled_rect(Rect((WIDTH-50, 0), (50, HEIGHT)), "darkred")

    for tower in towers:
        tower.draw()

    for u in player_units:
        u.draw()

    for e in enemy_units:
        e.draw()

    screen.draw.text(f"Lives: {lives}", (10, 10), fontsize=40, color="white")
    screen.draw.text(f"Units: {len(player_units)}", (10, 50), fontsize=30, color="white")

    if lives <= 0:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=80, color="red")


pgzrun.go()