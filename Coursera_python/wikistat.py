from bs4 import BeautifulSoup
import unittest
import re


def num_1_image(body):
    """Количество картинок (img) с шириной (width) не меньше 200.
    Например: <img width="200">, но не <img> и не <img width="199">"""

    img_tags = body.findAll(name='img')
    num_of_img = 0
    for tag in img_tags:
        try:
            width = tag['width']
            if int(width) >= 200:
                num_of_img += 1
        except:
            pass
    return num_of_img


def num_2_headers(body):
    """Количество заголовков (h1, h2, h3, h4, h5, h6), первая буква текста внутри которых соответствует заглавной
    букве E, T или C. Например: <h1>End</h1> или <h5><span>Contents</span></h5>, но не <h1>About</h1> и не
    <h2>end</h2> и не <h3><span>1</span><span>End</span></h3> """

    h_tags = body.findAll(('h1', 'h2', 'h3', 'h4', 'h5', 'h6'))
    num_of_tags = 0
    for tag in h_tags:
        if tag.text[0] == 'E' \
                or tag.text[0] == 'T' \
                or tag.text[0] == 'C':
            num_of_tags += 1
    return num_of_tags


def num_3_links(body):
    """Длину максимальной последовательности ссылок, между которыми нет других тегов, открывающихся или
    закрывающихся. Например: <p><span><a></a></span>, <a></a>, <a></a></p> - тут 2 ссылки подряд, т.к. закрывающийся
    span прерывает последовательность. <p><a><span></span></a>, <a></a>, <a></a></p> - а тут 3 ссылки подряд,
    т.к. span находится внутри ссылки, а не между ссылками. """
    all_a = body.find_all('a')
    nums = [1, ]

    while all_a:
        a = all_a.pop()
        i = 1
        for sib in a.find_next_siblings():
            if sib.name == 'a':
                i += 1
            else:
                if nums[-1] < i:
                    nums.append(i)
                i = 0
            if nums[-1] < i:
                nums.append(i)

    # print(nums)
    max_num = max(nums)
    # print(f"max={max_num}")
    return max_num


def num_4_lists(body):
    """Количество списков (ul, ol), не вложенных в другие списки. Например: <ol><li></li></ol>,
    <ul><li><ol><li></li></ol></li></ul> - два не вложенных списка (и один вложенный) """
    ul_ol_tags = body.findAll(('ul', 'ol'))
    independent_tags = 0
    for tag in ul_ol_tags:
        flag = 0
        try:
            parents = tag.findParents()
            for parent in parents:
                parent_tag = parent.name
                if parent_tag == 'ol' or parent_tag == 'ul':# or parent_tag == 'li':
                    flag = 1
            if flag == 0:
                independent_tags += 1
        except:
            pass
    return independent_tags


def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        html = f.read()
        soup = BeautifulSoup(html, 'lxml')
        body = soup.find(name="div", id='bodyContent')
        imgs = num_1_image(body)
        headers = num_2_headers(body)
        linkslen = num_3_links(body)
        lists = num_4_lists(body)
        print([imgs, headers, linkslen, lists], path_to_file)
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    # def test_parse(self):
    #     test_cases = (
    #         ('wiki/608_(number)', [0, 1, 12, 120]),
    #         ('wiki/Spectrogram', [1, 2, 4, 7]),)

    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Social_theory', [0, 8, 12, 10]),
            ('wiki/608_(number)', [0, 1, 12, 120]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
