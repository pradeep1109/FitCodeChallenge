class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:          # first node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node   # move tail to new node

    def display(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")

# ---- main code ----
if __name__ == "__main__":
    ll = LinkedList()

    # input as space-separated integers
    data = list(map(int, input("Enter values as space separated integers: ").split()))

    for val in data:
        ll.append(val)

    print("Linked List:")
    ll.display()

