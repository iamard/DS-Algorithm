def isLegalMove(nextX, nextY, table):
    if nextX >= 0 and \
       nextX < 8 and \
       nextY >= 0 and \
       nextY < 8 and \
       table[nextX][nextY] == -1:
       return True
    return False

def findSolution(curX, curY, step, xMove, yMove, table):
    if step == (8 * 8):
        return True
    else:
        for i in range(8):
            nextX = curX + xMove[i]
            nextY = curY + yMove[i]
            if isLegalMove(nextX, nextY, table):
                table[nextX][nextY] = step
                if (findSolution(nextX, nextY, step + 1, xMove, yMove, table)):
                    return True
                else:
                    table[nextX][nextY] = -1
    return False
                    
def printTour(table):
    for i in range(8):
        print(table[i])
                    
def knightTour():
    table = [[-1 for x in range(8)] for x in range(8)]

    xMove = [ 2, 1, -1, -2, -2, -1,  1,  2]
    yMove = [ 1, 2,  2,  1, -1, -2, -2, -1]

    table[0][0] = 0

    if (findSolution(0, 0, 1, xMove, yMove, table)):
        printTour(table)

if __name__ == "__main__":
    knightTour()
