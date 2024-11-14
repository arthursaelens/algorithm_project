"""
Group: 5

Template for AVL Binary Search Tree with persistent height information implementation. 
NOTE: The class AVLTreeX1 inherrits from AVLTree.
NOTE: A new node class is defined, which inherits from BinaryTreeNode. 
"""

from avltree import AVLTree, BinaryTreeNode

class AVLTreeNode(BinaryTreeNode):
    height: int

    def __init__(self, key: str, id: int) -> None:
        super().__init__(key, id)
        self.height = 1


class AVLTreeX1(AVLTree):

    def __init__(self) -> None:
        super().__init__()
        self.NodeType = AVLTreeNode

    def _calc_node_height(self, node: AVLTreeNode) -> int:
        """
        Calculates the height of a node. Overridden method.

        :param AVLTreeNodeX1 node: The node to calculate the height of.
        :return int: The height of the node.
        """
        if node is not None:
            return node.height
        return 0

    def _find_balance(self, node: AVLTreeNode) -> int:
        """
        Calculates the balance of a node. Overridden method.

        :param AVLTreeNodeX1 node: Node to calculate the balance of.
        :return int: The balance of the node.
        """
        if node is None:
            return 0
        left = node.left
        right = node.right
        lh = 0
        rh = 0
        if left is not None:
            lh = left.height
        if right is not None:
            rh = right.height
        return rh-lh
        

    def _insert(self, node: AVLTreeNode, key: str, value) -> AVLTreeNode:
        """
        Overridden recursive insertion method.

        :param AVLTreeNodeX1 node: Current node to evaluate.
        :param str key: Key in tree.
        :param int value: Value to add.
        :return AVLTreeNodeX1: Current node.
        """
        node = super()._insert(node, key, value)        
        node.height = 1 + max(self._calc_node_height(node.left), self._calc_node_height(node.right))
        return node

    def _right_rotate(self, old_root: AVLTreeNode) -> AVLTreeNode:    
        """
        Perform a right rotate for the subtree. Overridden method.

        :param AVLTreeNodeX1 old_root: The current root for the subtree.
        :return AVLTreeNodeX1: The root of the subtree after rotation.
        """  
        new_root = super()._right_rotate(old_root)
        old_root.height = 1 + max(self._calc_node_height(old_root.left), self._calc_node_height(old_root.right))
        new_root.height = 1 + max(self._calc_node_height(new_root.left), self._calc_node_height(new_root.right))
        return new_root


    def _left_rotate(self, old_root: AVLTreeNode) -> AVLTreeNode:
        """
        Perform a left rotate for the subtree. Overridden method.

        :param AVLTreeNodeX1 old_root: The current root for the subtree.
        :return AVLTreeNodeX1: The root of the subtree after rotation.
        """
        new_root = super()._left_rotate(old_root)
        old_root.height = 1 + max(self._calc_node_height(old_root.left), self._calc_node_height(old_root.right))
        new_root.height = 1 + max(self._calc_node_height(new_root.left), self._calc_node_height(new_root.right))
        return new_root
        