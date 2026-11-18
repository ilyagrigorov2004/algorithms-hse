from timer import timer


def _quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, middle, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    return _quick_sort(left) + middle + _quick_sort(right)


@timer
def quick_sort(arr):
    return _quick_sort(arr)