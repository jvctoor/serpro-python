def findCenter(edges):
    map = {}
    for edge in edges:
        for node in edge:
            if node not in map:
                map[node] = node
            else:
                return node


