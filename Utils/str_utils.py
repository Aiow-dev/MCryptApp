from typing import Iterable, List


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


def get_number_letter(txt: str) -> List[str]:
    return [str(index + 1) for index in range(len(txt))]
