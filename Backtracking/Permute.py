def permute(str, left, right):
    if (left == right):
        print(''.join(str))
    for i in range(left, right + 1):
        str[left], str[i] = str[i], str[left]
        permute(str, left + 1, right)
        str[left], str[i] = str[i], str[left]

if __name__ == "__main__":
    string = "ABC"
    permute(list(string), 0, len(string) - 1)
