import math
import random
import time
chil = [[]]
pars = [-1]
vals = [[0, 0]]
moof = [[-1, -1]]
bord = []
nodbord = [[]]
bw = 1
posmov = [[]]
nodbw = [2]
posnsim = [[]]
def gameover():
    temdas = 0
    for i in range(8):
        for k in range(8):
            if(bord[i][k]==0):
                return -1
            else:
                if(bord[i][k] == 1):
                    temdas = temdas-1
                if(bord[i][k] == 2):
                    temdas = temdas+1
    return temdas
def getpar(chil, upto):
    ret = [chil]
    if(chil == upto):
        return ret
    while(True):
        chil = pars[chil]
        ret.append(chil)
        if(chil == upto):
            return ret
def adchil(par):
    global chil
    global pars
    global vals
    chil[par].append(len(chil))
    chil.append([])
    vals.append([0, 0])
    pars.append(par)
    moof.append([-1, -1])
    posmov.append([])
    nodbord.append([])
    nodbw.append(3-nodbw[par])
    posnsim.append([])
def getbagus(par):
    global chil
    global vals
    temp = 0
    if(0 < len(posmov[par])):
            return -par
    for i in chil[par]:
        if(vals[i][0]+vals[i][1] == 0):
            print("This shouldn't happen")
            return -i
        tmep = vals[i][0]/(vals[i][0]+vals[i][1]) + math.sqrt(2* math.log(vals[par][0] + vals[par][1], math.e)/(vals[i][0]+vals[i][1]))
        if(temp<=tmep):
            temp = tmep
            bagoose = i
    try:
        return bagoose
    except:
        print(len(chil[par]), par, chil[par], moof[par])
def expnode(nod):
    while(True):
        if(len(chil[nod])==0):
            return nod
        temp = getbagus(nod)
        if(temp<=0):
            return -temp
        nod = temp
#1 - white, 2- black
for i in range(8):
    temp = []
    for i in range(8):
        temp.append(0)
    bord.append(temp)
bord[3][3] = 1
bord[4][4] = 1
bord[3][4] = 2
bord[4][3] = 2
nodbord[0]  = [x[:] for x in bord]
def gvm(bw, bord):
    validMoves = []
    for x in range(8):
        for y in range(8):
            temp = isValidMove(x, y, bw, bord)
            if(temp!=False):
                validMoves.append([x, y, temp])
    return validMoves
def isValidMove(x, y, bw, obrd):
    if obrd[x][y] != 0 or not (x >= 0 and x <= 7 and y >= 0 and y <=7):
        return False
    obrd[x][y] = bw
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        tx, ty = x, y
        tx += xdirection
        ty += ydirection
        if (tx >= 0 and tx <= 7 and ty >= 0 and ty <=7) and obrd[tx][ty] == 3-bw:
            tx += xdirection
            ty += ydirection
            if not (tx >= 0 and tx <= 7 and ty >= 0 and ty <=7):
                continue
            while obrd[tx][ty] == 3-bw:
                tx += xdirection
                ty += ydirection
                if not (tx >= 0 and tx <= 7 and ty >= 0 and ty <=7):
                    break
            if not (tx >= 0 and tx <= 7 and ty >= 0 and ty <=7):
                continue
            if obrd[tx][ty] == bw:
                while True:
                    tx -= xdirection
                    ty -= ydirection
                    if tx == x and ty == y:
                        break
                    tilesToFlip.append([tx, ty])
    obrd[x][y] = 0
    if len(tilesToFlip) == 0: 
        return False
    return tilesToFlip
def tes(expno):
    global chil
    global bw
    global pars
    global vals
    global bord
    wb = nodbw[expno]
    tbod = [x[:] for x in nodbord[expno]]
    teemp = posmov[expno]
    if(teemp == [-1]):
        adchil(expno)
        nodbord[-1] = [x[:] for x in tbod]
        posmov[-1]  = gvm(3-wb, tbod)
        if(posmov[-1] == []):
            posmov[-1] = [-1]
        moof[-1] = [-1, -1]
        prevturntook = False
        del posmov[expno][0]
    else:
        ran = random.randint(0, len(teemp)-1)
        for i in teemp[ran][2]:
            tbod[i[0]][i[1]] = wb
        tbod[teemp[ran][0]][teemp[ran][1]] = wb
        adchil(expno)
        nodbord[-1] = [x[:] for x in tbod]
        posmov[-1]  = gvm(3-wb, tbod)
        if(posmov[-1] == []):
            posmov[-1] = [-1]
        moof[-1] = [teemp[ran][0], teemp[ran][1]]
        prevturntook = True
        del posmov[expno][ran]
    while(True):
        wb = 3-wb
        teemp = gvm(wb, tbod)
        if(teemp!=[]):
            ran = random.randint(0, len(teemp)-1)
            prevturntook = True
            for i in teemp[ran][2]:
                tbod[i[0]][i[1]] = wb
            tbod[teemp[ran][0]][teemp[ran][1]] = wb
        else:
            if(prevturntook == False):
                wiin = 0
                for h in range(8):
                    for w in range(8):
                        if(tbod[h][w]==bw):
                            wiin+=1
                        elif(tbod[h][w]==3-bw):
                            wiin-=1
           #     if(nodbw[expno] == bw):
             #       vals[-1][0]+=1
              #  else:
               #     vals[-1][1]+=1
               # return 1
                if(wiin > 0):
                    if(nodbw[expno] == bw):
                        vals[-1][0]+=1
                    else:
                        vals[-1][1]+=1
                    return 1
                elif(wiin == 0):
                    vals[-1][0]+=0.5
                    vals[-1][1]+=0.5
                    return 0.5
                else:
                    if(nodbw[expno] == bw):
                        vals[-1][1]+=1
                    else:
                        vals[-1][0]+=1
                    return 0
            prevturntook = False
