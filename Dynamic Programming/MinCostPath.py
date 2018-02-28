def minCostPath(cost, m, n):
    table = [[0 for x in range(n + 1)] for x in range(m + 1)]

    table[0][0] = cost[0][0]

    for i in range(0, m + 1):
        table[i][0] = table[i - 1][0] + cost[i][0]

    for j in range(0, n + 1):
        table[0][j] = table[0][j - 1] + cost[0][j]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = min(table[i][j - 1],
                              table[i - 1][j],
                              table[i - 1][j - 1]) + cost[i][j]
    return table[m][n]

if __name__ == "__main__":
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    value = minCostPath(cost, 2, 2)
    print(value)
