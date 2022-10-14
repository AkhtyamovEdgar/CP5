print('Введите число: ')
n = int(input())
print('Введите целевую систему счисления: ')
cc = int(input())

def f(n):
    res = ''
    while n > 0:
        res += str(n % cc)
        n //=  cc
    return res
print(n, '==>', f(n))