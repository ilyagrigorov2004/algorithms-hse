def validate(pushed: list, popped: list):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return len(stack) == 0

print(validate([1,2,3,4,5], [1,3,5,4,2]))  # True
print(validate([1,2,3], [3,1,2]))          # False
print(validate([1,2], [2,1]))              # True
print(validate([1,2], [1,2]))              # True
print(validate([1], [1]))                  # True