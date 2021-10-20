lygiai = [
    {'lenta':[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions' : 4}, 
    {'lenta':[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions' : 4}
  ]

def drawBoard():
  lygis  = level -1
  a = "---"
  for i in range((lygiai[lygis]['dimensions'])-1):
    a= a+"----"
  for y in range(lygiai[(lygis)]['dimensions']):
    for x in range(lygiai[(lygis)]['dimensions']):
      print(lygiai[(lygis)]['lenta'][(y)*(lygiai[(lygis)]['dimensions']) + x], end= (" | "))
    print()
    print(a)
  
def langelioTikrinimas(x, y): #nuskaitys y nuo 0 iki (dimensions -1) ir x nuo 0 iki (dimensions -1)
  lygis = level - 1
  if (0 <= y < lygiai[lygis]['dimensions']):
    if (0<= x < lygiai[lygis]['dimensions']):
      return True
    else:
      return False
  else:
    return False

level = int(input("Kurio nori lygio: ")) 
drawBoard()
