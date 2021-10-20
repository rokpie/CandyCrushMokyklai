lygiai = [{'lenta':[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions' : 4}, {'lenta':[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions' : 4}]

def drawBoard(lygis):
  lygis  = lygis -1
  a = "---"
  for i in range((lygiai[lygis]['dimensions'])-1):
    a= a+"----"
  for y in range(lygiai[(lygis)]['dimensions']):
    for x in range(lygiai[(lygis)]['dimensions']):
      print(lygiai[(lygis)]['lenta'][(y)*(lygiai[(lygis)]['dimensions']) + x], end= (" | "))
    print()
    print(a)

level = int(input("Kurio nori lygio: ")) 
drawBoard(level)
