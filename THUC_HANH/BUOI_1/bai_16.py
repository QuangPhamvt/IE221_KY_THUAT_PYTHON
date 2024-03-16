n = int(input())

arr = []
for i in range(n):
    tranfer_type, tranfer = map(str, input().split())
    arr.append([tranfer_type, tranfer])

sum = 0
for i in range(n):
    if arr[i][0] == 'D':
        sum += int(arr[i][1])
    if arr[i][0] == 'W':
        sum -= int(arr[i][1])


print(sum)



