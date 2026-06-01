# Updated Pygame Zero tower defense game with:
# - Single lane
# - Larger characters
# - Basic sprite animation support
# - Enemies queue and don't overlap

import random, math
import pgzrun

WIDTH = 1200
HEIGHT = 500
LANE_Y = HEIGHT // 2

lives = 20
spawn_timer = 0

UNIT_TYPES = {
    "soldier": {"hp": 80, "speed": 2, "damage": 6, "range": 60, "cooldown": 40},
    "archer": {"hp": 50, "speed": 2.2, "damage": 5, "range": 160, "cooldown": 30},
    "tank": {"hp": 180, "speed": 1, "damage": 10, "range": 50, "cooldown": 60},
    "ninja": {"hp": 40, "speed": 4, "damage": 8, "range": 40, "cooldown": 18},
    "mage": {"hp": 60, "speed": 1.8, "damage": 12, "range": 130, "cooldown": 50},
}

player_units = []
enemy_units = []
towers = []

class Unit:
    def __init__(self, x, kind, team="player"):
        self.x = x
        self.y = LANE_Y
        self.kind = kind
        self.team = team
        self.stats = UNIT_TYPES[kind].copy()
        self.hp = self.stats['hp']
        self.cooldown = 0
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 0.15) % 4
        enemies = enemy_units if self.team == 'player' else player_units
        target = None
        nearest = 99999
        for e in enemies:
            d = abs(e.x - self.x)
            if d < nearest:
                nearest = d
                target = e
        if target and nearest <= self.stats['range']:
            if self.cooldown <= 0:
                if self.kind == 'mage':
                    for e in enemies:
                        if abs(e.x - self.x) < 70:
                            e.hp -= self.stats['damage']
                else:
                    target.hp -= self.stats['damage']
                self.cooldown = self.stats['cooldown']
        else:
            direction = 1 if self.team == 'player' else -1
            self.x += self.stats['speed'] * direction
        if self.cooldown > 0:
            self.cooldown -= 1

    def draw(self):
        img = f"{self.kind}{int(self.frame)}"
        try:
            screen.blit(img, (self.x-32, self.y-32))
        except:
            screen.draw.filled_circle(
                (self.x, self.y),
                24,
                "blue" if self.team == "player" else "red"
            )

class Tower:
    def __init__(self, x, kind):
        self.x = x
        self.kind = kind
        self.spawn_cd = 0

    def update(self):
        if self.spawn_cd <= 0:
            player_units.append(Unit(self.x+50, self.kind))
            self.spawn_cd = 180
        else:
            self.spawn_cd -= 1

    def draw(self):
        screen.draw.filled_rect(Rect((self.x-20, LANE_Y-60), (40, 120)), "gray")

class Enemy:
    def __init__(self):
        self.x = WIDTH - 80
        self.y = LANE_Y
        self.hp = 100
        self.speed = 1.2
        self.frame = 0

    def update(self):
        global lives
        self.frame = (self.frame + 0.1) % 4
        # stop if too close to enemy ahead
        ahead = [e for e in enemy_units if e != self and e.x < self.x]
        blocked = False
        if ahead:
            nearest = max(ahead, key=lambda e: e.x)
            if self.x - nearest.x < 60:
                blocked = True
        if not blocked:
            self.x -= self.speed
        if self.x < 50:
            lives -= 1
            if self in enemy_units:
                enemy_units.remove(self)

    def draw(self):
        img = f"enemy{int(self.frame)}"
        try:
            screen.blit(img, (self.x-32, self.y-32))
        except:
            screen.draw.filled_circle((self.x, self.y), 26, "darkred")

for i, kind in enumerate(UNIT_TYPES.keys()):
    towers.append(Tower(80, kind))


def update():
    global spawn_timer
    spawn_timer += 1
    if spawn_timer > 120:
        enemy_units.append(Enemy())
        spawn_timer = 0
    for t in towers:
        t.update()
    for u in player_units[:]:
        u.update()
        if u.hp <= 0:
            player_units.remove(u)
    for e in enemy_units[:]:
        e.update()
        if e.hp <= 0:
            enemy_units.remove(e)


def draw():
    screen.clear()
    screen.fill((40,40,60))
    screen.draw.line((0, LANE_Y+40), (WIDTH, LANE_Y+40), "white")
    for t in towers:
        t.draw()
    for u in player_units:
        u.draw()
    for e in enemy_units:
        e.draw()
    screen.draw.text(f"Lives: {lives}", (20,20), fontsize=40, color='white')

pgzrun.go()