# -*- coding: utf-8 -*-
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    operator = ['+', '-', '*', '/']
    num_stack = []
    operator_stack = []
    operator_map = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue

        if s[i] not in operator:  # 数字
            number = 0
            while i < len(s) and s[i].isdigit():
                number = number * 10 + int(s[i])
                i += 1
            num_stack.append(number)

        else:  # 符号
            if operator_stack:
                # 取栈顶符号优先级比较一下
                # 如果小于当前栈顶优先级 就可以清空一下栈了
                # 而且要放在while 条件中—— 因为！！！不可能一次遇到栈顶符号优先级小于当前栈顶优先级就可以一下子全部清空栈了！
                # 比如：1+2*5/3+6/4*2 的 * /连在一起了
                while operator_stack and operator_map[operator_stack[-1]] >= operator_map[s[i]]:
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    op = operator_stack.pop()
                    num_stack.append(op_res(num1, num2, op))
                # 记得清空完把最新符号压进去，这里是简便下法 因为每一层的else都需要operator_stack.append(i)

            operator_stack.append(s[i])
            i += 1

    while operator_stack:
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        op = operator_stack.pop()
        num_stack.append(op_res(num1, num2, op))
    return num_stack[0]


def op_res(n1, n2, op):
    n1 = int(n1)
    n2 = int(n2)
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return int(n1 / n2)


if __name__ == '__main__':
    print(calculate("1+2*5/3+6/4*2"))
