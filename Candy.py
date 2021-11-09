from random import randint
lygiai = [{'lenta': ["m", "o", "z", "r", "o", "z", "r", "m", "m", "m", "m", "r", "r", "m", "m", "o"], 'dimensions': 4}, {'lenta': [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0], 'dimensions': 4}]

galimiEjimai = []

oranzine = "o"
melyna = "m"
zalia = "z"
raudona = "r"


def tileGenerate(x, y):
    # funkcija skirta sugeneruoti nauja tile tam tikrame laukelyje
    lygis = level - 1
    tile = lygiai[lygis]['lenta'][arrayPos(x, y)]
    tilenum = randint(1, 4)
    if tilenum == 1:
        tile = oranzine
    if tilenum == 2:
        tile = melyna
    if tilenum == 3:
        tile = zalia
    if tilenum == 4:
        tile = raudona
    lygiai[lygis]['lenta'][arrayPos(x, y)] = tile
    return tile


def kritimas():
    # funkcija skirta langeliu sukritimui, kai po jais yra tuščios vietos
    lygis = level - 1
    for y in range(lygiai[lygis]['dimensions']):
        for x in range(lygiai[lygis]['dimensions']):
            # kai tikrinimas langelis tuscias ir virsutinis langelis egzistuoja:
            if langelis(x, y) == " " and langelioTikrinimas(x, y-1):
                a = langelis(x, y)
                b = langelis(x, y-1)
                # sukeiciam abieju langeliu reiksmes
                lygiai[lygis]['lenta'][arrayPos(x, y - 1)] = a
                lygiai[lygis]['lenta'][arrayPos(x, y)] = b


def arrayPos(x, y):
    # funkcija skirta gauti lentos array pozicija naudojant x ir y koordinates
    lygis = level - 1
    if x == 0 and y != 0:
        pos = y*lygiai[lygis]["dimensions"]
    if x != 0 and y == 0:
        pos = x
    else:
        pos = y*lygiai[lygis]["dimensions"] + x
    return pos


def langelis(x, y):
    # funkcija skirta gauti langelio reiksme tam tikroje lentos vietoje
    lygis = level - 1
    return lygiai[lygis]['lenta'][y*lygiai[lygis]['dimensions'] + x]


def drawBoard(lygis):
    # funkcija skirta nupiesti lenta
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
    # funkcija skirta patikrinti ar duotas langelis egzistuoja
    lygis = level - 1
    # patikrina, ar tikrinamas langelis egzistuoja
    if 0 <= y < lygiai[lygis]['dimensions']:
        if 0 <= x < lygiai[lygis]['dimensions']:
            return True
        else:
            return False
    else:
        return False


