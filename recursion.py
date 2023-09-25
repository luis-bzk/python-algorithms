def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


print(iterative_factorial(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n - 1)
        temp = temp * n
    return temp


print(recur_factorial(5))


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


def list_sum(x_list):
    if not x_list:
        return 0
    else:
        return x_list[0] + list_sum(x_list[1:])


def calc_power_num(base, exp_num):
    if exp_num == 0:
        return 1
    else:
        return base * calc_power_num(base, exp_num - 1)


def countdown(n):
    if n == 0:
        return
    else:
        print(n)
        countdown(n - 1)


def decimal_to_binary(n):
    if n <= 1:
        return str(n)
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
