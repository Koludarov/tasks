"""
Задача №3. Секция статьи "Задача №3."
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) заданного числа:
"""


def zeros(n):
    if n == 0:
        return 0
    else:
        answer = 0
        while n > 0:
            answer += n // 5
            n //= 5
    return answer


if __name__ == '__main__':
    print(zeros(50))
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
