n = int(input())


def sum_div(number):
    sum_div = 0
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            sum_div += i
            if i != number//i and i != 1:
                sum_div += number//i
    return sum_div

print(sum_div(n))
