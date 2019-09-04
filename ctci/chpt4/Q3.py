import sys
sys.path.append("..")

from data_structures.LinkedList import LinkedList


#breath first
def list_depths_breadth(root):
    current = LinkedList()
    result = {}

    if root is not None:
        current.add(root)

    counter = 0

    while not current.is_empty():
        result[str(counter)] = current
        parents = current
        current = LinkedList()

        for node in parents:
            if node.left:
                current.add(node.left)
            if node.right:
                current.add(node.right)

        counter += 1
    return result

def list_depths_depth(root):
    lists = {}
    list_depths_depth_help(root, 0, lists)
    return lists

def list_depths_depth_help(root, level, result):
    if root is None:
        return
    current = LinkedList()
    if result[level] is None:
        result[level] = current

    result[level].add(root)
    list_depths_depth(root.left, level + 1, result)
    list_depths_depth(root.right, level + 1, result)
