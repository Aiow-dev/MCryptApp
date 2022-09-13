from typing import Iterable, List

from Assets import constants


def repeat_on_str(txt: str, txt_repeat: str) -> str:
    text = ''
    txt_index = 0

    for symbol in txt:
        if symbol.isspace():
            text += symbol
            txt_index -= 1
        else:
            text += txt_repeat[txt_index % len(txt_repeat)]

        txt_index += 1

    return text


def get_index(txt: Iterable[str], symbols: str) -> List[str]:
    txt_index: List[str] = []

    for letter in txt:
        letter_index: int = symbols.find(letter)

        if letter_index != -1:
            txt_index.append(str(letter_index))
        else:
            txt_index.append(letter)

    return txt_index


if __name__ == '__main__':
    print(repeat_on_str('Синтаксис', 'новая'))
    print(get_index(repeat_on_str('прилетаю десятого', 'работа'), constants.RU_ALPHABET))
    print(constants.RU_ALPHABET)
