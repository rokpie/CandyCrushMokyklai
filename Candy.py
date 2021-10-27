lygiai = [{'lenta': [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions': 4}, {'lenta': [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions': 4}]

galimiEjimai = []


def langelis(x, y):
    lygis = level - 1
    return lygiai[lygis]['lenta'][y*lygiai[lygis]['dimensions'] + x]


def drawBoard(lygis):
    lygis = lygis - 1
    a = "---"
    for i in range((lygiai[lygis]['dimensions'])-1):
        a = a+"----"
    for y in range(lygiai[lygis]['dimensions']):
        for x in range(lygiai[lygis]['dimensions']):
            print(lygiai[lygis]['lenta'][y*(lygiai[lygis]['dimensions']) + x], end=" | ")
        print()
        print(a)


level = int(input("Kurio nori lygio: ")) 
drawBoard(level)


def langelioTikrinimas(x, y):   # nuskaitys y nuo 0 iki (dimensions -1) ir x nuo 0 iki (dimensions -1)
    lygis = level - 1
    if 0 <= y < lygiai[lygis]['dimensions']:
        if 0 <= x < lygiai[lygis]['dimensions']:
            return True
        else:
            return False
    else:
        return False


oranzine = "o"
melyna = "m"
zalia = "z"
raudona = "r"


def ejimuPatikrinimas():
    lygis = level - 1
    galimiEjimai.clear()
    for y in range(lygiai[lygis]['dimensions']):
        for x in range(lygiai[lygis]['dimensions']):
            if not ((x == 0 and y == 0) or (x == lygiai[lygis]['dimensions']-1 and y == 0) or (y == lygiai[lygis]['dimensions']-1 and x == 0) or (y == lygiai[lygis]['dimensions']-1 and x == lygiai[lygis]['dimensions']-1)):
                # patikrinam ar langeliai ne kampuose
                if langelioTikrinimas(x, y-1) and langelioTikrinimas(x, y+1):   # patikrinam ar egzistuoja langeliai virsuje ir apacioje
                    # Patikrinam ar langeliai virsuj ir apacioj tokie patys
                    if langelis(x, y-1) == langelis(x, y+1):
                        spalva = langelis(x, y-1)
                        if langelioTikrinimas(x+1, y) and langelis(x+1, y) == spalva:
                            galimiEjimai.append([langelis(x, y), langelis(x+1, y)])
                        if langelioTikrinimas(x-1, y) and langelis(x-1, y) == spalva:
                            galimiEjimai.append([langelis(x, y), langelis(x-1, y)])
                    if langelioTikrinimas(x+1, y) and langelioTikrinimas(x-1, y):
                        if langelis(x+1, y) == langelis(x-1, y):
                            spalva = langelis(x+1, y)
                        if langelioTikrinimas(x, y+1) and langelis(x, y+1) == spalva:
                            galimiEjimai.append([langelis(x, y+1), langelis(x, y)])
                        if langelioTikrinimas(x, y-1) and langelis(x, y-1) == spalva:
                            galimiEjimai.append([langelis(x, y-1), langelis(x, y)])
                # tikriname ar langeliai apacioje kaireje ir virsuje kaireje yra tokie patys kaip vidurinis ir desineje vidurinis langelis
                if langelioTikrinimas(x-1, y-1) and langelioTikrinimas(x+1, y) and langelioTikrinimas(x-1, y+1):
                    spalva = langelis(x,y)
                    if langelis(x+1, y) == spalva:
                        if langelis(x-1, y-1) == spalva:
                            galimiEjimai.append([langelis(x-1, y-1), langelis(x-1, y)])
                        if langelis(x-1, y+1) == spalva:
                            galimiEjimai.append([langelis(x-1, y+1, x-1, y)])
                # tikriname ar langeliai apacioje desineje ir virsuje desineje yra tokie patys kaip vidurinis ir kaireje vidurinis langelis
                if langelioTikrinimas(x + 1, y - 1) and langelioTikrinimas(x - 1, y) and langelioTikrinimas(x + 1, y + 1):
                    spalva = langelis(x,y)
                    if langelis(x-1, y) == spalva:
                        if langelis(x+1, y+1) == spalva:
                            galimiEjimai.append([langelis(x + 1, y + 1), langelis(x + 1, y)])
                        if langelis(x + 1, y-1) == spalva:
                            galimiEjimai.append([langelis(x + 1, y - 1), langelis(x + 1, y)])


