from swap_case import strip_punctuation


def test1(): assert strip_punctuation('Hello world!') == ('Helloworld', {' ': [5], '!': [11]})
