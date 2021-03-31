def numOfWays(a, b):
    n = len(a)
    m = len(b)

    if m == 0:
        return 1

    new = [[0] * (n) for _ in range(m)]

    for i in range(m):

        for j in range(i, n):

            if i == 0:
                if j == 0:
                    if a[j] == b[i]:
                        new[i][j] = 1
                    else:
                        new[i][j] = 0
                elif a[j] == b[i]:
                    new[i][j] = new[i][j - 1] + 1
                else:
                    new[i][j] = new[i][j - 1]

            # Filling other rows
            else:
                if a[j] == b[i]:
                    new[i][j] = new[i][j - 1] + new[i - 1][j - 1]
                else:
                    new[i][j] = new[i][j - 1]
    print(new)
    return new[m - 1][n - 1]


# Driver Code
if __name__ == "__main__":
    a = input("wrong word: ")
    b = input("correct word: ")
    print(numOfWays(a, b))
