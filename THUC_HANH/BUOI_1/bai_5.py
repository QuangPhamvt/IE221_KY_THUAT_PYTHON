x = input()

def check(x):
    count = 0

    for i in str(x):
        if i == '4' or i == '7':
            count += 1

    for i in str(count):
        if i != '4' and i != '7':
            return False
    return True

print("YES" if check(x) else "NO")

