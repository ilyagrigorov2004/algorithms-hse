from timer import timer

@timer
def merge_sort_iter(arr):
    n = len(arr)
    if n <= 1:
        return arr[:]
    result = arr[:]
    buf = [0] * n
    width = 1
    while width < n:
        for left in range(0, n, 2 * width):
            mid   = min(left + width, n)
            right = min(left + 2 * width, n)
            i, j, k = left, mid, left
            while i < mid and j < right:
                if result[i] <= result[j]:
                    buf[k] = result[i]; i += 1
                else:
                    buf[k] = result[j]; j += 1
                k += 1
            while i < mid:
                buf[k] = result[i]; i += 1; k += 1
            while j < right:
                buf[k] = result[j]; j += 1; k += 1
        result, buf = buf, result
        width *= 2
    return result