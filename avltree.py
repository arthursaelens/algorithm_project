"""
Group: 5

Template for AVL Binary Search Tree implementation. 
NOTE: The class AVLTree inherrits from BinaryTree.
"""

from binarytree import BinaryTree, BinaryTreeNode

class AVLTree(BinaryTree):

    def __init__(self) -> None:
        super().__init__()

    def _insert(self, node: BinaryTreeNode, key: str, value: int) -> BinaryTreeNode:
        """
        Overridden recursive insertion method.
        Calls `_rebalance` on the way up.

        :param BinaryTreeNode node: Current node to evaluate.
        :param str key: Key in tree.
        :param int value: Value to add.
        :return BinaryTreeNode: Current node.
        """
        node = super()._insert(node, key, value)
        node = self._rebalance(node, key)
        return node

    def _calc_node_height(self, node: BinaryTreeNode) -> int:
        """
        Recursive calculation of the height of a node.

        :param BinaryTreeNode node: Node to calculate height of.
        :return int: The height of the node.
        """
        if node is None:
            return -1
        left_height = self._calc_node_height(node.left)
        right_height = self._calc_node_height(node.right)
        return max(left_height, right_height) + 1

    def _find_balance(self, node: BinaryTreeNode) -> int:
        """
        Calculates the balance of a node.

        :param BinaryTreeNode node: Node to calculate the balance of.
        :return int: The balance of the node.
        """
        if node is None:
            return 0
        return self._calc_node_height(node.right) - self._calc_node_height(node.left)

    def _rebalance(self, node: BinaryTreeNode, key: str) -> BinaryTreeNode:
        """
        Rebalance the subtree when necessary.

        :param BinaryTreeNode node: The current node, the root of the subtree.
        :param str key: The key of the last-inserted node.
        :return BinaryTreeNode: The (new) root of the subtree.
        """
        balance = self._find_balance(node)

        # Left Heavy
        if balance > 1 and key > node.right.key:
            return self._right_rotate(node)
        
        # Right Heavy
        if balance < -1 and key < node.left.key:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and key < node.right.key:
            node.right = self._left_rotate(node.right)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and key > node.left.key:
            node.left = self._right_rotate(node.left)
            return self._left_rotate(node)

        return node
        

    def _right_rotate(self, old_root: BinaryTreeNode) -> BinaryTreeNode:
        """
        Perform a right rotate for the subtree.

        :param BinaryTreeNode old_root: The current root for the subtree.
        :return BinaryTreeNode: The root of the subtree after rotation.
        """
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left = old_root
        return new_root
       

    def _left_rotate(self, old_root: BinaryTreeNode) -> BinaryTreeNode:
        """
        Perform a left rotate for the subtree.

        :param BinaryTreeNode old_root: The current root for the subtree.
        :return BinaryTreeNode: The root of the subtree after rotation.
        """
        new_root = old_root.left
        old_root.left = new_root.right
        new_root.right = old_root
        return new_root
        
