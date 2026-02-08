def Sudoku_Tester(list):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # row check
    for i in range(0, 8):
        for j in range(0, 8):
            if list[i][j] in num:
                num.remove((list[i][j]))
            else:
                print("This is an Invalid Sudoku Solution")
                exit(0)
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("The rows are all correct")
    # column check
    for i in range(0, 8):
        for j in range(0, 8):
            if list[j][i] in num:
                num.remove((list[j][i]))
            else:
                print("This is an Invalid Sudoku Solution")
                exit(0)
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("The columns are all correct")
    # box check
    for x in range(0, 3):
        for y in range(0, 3):
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for x1 in range(0, 3):
                for y1 in range(0, 3):
                    if list[x*3+x1][y*3+y1] in num:
                        num.remove((list[x*3+x1][y*3+y1]))
                    else:
                        print("This is an Invalid Sudoku Solution")
                        exit(0)
    print("The boxes are all correct")
    print("This Sudoku is Correct")


Sudoku_Tester([[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 4, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]])

Sudoku_Tester([[1, 2, 3, 4, 5, 6, 7, 8, 9],
               [2, 3, 4, 5, 6, 7, 8, 9, 1],
               [3, 4, 5, 6, 7, 8, 9, 1, 2],
               [4, 5, 6, 7, 8, 9, 1, 2, 3],
               [5, 6, 7, 8, 9, 1, 2, 3, 4],
               [6, 7, 8, 9, 1, 2, 3, 4, 5],
               [7, 8, 9, 1, 2, 3, 4, 5, 6],
               [8, 9, 1, 2, 3, 4, 5, 6, 7],
               [9, 1, 2, 3, 4, 5, 6, 7, 8],])