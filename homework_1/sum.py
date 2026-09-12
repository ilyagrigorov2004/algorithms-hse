def max_even_sum(arr):
    s = 0
    min_odd = float('inf')
    for x in arr:
        s += x
        if x % 2 != 0 and x < min_odd:
            min_odd = x
    if s % 2 == 0:
        return s
    else:
        return s - min_odd




