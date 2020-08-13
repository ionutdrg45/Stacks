from stack import Stack

stack = Stack()
print(stack.is_empty())

for i in range(1, 11):
    stack.push(i)

print(stack.items)

stack2 = Stack()

for c in "Hello World!":
    stack2.push(c)

reversed_string = ""
for i in range(len(stack2.items)):
    reversed_string += stack2.pop()

print(reversed_string)
