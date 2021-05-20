# -*- coding: utf-8 -*-
"""
@author: Björn Luig
"""

import numpy as np

def show(field): # show the sudoku field in the consol
    if np.any(field):
        bar = 25 * "-"
        for i in range(3):
            print(bar)
            for ii in range(3):
                row = ""
                for j in range(3):
                    row += "| "
                    for jj in range(3): row += str(field[3*i+ii][3*j+jj])+" "
                row += "|"
                print(row)
        print(bar)
    else:
        print("this sudoku is not solvable!")

def block(field,i,j): # get elements of the 3x3-block wich contains (i,j)
        i -= i%3
        j -= j%3
        return([field[i+ii][j+jj] for ii in range(3) for jj in range(3)])

def possibilities(field,i,j): # possible numbers at (i,j)
    p = field[i][j]
    if p: return([p]) # number already fixed
    p = [1,2,3,4,5,6,7,8,9]
    for numbers in [field[i,:],field[:,j], block(field,i,j)]:
        for k in range(9):
            if numbers[k]:
                # remove all numbers from p, wich are not possible anymore
                try: p.remove(numbers[k])
                except: pass
    return(p)

def solve(field): # solve a sudoku
    solved = False
    changed = True
    while not(solved) and changed:
        solved = True
        changed = False
        for i in range(9):
            for j in range(9):
                if not field[i,j]:
                    solved = False
                    p = possibilities(field,i,j)
                    if not p: # no possible number at (i,j)
                        return(None)
                    if(len(p) == 1): # exactly one  possible number at (i,j)
                        field[i,j] =p[0]
                        changed = True
                    else:
                        for number in p: # recursion necessery, try numbers in p
                            testField = field.copy()
                            testField[i][j] = number
                            testField = solve(testField)
                            if np.any(testField): return(testField)
                        return(0)
    return(field)

# start sudoku solver and enter sudoku field
print('SUDOKU SOLVER')
loop = True
while loop:
    text = input('enter sudoku line by line (l) or solve test sudoku (t)? ')
    if text in ['l','t']: loop = False
    else: print('unvalid input!')
if text == 'l':
    print("0,space = empty\nyou can skip empty fields at the end)")
    field = np.zeros(shape=(9,9),dtype="int")
    for i in range(9):
        loop = True
        while loop:
            loop = False
            row = input("enter numbers of the "+str(i+1)+"th line: ").replace(" ","0")
            try:
                for j in range(min(len(row),9)): field[i,j] = int(row[j])
            except:
                loop = True
                print("unvalid input!")
    show(field)
    print("solving...(can take seconds or hours)")
    show(solve(field))
else:
    field = np.array([[0,0,3,0,0,0,2,0,0],
                     [0,2,0,4,0,8,0,3,0],
                     [8,0,0,0,9,0,0,0,4],
                     [0,5,0,6,0,1,0,2,0],
                     [0,0,8,0,0,0,6,0,0],
                     [0,7,0,8,0,4,0,1,0],
                     [1,0,0,0,7,0,0,0,0],
                     [0,4,0,1,0,2,0,0,0],
                     [0,0,9,0,0,0,0,0,0],])
    show(field)
    print("solving...")
    show(solve(field))

# end
input('press enter to exit')
