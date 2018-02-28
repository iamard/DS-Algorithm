def editDist(str1, m, str2, n):
    table = [[0 for x in range(0, n + 1)] for x in range(0, m + 1)]

    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif (str1[i - 1] == str2[j - 1]):
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i][j - 1],
                                      table[i - 1][j],
                                      table[i - 1][j - 1])
    return table[i][j]

if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    dist = editDist(str1, len(str1), str2, len(str2))
    print(dist)
