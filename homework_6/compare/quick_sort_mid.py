from timer import timer


def _quick_sort_mid(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return _quick_sort_mid(left) + middle + _quick_sort_mid(right)


@timer
def quick_sort_mid(arr):
    return _quick_sort_mid(arr)