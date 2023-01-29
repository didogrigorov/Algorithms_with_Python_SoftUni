array = [int(x) for x in input().split()]


def selectionSort(array):
    for idx in range(len(array)):
        min_idx = idx

        for curr_idx in range(idx + 1, len(array)):
            if array[curr_idx] < array[min_idx]:
                min_idx = curr_idx

        array[idx], array[min_idx] = array[min_idx], array[idx]

    return array


print(selectionSort(array))
