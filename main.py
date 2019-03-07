import json
from os import system
from sty import fg, bg
from random import choice
import sys

WRONG_INTERACTION_RESPONSES = [
    "non succede nulla",
    "non funziona",
    "niente da fare",
    "non credo sia la cosa giustsa da fare",
    "non credo proprio",
    "non e'il caso"
]
IS_WINDOWS = sys.platform.lower() == "win32"


class Directions:
    N = 0
    S = 1
    W = 2
    E = 3


class Entity:
    def __init__(self, room, x, y, graphic=None, color=None, name=None, description=None, interactions=None):
        self.room = room
        self.x = x
        self.y = y
        self.graphic = graphic
        self.color = color
        self.name = name
        self.description = description
        self.interactions = interactions

    def set(self, graphic, definition):
        self.graphic = graphic
        self.color = getattr(bg, definition["color"])
        self.name = definition["name"]
        self.description = definition["description"]

    def interact(self, item=None):
        if self.description:
            print(self.description)

        if self.interactions:
            if item in self.interactions:
                self.interactions[item]()
            else:
                if item is None and "no-item" in self.interactions:
                    self.interactions["no-item"]()
                else:
                    print(choice(WRONG_INTERACTION_RESPONSES))

    def __str__(self):
        return self.color + " " + self.graphic + " " + fg.rs + bg.rs


class Mobile(Entity):
    def __init__(self, room, x, y, graphic, color):
        Entity.__init__(self, room, x, y, graphic, color)

    def move(self, direction):
        if direction == Directions.N and self.y > 0 and self.room.get_entity_at_coords(self.x, self.y - 1) is None:
            self.y -= 1
        elif direction == Directions.S and self.y < self.room.h - 1 and self.room.get_entity_at_coords(self.x, self.y + 1) is None:
            self.y += 1
        elif direction == Directions.W and self.x > 0 and self.room.get_entity_at_coords(self.x - 1, self.y) is None:
            self.x -= 1
        elif direction == Directions.E and self.x < self.room.w - 1 and self.room.get_entity_at_coords(self.x + 1, self.y) is None:
            self.x += 1


class Player(Mobile):
    def __init__(self, x, y):
        Mobile.__init__(self, None, x, y, "P", bg.blue)
        self.inventory = []

    def draw_inventory(self):
        print("Inventory:")
        l = len(self.inventory)
        if l == 0:
            print("\t- empty")
        else:
            for i in range(l):
                print("\t- {}. {}".format(i, self.inventory[i]))

    def change_player_room(self, room):
        # self.room.number
        self.room = room
        # todo set player coords based on previous room

    def get_nearby_entities(self):
        nearby_entities = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if not x == y == 0:
                    entity = self.room.get_entity_at_coords(self.x + x, self.y + y)
                    if entity and type(entity) is not Wall:
                        nearby_entities.append(entity)

        return nearby_entities


class Wall(Entity):
    def __init__(self, room, x, y):
        Entity.__init__(self, room, x, y, " ", bg.da_black)


class Game:
    file = open("./entities.json")
    items = json.load(file)
    file.close()

    def __init__(self):
        self.player = Player(1, 1)
        self.rooms = []
        for i in range(1):
            self.rooms.append(Room(i, self.player))

        self.player.room = self.rooms[0]

    def get_current_room(self):
        return self.player.room

    def update(self):
        if IS_WINDOWS:
            system("cls")
        else:
            system("clear")

        print()
        self.get_current_room().draw()
        print()
        self.player.draw_inventory()
        print()
        print("Azioni:")
        print("\t- muovi premendo W A S D")
        nearby_entities = self.player.get_nearby_entities()
        for e in nearby_entities:
            print("\t- interagisci con {} premendo {}".format(e.name, e))
        print("\t- QUIT per uscire")

        action = input().upper()
        if action == "W":
            self.player.move(Directions.N)
        elif action == "S":
            self.player.move(Directions.S)
        elif action == "A":
            self.player.move(Directions.W)
        elif action == "D":
            self.player.move(Directions.E)
        elif action == "QUIT":
            quit()
        else:
            for e in nearby_entities:
                if action == e.graphic:
                    e.interact()
                    input("premi un tasto per continuare...")
                    break


class Room:
    def __init__(self, number, player):
        self.number = number
        file = open("./rooms/{}.room".format(number))
        rows = file.readlines()
        file.close()
        self.h = len(rows)
        self.w = len(rows[0]) - 1
        self.entities = [player]

        for y in range(self.h):
            for x in range(self.w):
                char = rows[y][x].upper()
                if char == "#":
                    self.entities.append(Wall(self, x, y))
                elif char in Game.items:
                    e = Entity(self, x, y)
                    e.set(char, Game.items[char])
                    self.entities.append(e)

    def get_entity_at_coords(self, x, y):
        for e in self.entities:
            if e.x == x and e.y == y:
                return e

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                e = self.get_entity_at_coords(x, y)
                if e:
                    print(e, end="")
                else:
                    print(bg.da_red + "   " + bg.rs, end="")
            print()


g = Game()

while True:
    g.update()
