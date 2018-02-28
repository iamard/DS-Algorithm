def isLegalMove(nextX, nextY, maze):
    if nextX >= 0 and \
       nextX < 4 and \
       nextY >= 0 and \
       nextY < 4 and \
       maze[nextX][nextY] == 1:
        return True
    return False

def solveMaze(maze, curX, curY, xMove, yMove, table):
    if curX == 3 and curY == 3:
        return True
    else:
        for i in range(len(xMove)):
            nextX = curX + xMove[i]
            nextY = curY + yMove[i]
            if isLegalMove(nextX, nextY, maze):
                table[nextX][nextY] = 1
                if solveMaze(maze, nextX, nextY, xMove, yMove, table):
                    return True
                table[nextX][nextY] = 0
                
    return False

def printPath(table):
    for i in range(4):
        print(table[i])    

def ratInMaze(maze):
    table = [[0 for x in range(4)] for x in range(4)]
    
    xMove = [ 1, 0 ]
    yMove = [ 0, 1 ]

    table[0][0] = 1
    if solveMaze(maze, 0, 0, xMove, yMove, table):
        printPath(table)

if __name__ == "__main__":
    maze = [ [1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1] ]
    ratInMaze(maze)
