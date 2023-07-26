

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
        # print(self.head)

    def insertAtEnd(self, data):
        node = Node(data)
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def display(self):
        if self.head is None:
            print("Empty")

        itr = self.head
        # print(itr.data)
        llstr = ''

        while itr:
            if itr.next == None:
                llstr += str(itr.data)
                break
            llstr += str(itr.data) + ' -> '
            itr = itr.next

        print(llstr)




if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtBeginning(10)
    ll.insertAtBeginning(9)
    ll.insertAtEnd(2)
    ll.display()

