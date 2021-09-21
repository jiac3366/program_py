# -*- coding: utf-8 -*-
def validateStackSequences(pushed, popped) -> bool:
    if not (pushed and popped):
        return True
    if not pushed or not popped:
        return False
    stack = []
    for i in range(len(pushed)):
        stack.append(pushed[i])
        # 当遇到预想出栈元素时
        while stack and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
    while stack and popped:
        if stack.pop() != popped.pop(0):
            return False
    return True


if __name__ == '__main__':
    print(validateStackSequences(
        [2, 1, 0],
        [1, 2, 0]))
