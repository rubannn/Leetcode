# varianr 1 (120 ms, 16.7 MB)
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for c in tokens:
        # print(stack, c)
        if c in "+-*/":
            if c == "/":
                val = eval(f"{stack[-2]}//{stack[-1]}")
                if val < 0 and (int(stack[-2]) % int(stack[-1]) != 0):
                    val += 1
            else:
                val = eval(f"{stack[-2]}{c}{stack[-1]}")
            stack[-2] = str(val)
            stack.pop()
        else:
            stack.append(c)
    return int(stack[0])


# varianr 2 (63 ms, 17.2 MB)
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for c in tokens:
        if c in "+-*/":
            if c == "/":
                val = stack[-2] // stack[-1]
                if val < 0 and (stack[-2] % stack[-1]) != 0:
                    val += 1
            elif c == "+":
                val = stack[-2] + stack[-1]
            elif c == "-":
                val = stack[-2] - stack[-1]
            elif c == "*":
                val = stack[-2] * stack[-1]
            stack[-2] = val
            stack.pop()
        else:
            stack.append(int(c))
    return stack[0]


t = ["2", "1", "+", "3", "*"]
res = 9
print(evalRPN(t) == res)

t = ["4", "13", "5", "/", "+"]
res = 6
print(evalRPN(t) == res)

t = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
res = 22
print(evalRPN(t) == res)

t = [
    "-78",
    "-33",
    "196",
    "+",
    "-19",
    "-",
    "115",
    "+",
    "-",
    "-99",
    "/",
    "-18",
    "8",
    "*",
    "-86",
    "-",
    "-",
    "16",
    "/",
    "26",
    "-14",
    "-",
    "-",
    "47",
    "-",
    "101",
    "-",
    "163",
    "*",
    "143",
    "-",
    "0",
    "-",
    "171",
    "+",
    "120",
    "*",
    "-60",
    "+",
    "156",
    "/",
    "173",
    "/",
    "-24",
    "11",
    "+",
    "21",
    "/",
    "*",
    "44",
    "*",
    "180",
    "70",
    "-40",
    "-",
    "*",
    "86",
    "132",
    "-84",
    "+",
    "*",
    "-",
    "38",
    "/",
    "/",
    "21",
    "28",
    "/",
    "+",
    "83",
    "/",
    "-31",
    "156",
    "-",
    "+",
    "28",
    "/",
    "95",
    "-",
    "120",
    "+",
    "8",
    "*",
    "90",
    "-",
    "-94",
    "*",
    "-73",
    "/",
    "-62",
    "/",
    "93",
    "*",
    "196",
    "-",
    "-59",
    "+",
    "187",
    "-",
    "143",
    "/",
    "-79",
    "-89",
    "+",
    "-",
]
res = 165
print(evalRPN(t) == res)

t = ["4", "-2", "/", "2", "-3", "-", "-"]
res = -7
print(evalRPN(t) == res)
