#Viết chương trình nhập số nguyên dương x.

#Nếu x là số chẵn thì in ra màn hình số 0, nếu x là số lẻ thì in ra màn hình số 1.

#Số nguyên dương x có giá trị tuyệt đối không vượt quá 10^9.

x = int(input())


if x % 2 == 0 and x != 0 and x < 10**9:
    print(0)
if x % 2 != 0 and x != 0 and x < 10**9:
    print(1)
if x == 0:
    print(0)
