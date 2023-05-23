def repeat_on_str(txt, txt_repeat):
    result = ''
    txt_index = 0

    for symbol in txt:
        if symbol.isspace():
            result += symbol
            txt_index -= 1
        else:
            result += txt_repeat[txt_index % len(txt_repeat)]

        txt_index += 1

    return result


def get_index(txt, symbols):
    txt_index = []

    for letter in txt:
        letter_index: int = symbols.find(letter)

        if letter_index != -1:
            txt_index.append(str(letter_index))
        else:
            txt_index.append(letter)

    return txt_index


def get_number_letter(txt):
    return [str(index + 1) for index in range(len(txt))]


def get_words_len(words, len_word):
    return list(filter(lambda word: len(word) == len_word, words))