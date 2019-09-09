import sys
sys.path.append("..")

from data_structures.bst import Node

def check_balanced(root):
    if root is None:
        return -1

    left_height = check_balanced(root.left)
    if left_height == -1000:
        return -1000

    right_height = check_balanced(root.right)
    if right_height == -1000:
        return -1000

    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return -1000
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    return  check_balanced(root) != -1000



def check_balanced_bob(root):
    if root is None:
        return -1

    height_diff = check_balanced(root.left) - check_balanced(root.right)

    return height_diff


def is_balanced_bob(root):
    return abs(check_balanced_bob(root)) <  1 
