class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

head = linkedList()
head.head = Node("1")
n2 = Node("2")
n3 = Node("3")

head.head.next = n2
n2.next = n3

n = 1
nth1 = head
nth2 = head

for i in range(n):
    nth1 = nth1.next

if not nth1:
    print(nth1.next)

while nth1.next:
    nth2 = nth2.next
    nth1 = nth1.next

nth2.next = nth2.next.next
print(head)