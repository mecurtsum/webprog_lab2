def palindrome(x):
    a = list(map(int, str(x)))
    b = a.copy()
    a.reverse()
    if (a == b):
        return True
    else:
        return False
print('Введите число, чтобы проверить, является ли оно палиндромом')
val = input()
res = palindrome(val)
print(res)

