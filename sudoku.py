import copy

def nullmatrix():
    matrix = []
    for i in range(9):
        zeile = []
        for j in range(9):
            zeile.append(int(0))
        matrix.append(zeile)
    return(matrix)

def eingabe():
    matrix = []
    for i in range(9):
        matrix.append([])
        zeile = input(str(i+1) + ". Zeile eingeben (0 = leeres Feld): ")
        for j in range(9):
            try:
                x = int(zeile[j])
                if not(0<=x<10):
                    x = 0
                    print(str(x) + " ist ungueltiger Eintrag")
            except:
                x = 0
            matrix[i].append(x)
        print(matrix[i])
    return(matrix)

def zeigen(matrix):
    if(matrix == 0):
        print("Matrix existiert nicht!!!")
    else:
        l = 25 * "-"
        for i in range(3):
            print(l)
            for ii in range(3):
                t = ""
                for j in range(3):
                    t += "| "
                    for jj in range(3):
                        t += str(matrix[3*i+ii][3*j+jj])
                        t += " "
                print(t + "|")
        print(l)
    
def zeile(matrix, i):
    if 0<=i<9: return(matrix[i])
    else: print(str(i) + " ist ungueltiger Index fuer eine Zeile")

def spalte(matrix, j):
    if 0<=j<9:
        s = []
        for i in range(9): s.append(matrix[i][j])
        return(s)
    else: print(str(j) + " ist ungueltiger Index fuer eine Spalte")

def kasten(matrix, i, j):
    if (0<=i<9) and (0<=j<9):
        i -= i%3
        j -= j%3
        k = []
        for ii in range(3):
            for jj in range(3):
                k.append(matrix[ii+i][jj+j])
        return(k)
    else: print(str(i) + " oder " + str(j) + " sind ungueltige Indizes eines Kastens")

def moeglichkeiten(matrix, i, j):
    m = matrix[i][j]
    if(m != 0): return([m])
    m = [1,2,3,4,5,6,7,8,9]
    for v in [zeile(matrix, i), spalte(matrix, j), kasten(matrix, i, j)]:
        for i in range(9):
            if(v[i] != 0):
                try: m.remove(v[i])
                except: pass
    return(m)

def loesen(matrix):
    fertig = False
    geaendert = True
    while(not(fertig) and geaendert):
        fertig = True
        geaendert = False
        for i in range(9):
            for j in range(9):
                if(matrix[i][j] == 0):
                    fertig = False
                    m = moeglichkeiten(matrix, i, j)
                    if(m == []):
                        return(0)
                        print("Nicht lösbar")
                    if(len(m) == 1):
                        matrix[i][j] = m[0]
                        geaendert = True
                    else:
                        for x in m:
                            testmatrix = copy.deepcopy(matrix)
                            testmatrix[i][j] = x
                            testmatrix = loesen(testmatrix)
                            if(testmatrix != 0): return(testmatrix)
                        return(0)
    return(matrix)

def steuerung():
    matrix = [[0,0,3,0,0,0,2,0,0],
              [0,2,0,4,0,8,0,3,0],
              [8,0,0,0,9,0,0,0,4],
              [0,5,0,6,0,1,0,2,0],
              [0,0,8,0,0,0,6,0,0],
              [0,7,0,8,0,4,0,1,0],
              [1,0,0,0,7,0,0,0,0],
              [0,4,0,1,0,2,0,0,0],
              [0,0,9,0,0,0,0,0,0],
              ]
    print("Sudoku")
    print("Testmatrix:\n")
    zeigen(matrix)
    an = True
    while(an):
        text = input("bitte Befehl eingeben: ")
        t = text.split(" ")
        try:
            if(t[0] == "eingabe" or t[0] == "ein"):
                matrix = eingabe()
                zeigen(matrix)
            elif(t[0] == "zeigen" or t[0] == ""): zeigen(matrix)
            elif(t[0] == "setzewert" or t[0] == "set"):
                matrix[int(t[1])-1][int(t[2])-1] = int(t[3])
                zeigen(matrix)
            elif(t[0] == "null" or t[0] == "0"):
                matrix = nullmatrix()
                zeige(matrix)
            elif(t[0] == "zeile" or t[0] == "z"): print(zeile(matrix, int(t[1])-1))
            elif(t[0] == "spalte" or t[0] == "s"): print(spalte(matrix, int(t[1])-1))
            elif(t[0] == "kasten" or t[0] == "k"): print(kasten(matrix, int(t[1])-1, int(t[2])-1))
            elif(t[0] == "moeglichkeiten" or t[0] == "m"): print(moeglichkeiten(matrix, int(t[1])-1, int(t[2])-1))
            elif(t[0] == "loesen" or t[0] == "l"):
                matrix = loesen(matrix)
                zeigen(matrix)
            elif(t[0] == "exit" or t[0] == "x" or t[0] == "X"): an = False
            else: print("Befehl ungueltig")
        except:
            print("Falsche Syntax: " + str(text) + " ist ungueltig.")
    print("beendet")

steuerung()
