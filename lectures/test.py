# Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок правильной.

from collections import deque

def brackets(line):
    # Напишите тело функции
    ss = deque()
    for s in line:
        if s == '(':
            ss.append(s)
        elif s == ")":
            if len(ss) == 0:
                return False
            ss.popleft()
    if len(ss) > 0:
        return False
    return True
            


print(brackets("(()())"))
# True
print(brackets(""))
# True
print(brackets("(()()))"))
print(brackets(")("))