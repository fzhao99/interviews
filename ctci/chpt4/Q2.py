import sys
sys.path.append("..")

from data_structures.bst import Node as Tree

def min_tree(array):
    if len(array) == 0:
        return None


    middle = array[len(array)//2]

    tree = Tree(middle)

    left_array = array[0: len(array)//2 ]
    right_array = array[len(array)//2 + 1: len(array)]
    tree.left = min_tree(left_array)
    tree.right = min_tree(right_array)
    return tree


test_array = [1, 2, 3, 4]
print(min_tree(test_array))
