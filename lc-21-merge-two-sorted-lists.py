from LinkedList import LinkedList 
from LinkedList import Node
import pdb

print ("Create List1")

list1 = LinkedList()

data = list(map(int, input("Enter values as space separated integers: ").split()))

for val in data:
    list1.append(val)

list1.display ()

print ("Create List2")

list2 = LinkedList()

data = list(map(int, input("Enter values as space separated integers: ").split()))

for val in data:
    list2.append(val)

list2.display ()

def mergeTwoLists (list1, list2):
    dummy = node = Node () 
   
    head1 = list1.head
    head2 = list2.head

    while head1 and head2:
        if head1.val < head2.val:
            node.next = head1
            head1 = head1.next
        else:
            node.next = head2
            head2 = head2.next
        node = node.next

    return dummy.next

sorted_list_head = mergeTwoLists (list1, list2)

ll = LinkedList()
ll.head = sorted_list_head

ll.display ()
