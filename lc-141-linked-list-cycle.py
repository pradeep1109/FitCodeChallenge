from LinkedList import LinkedList

ll = LinkedList()

# input as space-separated integers
data = list(map(int, input("Enter values as space separated integers: ").split()))

for val in data:
    ll.append(val)

print("Linked List:")
ll.display()

if input ('do you want to create cyclical linkedlist: ') == 'yes':
    ll.tail.next = ll.head.next.next

def hasCycle (head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False

print (hasCycle(ll.head))
