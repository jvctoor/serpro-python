def validPath(self, n, edges, source, destination):
    if n < 2:
        return True

    adjMatrix = {}
    for [edge1, edge2] in edges:
        if edge1 not in adjMatrix:
            adjMatrix[edge1] = [edge2]
        else:
            neibours = adjMatrix[edge1]
            neibours.append(edge2)
            adjMatrix[edge1] = neibours
        if edge2 not in adjMatrix:
            adjMatrix[edge2] = [edge1]
        else:
            neibours = adjMatrix[edge2]
            neibours.append(edge1)
            adjMatrix[edge2] = neibours

    print(adjMatrix)

    queue = []
    visited = []
    queue.append(source)
    while len(queue) > 0:
        currentNode = queue.pop(0)
        if currentNode in visited:
            continue
        neibours = adjMatrix[currentNode]
        for node in neibours:
            queue.append(node)
        visited.append(currentNode)
        if destination in queue:
            return True

    return False