def insertIntoBST(root, val):
    newNode = val
    if root == None:
        root = newNode
        return root
    posicaoEncontrada = False
    currentNode = root
    while not posicaoEncontrada:
        if val <= currentNode.val:
            if currentNode.left == None:
                currentNode.left = newNode
                return root
            currentNode = currentNode.left
        else:
            if currentNode.right == None:
                currentNode.right = newNode
                return root
            currentNode = currentNode.right