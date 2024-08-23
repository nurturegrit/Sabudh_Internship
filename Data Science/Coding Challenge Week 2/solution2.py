def segregate_numbers(array):
    pos_idx = None
    for idx, num in enumerate(array):
        if pos_idx is None and num < 0:
            continue
        elif pos_idx is None:
            pos_idx = idx
            continue
        if pos_idx is not None and num < 0:
            array[pos_idx + 1: idx + 1] = array[pos_idx: idx]  # shifting positive values 1 step right
            array[pos_idx] = num
            pos_idx += 1
    return array


def recursive_seg_nums(array):
    pos_idx = None

    def change_neg_pos(pos_idx):
        sav = array[pos_idx]
        for i in range(pos_idx + 1, len(array)):
            if array[i] >= 0:
                temp = array[i]
                array[i] = sav
                sav = temp
            else:
                array[pos_idx] = array[i]
                array[i] = sav
                return i

    for idx, num in enumerate(array):
        if pos_idx is not None:
            if change_neg_pos(pos_idx) == len(array) - 1:
                return array
            pos_idx += 1
        elif num >= 0:
            pos_idx = idx
    return array


print(recursive_seg_nums([1, 0, -1, -1, 0, 1, -2]), '\n\n')
print(segregate_numbers([1, 0, -1, -1, 0, 1, -2]))