def ejimuPatikrinimas():
    # daugybe ifu tam, kad patikrinti ar yra galimu ejimu
    lygis = level - 1
    galimiEjimai.clear()
    # praeinam pro visą lentą su dviem for loops:
    for y in range(lygiai[lygis]['dimensions']):
        for x in range(lygiai[lygis]['dimensions']):
            # jeigu tikrinami langeliai ne kampuose:
            if not ((x == 0 and y == 0) or (x == lygiai[lygis]['dimensions']-1 and y == 0) or (y == lygiai[lygis]['dimensions']-1 and x == 0) or (y == lygiai[lygis]['dimensions']-1 and x == lygiai[lygis]['dimensions']-1)):
                if langelioTikrinimas(x, y-1) and langelioTikrinimas(x, y+1):   # jeigui egzistuoja langeliai virsuje ir apacioje:
                    if langelis(x, y-1) == langelis(x, y+1):  # jeigu langeliai virsuje ir apacioje yra tokie patys:
                        spalva = langelis(x, y-1)
                        if langelioTikrinimas(x+1, y):  # jeigu langelis desineje viduryje egzistuoja:
                            if langelis(x+1, y) == spalva:  # jeigu šis langelis yra toks pat kaip virsuje ir apacioje, tada yra galimas ejimas:
                                galimiEjimai.append([(x, y), (x+1, y)])
                        if langelioTikrinimas(x-1, y):  # jeigu langelis kaireje viduryje egzistuoja:
                            if langelis(x-1, y) == spalva:  # jeigu šis langelis toks pat tada kaip virsuje ir apacioje, tada yra galimas ejimas:
                                galimiEjimai.append([(x, y), (x-1, y)])
                    if langelioTikrinimas(x+1, y) and langelioTikrinimas(x-1, y):  # jeigu egzistuoja langeliai kaireje ir desineje:
                        if langelis(x+1, y) == langelis(x-1, y):  # jeigu abu langeliai lygūs:
                            spalva = langelis(x+1, y)
                            if langelioTikrinimas(x, y+1):  # jeigu langelis virsuje egzistuoja:
                                if langelis(x, y+1) == spalva:  # jeigu langelis yra toks pat, galimas ejimas:
                                    galimiEjimai.append([(x, y), (x, y+1)])
                            if langelioTikrinimas(x, y-1):      # jeigu langelis apacioje egzistuoja:
                                if langelis(x, y-1) == spalva:  # jeigu langelis toks pat, yra ejimas:
                                    galimiEjimai.append([(x, y), (x, y-1)])
                # toliau tikrinama ar langeliai kairėje apacioje ir kaireje virsuje egzistuoja ir ar yra lygūs centriniui ir desinėje viduryje esanciam langeliui:
                spalva = langelis(x, y)
                if langelioTikrinimas(x+1, y):  # jeigu desineje viduryje langelis egzistuoja:
                    if langelioTikrinimas(x-1, y-1):
                        if langelis(x+1, y) == langelis(x-1, y-1) == spalva:
                            galimiEjimai.append([(x-1, y-1), (x-1, y)])
                    if langelioTikrinimas(x-1, y+1):
                        if langelis(x + 1, y) == langelis(x - 1, y + 1) == spalva:
                            galimiEjimai.append([(x - 1, y + 1), (x - 1, y)])
                # tas pats, tik dabar tikrinama ar langeliai desinėje virsuje ir desinėje apacioje yra lygūs centriniam ir kairėje viduryje esanciam langeliui:
                if langelioTikrinimas(x-1, y):  # jeigu kairėje viduryje langelis egzistuoja:
                    if langelioTikrinimas(x+1, y-1):
                        if langelis(x-1, y) == langelis(x+1, y-1) == spalva:
                            galimiEjimai.append([(x+1, y-1), (x+1, y)])
                    if langelioTikrinimas(x + 1, y + 1):
                        if langelis(x - 1, y) == langelis(x + 1, y + 1) == spalva:
                            galimiEjimai.append([(x + 1, y + 1), (x + 1, y)])
                # tikrinam ar langeliai virsuje kaireje ir virsuje desineje egzistuoja ir ar yra lygūs centriniam ir apatiniam vidurianiam langeliui:
                if langelioTikrinimas(x, y-1):  # jeigu apatinis langelis egzistuoja:
                    if langelioTikrinimas(x-1, y+1):
                        if langelis(x, y-1) == langelis(x-1, y+1) == spalva:
                            galimiEjimai.append([(x-1, y + 1), (x, y + 1)])
                    if langelioTikrinimas(x+1, y+1):
                        if langelis(x, y-1) == langelis(x+1, y+1) == spalva:
                            galimiEjimai.append([(x+1, y+1), (x, y + 1)])
                # tikrininam ar langeliai apacioje kaireje ir apacioje desineje egzistuoja ir yra lygūs centriniam ir virsutiniam viduriniam langeliui:
                if langelioTikrinimas(x, y+1):  # jeigu egzistuoja virsutinis langelis:
                    if langelioTikrinimas(x-1, y-1):
                        if langelis(x, y+1) == langelis(x-1, y-1) == spalva:
                            galimiEjimai.append([(x-1, y - 1), (x, y - 1)])
                    if langelioTikrinimas(x+1, y-1):
                        if langelis(x, y+1) == langelis(x+1, y-1) == spalva:
                            galimiEjimai.append([(x+1, y-1), (x, y - 1)])


def panaikinimas():
    lygis = level - 1
    # praeinam pro visa lenta:
    for y in range(lygiai[lygis]['dimensions']):
        for x in range(lygiai[lygis]['dimensions']):
            # jeigu tikrinami langeliai ne kampuose:
            if not ((x == 0 and y == 0) or (x == lygiai[lygis]['dimensions'] - 1 and y == 0) or (y == lygiai[lygis]['dimensions'] - 1 and x == 0) or (y == lygiai[lygis]['dimensions'] - 1 and x == lygiai[lygis]['dimensions'] - 1)):
                spalva = langelis(x, y)
                # jeigu trys langeliai horizontaliai yra tokie patys, juos galima sunaikinti t.y. palikti tuscia vieta
                if langelioTikrinimas(x+1, y):
                    if langelioTikrinimas(x-1, y):
                        if langelis(x+1, y) == langelis(x-1, y) == spalva:
                            lygiai[lygis]['lenta'][arrayPos(x-1, y)] = " "
                            lygiai[lygis]['lenta'][arrayPos(x, y)] = " "
                            lygiai[lygis]['lenta'][arrayPos(x+1, y)] = " "
                # jeigu trys langeliai vertikalia yra tokie patys, juos galima sunaikinti t.y. palikti tuscia vieta
                if langelioTikrinimas(x, y+1):
                    if langelioTikrinimas(x, y-1):
                        if langelis(x, y+1) == langelis(x, y-1) == spalva:
                            lygiai[lygis]['lenta'][arrayPos(x, y-1)] = " "
                            lygiai[lygis]['lenta'][arrayPos(x, y)] = " "
                            lygiai[lygis]['lenta'][arrayPos(x, y+1)] = " "


ejimuPatikrinimas()
panaikinimas()
kritimas()
drawBoard(1)
