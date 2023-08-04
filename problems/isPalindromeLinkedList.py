def isPalindrome(head):
    linkedList = []
    current = head
    while (current):
        linkedList.append(current.val)
        current = current.next
    print(linkedList)

    def reverseList(arr):
        final = []
        for i in range(len(arr) - 1, -1, -1):
            final.append(arr[i])
        return final

    linkedListInverse = reverseList(linkedList)
    if linkedList == linkedListInverse:
        return True
    else:
        return False
