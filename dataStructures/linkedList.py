

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node
        print(self.head)

    def print(self):
        if self.head is None:
            print("Empty")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '> '
            itr = itr.next

        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    print(ll.head)
    ll.insertAtBeginning(3)
    ll.insertAtBeginning(12)
    ll.print()

