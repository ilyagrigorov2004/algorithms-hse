from timer import timer


@timer
def quick_sort_iter(arr):
    a = arr[:]
    if len(a) <= 1:
        return a
    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        pivot = a[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while a[i] < pivot: i += 1
            while a[j] > pivot: j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1; j -= 1
        # меньший подмассив кладём в стек последним — так стек мельче
        if j - lo < hi - i:
            if lo < j: stack.append((lo, j))
            if i < hi: stack.append((i, hi))
        else:
            if i < hi: stack.append((i, hi))
            if lo < j: stack.append((lo, j))
    return a