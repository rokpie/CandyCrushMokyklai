
lenta = []

lygiai = {lenta:[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], "dimensions" : 4}


def drawBoard(lygis):
  for y in range(lygiai[lygis].dimensions):
    for x in range(lygiai[lygis].dimensions):
      print(lenta[(y)*8 + x], end= (" | "))
    print()
    print("-------------------------------")

drawBoard(1)
