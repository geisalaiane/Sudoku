
# Sudoku
# Inteligência Artificial - Professor Favan
# Geísa e Fabrício

# Importação das bibliotecas.
# Random pra gerar o tabuleiro aleatório, numpy pro print da matriz
import random
import numpy

# Função apenas pra deixar o print do tabuleiro bonito,
# pode usar apenas o numpy para mostrar a matriz organizada
def Printgrid(Grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(Grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)

# =======   AMBIENTE   ==========
# Criando tabuleiro gerado aleatoriamente

def gera_sudoku():
    Grid = [[0 for x in range(9)] for y in range(9)]
            
    for i in range(9):
        for j in range(9):
            Grid[i][j] = 0
            
    for i in range(12):
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not validacao_aleatorio(Grid,row,col,num) or Grid[row][col] != 0): 
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        Grid[row][col]= num;
    return (Grid)

def validacao_aleatorio(Grid,row,col,num):
    #check if in row
    valid = True
    #check row and collumn
    for x in range(9):
        if (Grid[x][col] == num):
            valid = False
    for y in range(9):
        if (Grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            #check if section is valid
            if(Grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid

Grade = gera_sudoku()
#print (Grade)

# Tabuleiros escolhidos previamente
Tab_def = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]


Tab_def_hard1 = [[0,8,0,4,7,9,0,0,2],
         [0,0,7,0,0,2,0,0,0],
         [0,0,0,5,0,0,0,6,4],
         [2,4,3,0,0,7,0,0,0],
         [8,0,0,9,1,0,0,0,0],
         [0,0,1,0,0,0,0,0,0],
         [6,0,0,3,0,5,0,0,0],
         [0,0,8,0,0,0,0,0,9],
         [3,7,0,0,9,1,2,0,0]]

Tab_def_hard2 = [[0,0,0,0,0,6,0,0,0],
         [9,3,0,5,0,0,0,0,0],
         [0,0,0,0,0,0,8,9,1],
         [0,0,0,0,0,0,0,1,0],
         [5,0,0,4,0,0,0,0,7],
         [0,6,0,9,1,0,2,5,0],
         [0,7,0,0,0,0,5,0,0],
         [2,0,0,0,6,0,4,0,0],
         [8,5,0,0,0,4,0,0,2]]

Tab_def_expert = [[0,0,0,1,0,0,0,7,0],
         [0,3,0,0,0,0,0,6,0],
         [0,0,2,0,6,4,5,0,0],
         [0,0,0,0,0,0,0,4,0],
         [0,5,0,0,0,0,0,0,0],
         [0,0,0,2,0,6,8,9,1],
         [0,0,0,9,0,0,0,0,7],
         [8,6,5,0,2,0,0,0,0],
         [0,0,1,0,0,3,0,0,0]]

# =========   Sensor   ==========

def busca_vazio(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1


# =========   Atuador    ============

def validacao(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3)
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solucao_sudoku(grid, i=0, j=0):
        i,j = busca_vazio(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if validacao(grid,i,j,e):
                        grid[i][j] = e 
                        if solucao_sudoku(grid, i, j):
                                return True, grid
                        grid[i][j] = 0
        return False

Printgrid(Tab_def_hard1)
Tab_def_hard1=solucao_sudoku(Tab_def_hard1)
print ('Resolvido:')
Printgrid(Tab_def_hard1[1])

# Para resolver os outro tabuleiros usar:

#Tab_def=solucao_sudoku(Tab_def)
#print (numpy.array(Tab_def[1]))


#Tab_def3=solucao_sudoku(Tab_def3)
#print (numpy.array(Tab_def3[1]))


#print (numpy.array(Grade))
#Grid=solucao_sudoku(Grade)
#print (numpy.array(Grid[1]))