def is_prime(func):
    """
    Функция-декоратор проверяет "Простое" или "Составное" число
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0 or result == 1:
            print('Число ни простое, ни составное')
            return result
        k = 0
        for i in range(2, result // 3):
            if result % i == 0:
                k = k + 1
        if k <= 0:
            print('Простое')
            return result
        else:
            print('Составное')
            return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    """
    Функция, которая складывает 3 числа
    """
    return a + b + c


result = sum_three(0, 0, 0)
print(result)
