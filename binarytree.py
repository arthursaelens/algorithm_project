"""
Group: 5

Template for Binary Search Tree implementation. 
"""

class BinaryTreeNode():

    key: str
    values: list
    left: "BinaryTreeNode"
    right: "BinaryTreeNode"

    def __init__(self, key: str, id: int) -> None:
        self.key = key
        self.values = [id]
        self.left = None
        self.right = None


class BinaryTree():
    
    _root: BinaryTreeNode
    NodeType: type = BinaryTreeNode

    def __init__(self) -> None:
        self._root = None

    def get(self, key: str) -> list:
        """
        Method to retrieve the values (book IDs) for a key (word) from the search tree.
        Calls recursive method `_get`.

        :param str key: Key to retrieve values of.
        :return list: Values linked to key.
        """
        return self._get(self._root, key)

    def _get(self, node: BinaryTreeNode, key: str) -> list:
        """
        Recursive get method.

        :param BinaryTreeNode node: Current node to evaluate.
        :param str key: Key to retrieve values of.
        :return list: Values linked to key.
        """
        
        if node is None:
            return []
        elif key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        return node.values
    def insert(self, key: str, id: int) -> None:
        """
        Method to insert an id (book ID) matching a key (word from title) into the search tree.
        Calls recursive method `_insert`
        
        :param str key: Key in tree, word from title.
        :param int value: Value in tree, book ID.
        """
        self._root = self._insert(self._root, key, id)

    def _insert(self, node: BinaryTreeNode, key: str, id: int) -> BinaryTreeNode:
        """
        Recursive insertion method.
        :param BinaryTreeNode node: Current node to evaluate.
        :param str key: Key in tree.
        :param int value: Value to add.
        :return BinaryTreeNode: Current node.
        """
        if node is None:
            return self.NodeType(key, id)
        elif key < node.key:
            node.left = self._insert(node.left, key, id)
        elif key > node.key:
            node.right = self._insert(node.right, key, id)
        else:
            node.values.append(id)
        return node