from LinkedStack import LinkedStack as Stack
from LinkedDeque import LinkedDeque as Deque

def print_deque(D):
    '''Print elements in the deque'''
    current = D._header._next
    while current != D._trailer:
        print(current._element, end=" ")
        current = current._next
    print()

D = Deque()
S = Stack()

# Adding elements to the deque D
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

print("Initial deque:")
print_deque(D)

S.push(D.delete_first())
print_deque(D)
S.push(D.delete_first())
print_deque(D)
S.push(D.delete_first())
print_deque(D)
four = D.delete_first()
print_deque(D)
five = D.delete_first()
print_deque(D)
D.insert_last(five)
print_deque(D)
D.insert_last(four)
print_deque(D)
D.insert_first(D.delete_last())
print_deque(D)
D.insert_first(D.delete_last())
print_deque(D)
D.insert_first(S.pop())
print_deque(D)
D.insert_first(S.pop())
print_deque(D)
D.insert_first(S.pop())
print_deque(D)