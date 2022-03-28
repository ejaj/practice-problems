#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : bst.py
@Time : 3/27/22 11:23 PM
@Desc: 
"""


class Node:
    """
    A class to represent a node.
    Args:
        key:
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    """
    Inorder traverse.
    Args:
        root:

    Returns:

    """
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)


def insert(node, key):
    """
    Insert a node.
    Args:
        node:
        key:

    Returns:

    """
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def min_value_node(node):
    """
    Find the inorder successor,  leftmost leaf.
    Args:
        node:

    Returns:

    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    """
    Deleting a node.
    Args:
        root:
        key:

    Returns:

    """
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)
        return root


def main():
    """
    main function to drive code.
    Returns:

    """
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 10)
    root = insert(root, 14)
    root = insert(root, 4)

    print("Inorder traversal: ", end=' ')
    inorder(root)

    print("\nDelete 10")
    root = delete_node(root, 10)
    print("Inorder traversal: ", end=' ')
    inorder(root)


if __name__ == '__main__':
    main()
