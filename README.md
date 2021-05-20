# recursive-sudoku-solver
A simple recursive sudoku solver in python.

Examle:

    SUDOKU SOLVER
    enter sudoku line by line (l) or solve test sudoku (t)? l
    0,space = empty
    you can skip empty fields at the end)
    enter numbers of the 1th line: 00107029
    enter numbers of the 2th line: 04009081
    enter numbers of the 3th line: 06903004
    enter numbers of the 4th line: 850000109
    enter numbers of the 5th line: 02000607
    enter numbers of the 6th line: 076001
    enter numbers of the 7th line: 5172
    enter numbers of the 8th line: 600510907
    enter numbers of the 9th line: 400300021
    -------------------------
    | 0 0 1 | 0 7 0 | 2 9 0 |
    | 0 4 0 | 0 9 0 | 8 1 0 |
    | 0 6 9 | 0 3 0 | 0 4 0 |
    -------------------------
    | 8 5 0 | 0 0 0 | 1 0 9 |
    | 0 2 0 | 0 0 6 | 0 7 0 |
    | 0 7 6 | 0 0 1 | 0 0 0 |
    -------------------------
    | 5 1 7 | 2 0 0 | 0 0 0 |
    | 6 0 0 | 5 1 0 | 9 0 7 |
    | 4 0 0 | 3 0 0 | 0 2 1 |
    -------------------------
    solving...(can take seconds or hours)
    -------------------------
    | 3 8 1 | 4 7 5 | 2 9 6 |
    | 7 4 5 | 6 9 2 | 8 1 3 |
    | 2 6 9 | 1 3 8 | 7 4 5 |
    -------------------------
    | 8 5 4 | 7 2 3 | 1 6 9 |
    | 1 2 3 | 9 5 6 | 4 7 8 |
    | 9 7 6 | 8 4 1 | 3 5 2 |
    -------------------------
    | 5 1 7 | 2 8 9 | 6 3 4 |
    | 6 3 2 | 5 1 4 | 9 8 7 |
    | 4 9 8 | 3 6 7 | 5 2 1 |
    -------------------------
    press enter to exit

There is no guarantee that this algorithem will find a solution in reasonable time, but it mostly does in seconds or find out that there is no solution.
