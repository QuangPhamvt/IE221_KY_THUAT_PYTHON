
n = []
for i in range(5):
    n.append(list(map(int, input().split())))

def check(n):
    for i in range(5):
        for j in range(5):
            if n[i][j] == 1:
                x, y = i, j
                sum = abs(x - 2) + abs(y - 2)
                return sum

print(check(n))








