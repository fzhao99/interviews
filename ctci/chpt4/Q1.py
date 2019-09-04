def search(root, destination):
    if root is None:
        return

    root.visited = True
    for node in root.adjacent:
        if node.visited = False:
            if node == destination:
                return True
            else:
                search(node, destination)

    return False 
