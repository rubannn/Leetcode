def longestValidParentheses(s: str) -> int:
    if not s:
        return 0
    i = 1
    res = ['0']
    stack = [(0, s[0])]
    while i < len(s):
        if stack and stack[-1][1] + s[i] == '()':
            x = stack.pop()
            res[x[0]] = '1'
            res.append('1')
        else:
            stack.append((i , s[i]))
            res.append('0')
        i += 1
    return len(max(''.join(res).split('0')))


tests = [["(()", 2], [")()())", 4], ["", 0], ["())", 2]]
for s, ans in tests:
    print(longestValidParentheses(s) == ans)
