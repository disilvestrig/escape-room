class Entity:
  def __init__(self, x, y, graphic, name):
    self.x = x
    self.y = y
    self.graphic = graphic
    self.name = name

class Wall(Entity):
  def __init__(self, x, y):
    Entity.__init__(self, x, y, "M", "muro")

class Room:
  def __init__(self, number):
    self.number = number
    file = open("./rooms/{}.room".format(number))
    rows = file.readlines()
    file.close()
    self.h = len(rows)
    self.w = len(rows[0]) -1
    self.entities = []

    for y in range(self.h):
      for x in range(self.w):
        if rows[y][x] == "#":
          self.entities.append(Wall(x, y))


  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if e.x == x and e.y == y:
            print("[{}]".format(e.graphic), end="")
            break
        else:
          print("[ ]", end="")
      print()

r = Room(0)
r.draw()
'''

  print()
'''