def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()


def top(stack):
    if check_empty(stack):
        raise IndexError("Stack is empty")
    return stack[-1]

def clear_stack(stack):
    stack[:] = []

stack = create_stack()
push(stack, str(5))
push(stack, str(3))
print("Length of Stack:", len(stack))
print("Popped item: ", pop(stack))
# print("stack after popping an element: ", str(stack))
print("Stack is empty: ", check_empty(stack))
print("Popped item: ", pop(stack))
print("Stack is empty: ", check_empty(stack))
print("Popped item: ", pop(stack))
push(stack, str(7))
push(stack, str(9))
push(stack, str(4))
print("top item:", top(stack))
print("Length of Stack:", len(stack))
print("Popped item: ", pop(stack))
push(stack, str(6))
push(stack, str(8))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
clear_stack(stack)
print("Stack after clearing:", stack)
print("-------------------------------------")

push(stack, str(5))
print("stack elements: ", str(stack))
push(stack, str(3))
print("stack elements: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
push(stack, str(2))
print("stack elements: ", str(stack))
push(stack, str(8))
print("stack elements: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
push(stack, str(9))
print("stack elements: ", str(stack))
push(stack, str(1))
print("stack elements: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
push(stack, str(7))
print("stack elements: ", str(stack))
push(stack, str(6))
print("stack elements: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
push(stack, str(4))
print("stack elements: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
print("Popped item: ", pop(stack))
print("stack after popping an element: ", str(stack))
