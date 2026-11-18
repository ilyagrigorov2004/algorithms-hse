
def find_kth_largest(nums, k):
    n = len(nums)
    if not (1 <= k <= n):
        raise ValueError(f"k={k} вне диапазона [1, {n}]")

    a = nums[:]
    target = n - k
    lo, hi = 0, n - 1

    while True:
        if lo == hi:
            return a[lo]

        pivot = a[(lo + hi) // 2]

        i, j = lo, hi
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        if target <= j:
            hi = j
        elif target >= i:
            lo = i
        else:
            return a[target]