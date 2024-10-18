from StacksAndQueue import ArrayStack as Stack

def reverse_file(myfile):
    stack = Stack()

    with open(myfile, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))


    with open(myfile, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')

myfile = 'myfile.txt'
reverse_file(myfile)