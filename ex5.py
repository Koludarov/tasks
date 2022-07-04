"""
Задача №5. Секция статьи "Задача №5."
Написать метод count_find_num, который принимает на вход список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые множители простых чисел primesL.
"""


def count_find_num(primesL, limit):
    answer = primesL[0]
    i = 1
    while i < len(primesL):
        answer *= primesL[i]
        i += 1
    digits = {answer}
    if answer > limit:
        return []
    resh = answer
    j = 0
    while j < len(primesL):
        while resh <= limit:
            resh *= primesL[j]
            if j < len(primesL)-1:
                resh2 = resh * primesL[j+1]
                n = 0
                if j < len(primesL) - 1:
                    while j + n < len(primesL) - 1:
                        resh4 = resh2 * primesL[j + n]
                        while resh4 <= limit:
                            digits.add(resh4)
                            resh4 *= primesL[j + n]
                        if n < len(primesL) - 1:
                            n += 1
                while resh2 <= limit:
                    digits.add(resh2)
                    resh2 *= primesL[j+1]
            n = 0
            if j < len(primesL) - 1:
                while n <= len(primesL) - 1:
                    if j + n <= len(primesL) - j:
                        resh4 = resh * primesL[j+n]
                        t = 0
                        if j < len(primesL) - 1:
                            while j + t < len(primesL) - 1:
                                resh3 = resh4 * primesL[j + t]
                                while resh3 <= limit:
                                    digits.add(resh3)
                                    resh3 *= primesL[j + t]
                                if t < len(primesL) - 1:
                                    t += 1
                        while resh4 <= limit:
                            digits.add(resh4)
                            resh4 *= primesL[j + n]
                    if n < len(primesL) - j:
                        n += 1
                    else:
                        break
            if resh <= limit:
                digits.add(resh)
        resh = answer
        j += 1
    answer = [len(digits), max(digits)]
    return answer


if __name__ == '__main__':
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
