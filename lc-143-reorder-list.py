from LinkedList import LinkedList

ll = LinkedList()

# input as space-separated integers
data = list(map(int, input("Enter values as space separated integers: ").split()))

for val in data:
    ll.append(val)

print("Linked List:")
ll.display()

def reorderList (head):
    
    # find middle of the list

    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second list

    second = slow.next
    prev = slow.next = None

    while second:
        tmp1 = second.next
        second.next = prev
        prev = second
        second = tmp1

    # prev has the head of second list

    # stitch 2 lists together

    first, second = head, prev

    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2

reorderList(ll.head)
ll.display ()
