def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def prime_count(n):
    answer = 0
    for i in range(2, n):
        if is_prime(i):
            answer += 1
    return answer


