import functools
import sys


# декоратор скопирован из tracer.py
def tracer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        depth = 0
        frame = sys._getframe()
        while frame:
            if frame.f_code == wrapper.__code__:
                depth += 1
            frame = frame.f_back

        indent = "    " * depth
        args_str = ", ".join(map(str, args))

        print(f"{indent}-> {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"{indent}<- {func.__name__}({args_str}) = {result}")

        return result

    return wrapper


@tracer
def generate_permutations(nums: list, current: list = None, result: list = None) -> list:

    if result is None:
        result = []
    if current is None:
        current = []

    if len(current) == len(nums):
        result.append(current.copy())
        return result

    for num in nums:
        if num not in current:
            current.append(num)
            generate_permutations(nums, current, result)
            current.pop()

    return result


def permutations(nums: list) -> list:
    """Обертка для вызова без визуализации для чистоты тестов"""
    return generate_permutations(nums)