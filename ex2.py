"""
Задача №2. Секция статьи "Задача №2."
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса:
"""


def int32_to_ip(int32):
    nums1 = int(int32 / 16777216) % 256
    nums2 = int(int32 / 65536) % 256
    nums3 = int(int32 / 256) % 256
    nums4 = int(int32) % 256
    answer = f'{nums1}.{nums2}.{nums3}.{nums4}'
    return answer


if __name__ == '__main__':
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"