def bageesechil(nod):
    magxplay = -1
    magxwin = -1
    besact = []
    besmeh = []
    for chl in chil[nod]:
        wins = vals[chl][0]
        plays = vals[chl][0]+vals[chl][1]
        if plays > magxplay:
            magxplay = plays
            besact = [moof[chl]]
            besmeh = [chl]
            magxwin = wins
        elif plays == magxplay:
            if wins > magxwin:
                magxwin = wins
                besact = [moof[chl]]
                besmeh = [chl]
            elif wins == magxwin:
                besact.append(moof[chl])
                besmeh.append(chl)
    return random.choice(besmeh)
#bw = int(input("Black or white (1 - white, 2- black)?"))
bw = 2
turnno = 0
curroot = 0
tiama = 0
posmov[0] = gvm(bw, bord)
simrun = 0
def thing(num):
    if(num==0):
        return '_'
    elif(num==1):
        return 'X'
    else:
        return '0'
while(True):
    sadfds = gameover()
    if(sadfds>=0):
        print("Game over!\n")
        if(sadfds==0):
            print("Tie!")
        if(sadfds>0):
            print("Black wins! ",(64+sadfds)/2, "-", (64-sadfds)/2)
        if(sadfds<0):
            print("White wins!",(64+sadfds)/2, "-", (64-sadfds)/2)
        for j in range(8):
            for k in range(8):
                print(bord[k][j], end = " ")
            print("")
        break
    if(turnno%2==bw%2):
        simrun=0
        tiama = time.time()
        while(time.time()<tiama+10):
            simrun+=1
            for i in range(10):
                temp = 0
                exno = expnode(curroot)
                result = tes(exno)
          #      result = 1
                meh = getpar(exno, curroot)
                meh.reverse()
                for a in range(len(meh)):
                    vals[meh[a]][1]+= result
                    vals[meh[a]][0]+= (1-result)
                    result = 1-result
           #     meh = exno
             #   while(True):
               #     vals[meh][1]+= result
                 #   vals[meh][0]+= (1-result)
                   # result = 1-result
                   # meh = pars[meh]
                    #if(meh == -1):
                     #   break
        curroot = bageesechil(curroot)
        print("Take this move:", moof[curroot][0], moof[curroot][1],"Time taken:", time.time()-tiama, "Simulations run:", simrun*10, "Turns passed:", turnno)
        bord = [x[:] for x in nodbord[pars[curroot]]]
        if(moof[curroot]!=[-1, -1]):
            whateve = isValidMove(moof[curroot][0], moof[curroot][1], bw, bord)
            for j in whateve:
                bord[j[0]][j[1]] = bw
            bord[moof[curroot][0]][moof[curroot][1]] = bw
    else:
        print("-", end=" ")
        for j in range(8):
            print(j, end=" ")
        print("")
        for j in range(8):
            print(j, end=" ")
            for k in range(8):
                print(thing(bord[k][j]), end = " ")
            print("")
        ptem = gvm(3-bw, bord)
        if(ptem!=[]):
            if(len(ptem)!=len(chil[curroot])):
                print("!!!!!!", len(ptem), len(chil[curroot]))
            for i in range(len(chil[curroot])):
                print(i, ": (", moof[chil[curroot][i]][0], ",", moof[chil[curroot][i]][1], ")")
            if(chil[curroot]!=[-1] and chil[curroot]!=[-1, -1]):
                oppmove = int(input("Choose a move:"))
               # oppmove = random.randint(0, len(chil[curroot])-1)
                if(oppmove>-1 and oppmove<len(chil[curroot])):
                    bord = [x[:] for x in nodbord[chil[curroot][oppmove]]]
                    curroot = chil[curroot][oppmove]
                else:
                    print("Invalid move, scrub!")
                    turnno-=1
            else:
                curroot = chil[curroot][0]
    turnno+=1

