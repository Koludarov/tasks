"""
Задача №1. Секция статьи "Задача №1."
Написать метод domain_name, который вернет домен из url адреса:
"""


def domain_name(url):
    if url.startswith('https://') or url.startswith('http://'):
        ind = url.index('/') + 2
        url2 = url[ind:]
        name = url2.split('.')
        if 'www.' in url2:
            url3 = str(name[1])
            return url3
        else:
            url3 = str(name[0])
            return url3
    elif url.startswith('www.'):
        name = url.split('.')
        url3 = str(name[1])
        return url3
    else:
        name = url.split('.')
        url4 = str(name[0])
        return url4


if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
