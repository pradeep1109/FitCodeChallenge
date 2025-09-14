from LinkedList import LinkedList
from LinkedList import Node

ll = LinkedList()

# input as space-separated integers
data = list(map(int, input("Enter values as space separated integers: ").split()))

for val in data:
    ll.append(val)

print("Linked List:")
ll.display()

def removeNthElemInLL(head, n):
    dummy = Node()
    dummy.next = head

    left, right = dummy, head

    while n:
        right = right.next
        n-=1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next

new_ll = LinkedList()
new_ll.head = removeNthElemInLL(ll.head,int(input("enter elem to remove from end: ")))

new_ll.display()

