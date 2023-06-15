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
        letter_index = symbols.find(letter)

        if letter_index != -1:
            txt_index.append(str(letter_index))
        else:
            txt_index.append(letter)

    return txt_index


def get_chars_numbers(txt):
    return [str(index + 1) for index in range(len(txt))]


def get_text_parts(txt):
    len_txt = len(txt)
    if len_txt % 2 == 1:
        txt += 'ъ'

    parts = []

    for i in range(0, len_txt, 2):
        if txt[i] == txt[i + 1]:
            parts.extend((f'{txt[i]}ъ', f'{txt[i]}ъ'))
        else:
            parts.append(txt[i: i + 2])

    return parts


def get_text_blocks(txt, block_size, num_blocks):
    if len(txt) != num_blocks * block_size:
        return []
    blocks = []
    for i in range(num_blocks):
        block = []
        for j in range(block_size):
            index = i * block_size + j
            block.append(txt[index])
        blocks.append(block)
    return blocks
