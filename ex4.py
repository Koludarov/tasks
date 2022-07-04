"""
Задача №4. Секция статьи "Задача №4."
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.
"""
import itertools


def bananas(s):
    result = set()

    for comb in itertools.combinations(range(len(s)), len(s) - 6):
        arr = list(s)
        print(comb, 'cpo,d')

        for i in comb:
            print(arr)
            arr[i] = '-'

        adding = ''.join(arr)

        if adding.replace('-', '') == 'banana':
            result.add(adding)
    return result


if __name__ == '__main__':
    print(bananas('bananana'))
    """assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}"""
