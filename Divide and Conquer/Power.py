def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power(x, y / 2) * power(x, y / 2)
    else:
        return x * power(x, int(y / 2)) * power(x, int(y / 2))

if __name__ == "__main__":
    value = power(3, 3)
    print(value)
