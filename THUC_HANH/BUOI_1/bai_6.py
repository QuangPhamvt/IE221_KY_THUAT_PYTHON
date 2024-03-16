
n,m,h,w = map(float, input().split())


if n <= h and m <= w:
    print(0)
else:
    count = 0
    new_n = n
    new_m = m

    second_count = 0

    while new_n > h:
        new_n /=2
        count += 1
    while new_m > w:
        new_m/=2
        count += 1

    n, m = m,n
    while n > h:
        n = n / 2
        second_count += 1
    while m > w:
        m = m / 2
        second_count += 1

    print(min(count, second_count))






