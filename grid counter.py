
grid = []
rowArray =[]
columnArray = []
diagonalArray = []


#This creates the grid from which the counting will be done
def formGrid(numRows, numColumns):
    count = 1
    for hori in range(numRows):
        row =[]
        for vert in range(numColumns):
            row.append(count)
            count +=1
        grid.append(row)


#This function array for the row
def rowCount(row, column):
    for hori in range(row):
        for vert in range(column):
            temp = []
            if (column - vert) > 2:
                for i in range(3):
                    temp.append( grid[hori][vert + i] )
                rowArray.append(temp)



#This function array for the column
def columnCount(row, column):
    for vert in range(column):
        for hori in range(row):
            temp = []
            if (row - hori) > 2 :
                for i in range(3):
                    temp.append( grid[hori + i][vert] )
                columnArray.append(temp)


#This generates the arrays from the grid diagonal
def diagonalCount(row, column):
    for vert in range(column):
        for hori in range(row):
            temp = []
            if (column - vert) > 2 and (row - hori) > 2:
                for i in range(3):
                    temp.append(grid[hori+i][vert+i])
                diagonalArray.append(temp)






#This displays the results of the program
def display():
    for row in grid:
        for i in row:
            print("{:^5}".format(str(i)), end = "")
        print()
    print("row")
    for row in rowArray:
        print(row)


    print("column")
    for col in columnArray:
        print(col)

    print("diagonal")
    for dia in diagonalArray:
        print(dia)


















#This function runs the program
def main(rows, columns):
    formGrid(rows, columns)
    rowCount(rows, columns)
    columnCount(rows, columns)
    diagonalCount(rows, columns)
    display()

nRow, nColumn = int(input("Enter the number of rows: ")), int(input("Enter the number of column: "))

main(nRow, nColumn)
