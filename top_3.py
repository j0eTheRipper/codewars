import string


def top_3_words(txt: str):
    txt = format_txt(txt.lower())
    word_count_dict = count_word_occurrences(txt)
    return get_top_3(word_count_dict)


def count_word_occurrences(txt: list):
    """Returns a dictionary with keys as words and values as count of occurrences in the text."""
    txt_unrepeated = set(txt)
    repeated_words = {}

    for word in txt_unrepeated:
        if txt.count(word) not in repeated_words.values() and isword(word):
            repeated_words[word] = txt.count(word)

    return repeated_words


def format_txt(txt: str):
    """Removes all the punctuation in the txt and returns a list of just the words."""

    string.punctuation = string.punctuation.replace("'", '\n')

    for punctuation in string.punctuation:
        if punctuation in txt:
            txt = txt.replace(punctuation, '')
    else:
        return txt.split()


def get_top_3(words_occurrences: dict):
    """Returns a list of the highest 3 occurring words given a dictionary of words: occurrences"""
    result = []
    range_ = 3 if len(words_occurrences) >= 3 else len(words_occurrences)

    for _ in range(range_):
        highest_word = get_max_item(words_occurrences)
        result.append(highest_word)
        del words_occurrences[highest_word]

    return result


def get_max_item(dictionary: dict):
    result = ''
    max_number = 0

    for word, occurrences in dictionary.items():
        if occurrences > max_number:
            result = word
            max_number = occurrences

    return result


def isword(txt: str):
    for char in set(txt):
        if char in string.ascii_lowercase:
            return True
    else:
        return False


if __name__ == '__main__':
    print(top_3_words("srGGNpKk _ ,AQxdWxr./AQxdWxr,AQxdWxr:,!AQxdWxr?!:srGGNpKk!,?-:AQxdWxr-!, ;AQxdWxr,xngwlwhfET/AQxdWxr?__ .srGGNpKk;-, AQxdWxr!_,!?AQxdWxr--AQxdWxr_!,//AQxdWxr_?!.xngwlwhfET AQxdWxr ;!!xngwlwhfET:.!:,xngwlwhfET;AQxdWxr_ AQxdWxr,?AQxdWxr.,xngwlwhfET,/xngwlwhfET-;/AQxdWxr;- AQxdWxr!xngwlwhfET_! :?AQxdWxr/:xngwlwhfET?-._.xngwlwhfET;AQxdWxr?AQxdWxr-,AQxdWxr! !.AQxdWxr-_AQxdWxr!-?AQxdWxr?;!:/xngwlwhfET;_:?!AQxdWxr,_AQxdWxr,;/??xngwlwhfET!/. xngwlwhfET.?AQxdWxr-?.?"))
