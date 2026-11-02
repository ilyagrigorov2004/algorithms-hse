import functools
import sys


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