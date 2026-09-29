'''def f(arr: list, k: int):
    for i in range(len(arr)-1):
        r = k - arr[i]
        for j in range(i+1, len(arr)):
            if r == arr[j]:
                return str(i) + ' ' + str(j)'''


def two_sum_hash(arr: list, k: int):
    d = {}
    for i in range(len(arr)):
        elem = k - arr[i]
        if elem in d:
            return (d[elem], i)
        else:
            d[arr[i]] = i
    return None


def two_sum_brute(arr: list, k: int):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                return (i, j)
    return None

#print(two_sum_hash([5, 5, 1, 4], 10))

