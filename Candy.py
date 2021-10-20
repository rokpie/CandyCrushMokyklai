
lenta = []

lygiai = [{lenta:[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], "dimensions" : 4}, {lenta:[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], "dimensions" : 4}]


def drawBoard(lygis):
  for y in range(lygiai[(lygis -1)].dimensions):
    for x in range(lygiai[(lygis-1)].dimensions):
      print(lygiai[(lygis-1)].lenta[(y)*8 + x], end= (" | "))
    print()
    print("-------------------------------")

drawBoard(1)
