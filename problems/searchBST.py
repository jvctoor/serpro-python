def searchBST(root, val):
    currentNode = root
    while currentNode != None:
        if val == currentNode.val:
            return currentNode
        if (val >= currentNode.val):
            currentNode = currentNode.right
        else:
            currentNode = currentNode.left

    return currentNode


