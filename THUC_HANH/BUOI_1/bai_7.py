x = int(input())

if x < 1 or x > 30:
    print(f"So {x} khong nam trong khoang [1,30].")
else:
    a, b = 0, 1
    for i in range(2, x+1):
        a, b = b, a+b
    print(b)

