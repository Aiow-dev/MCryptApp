# def repeat_on_str(txt: str, txt_repeat: str) -> str:
#     return ''.join(txt_repeat[number % len(txt_repeat)] for number in range(len(txt.replace(' ', ''))))
from typing import Iterable, List

from Core.Helpers import constants


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


# def repeat_str(txt, txt_repeat):
#     len_txt = len(txt)
#     len_txt_repeat = len(txt_repeat)
#
#     number_repeat = math.ceil(len_txt / len_txt_repeat)
#     result = txt_repeat * number_repeat
#
#     offset = -((len_txt_repeat * number_repeat) - len_txt)
#
#     return result if len(result) == len_txt else result[:offset]


# def repeat_on_str(txt: str, txt_repeat: str) -> str:
#     len_txt: int = len(txt)
#     len_txt_repeat: int = len(txt_repeat)
#
#     number_repeat: int = len_txt // len_txt_repeat
#     repeat_str: str = txt_repeat * number_repeat
#
#     offset: int = len_txt - len(repeat_str)
#
#     return repeat_str + txt_repeat[:offset]


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
