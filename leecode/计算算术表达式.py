in_str = "(1+((2+3)*(4*5)))"

if __name__ == '__main__':
    op_stack = []
    num_stack = []

    for item in in_str:
        if item == "(":
            continue
        elif item == "+" or item == "*" or item == "-" or item == "/":
            op_stack.append(item)
        elif item == ")":
            # 运算符出一次 操作数出2次
            num1 = num_stack.pop()
            op = op_stack.pop()
            if op == "+":
                num_stack.append(num_stack.pop() + num1)
            if op == "-":
                num_stack.append(num_stack.pop() - num1)
            if op == "*":
                num_stack.append(num_stack.pop() * num1)
            if op == "/":
                num_stack.append(num_stack.pop() / num1)
        else:
            num_stack.append(int(item))

    print(op_stack)
    print(num_stack)

