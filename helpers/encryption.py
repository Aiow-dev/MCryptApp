from helpers import items


def check_magic_square(magic_square):
    row_len = len(magic_square)
    clm_len = len(magic_square[0])

    if row_len != clm_len:
        return False

    elements = []
    sums_row = []
    sums_clm = []
    sum_left_diagonal = 0
    sum_right_diagonal = 0

    for row_index in range(row_len):
        sum_row = 0
        sum_clm = 0
        for clm_index in range(clm_len):
            if not magic_square[row_index][clm_index]:
                return False

            elements.append(magic_square[row_index][clm_index])
            sum_row += magic_square[row_index][clm_index]
            sum_clm += magic_square[clm_index][row_index]
            if row_index == clm_index:
                sum_left_diagonal += magic_square[row_index][clm_index]
            if row_index + clm_index == clm_len - 1:
                sum_right_diagonal += magic_square[row_index][clm_index]
        sums_row.append(sum_row)
        sums_clm.append(sum_clm)

    if not items.all_equal(sums_row) and not items.all_equal(sums_clm):
        return False

    return sum_left_diagonal == sum_right_diagonal and items.is_serial(sorted(elements))
