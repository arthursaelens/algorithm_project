"""
Group: 5

Template for BK-Tree implementation. 
NOTE: The function for the distance can be given upon initialization of the BK-Tree. 
      For the project, this will be `lev(a, b)` or `lev_dp(a, b)`.
"""


class BKTreeNode():

    value: str
    _children: dict

    def __init__(self, value: str) -> None:
        self.value = value
        self._children = {}

    def get_distances_of_children(self) -> list:
        """
        Return the distances for which this node has children.

        :return list: Sorted list of distances.
        """
        return sorted(list(self._children.keys()))

    def get_child(self, distance: int) -> "BKTreeNode":
        """
        Return the child for a certain distance

        :param int distance: Distance to the child to retrieve.
        :return BKTreeNode: The child.
        """
        return self._children.get(distance, None)

    def set_child(self, distance: int, child: "BKTreeNode") -> None:
        """
        Add a child to the node.

        :param int distance: The distance to the child.
        :param BKTreeNode child: The child.
        """
        self._children[distance] = child


class BKTree():

    _root: BKTreeNode
    _distance_function = None

    def __init__(self, distance_function: callable) -> None:
        """
        :param callable distance_function: The function to calculate the distance between two strings. 
        """
        self._root = None
        self._distance_function = distance_function

    def get(self, query_word:str, thresh: int = 1) -> list:
        """
        Method to retrieve matches for a query word.
        Call recursive method `_get`.
        
        :param str query_word: The query word.
        :param int thresh: The threshold to respect, defaults to 1
        :return list: List of tuples (v, d) for values matching the query, 
                      where v is the value matching the query q, and d is the distance from k to q.
        """
        retval = self._get(self._root, query_word, thresh)
        return sorted(sorted(retval), key=lambda t: t[1])

    def _get(self, node: BKTreeNode, query: str, thresh: int) -> list:
        """
        Recursive get method.

        :param BKTreeNode node: The current node to evaluate.
        :param str query: The query word.
        :param int thresh: The threshold to respect.
        :return list: List of tuples (v, d) for values matching the query, 
                      where v is the value matching the query q, and d is the distance from k to q.
        """
        if node is None:
            return []

        distance = self._distance_function(node.value, query)
        result = []
        if distance <= thresh:
            result.append((node.value, distance))

        for i in node.get_distances_of_children():
            if abs(i - distance) <= thresh:
                result.extend(self._get(node.get_child(i), query, thresh))

        return result

    def insert(self, value: str) -> None:
        """
        Method to insert a new value into the tree.

        :param str value: Value to insert.
        """
        if self._root is None: self._root = BKTreeNode(value)
        else: self._root = self._insert(self._root, value)

    def _insert(self, node: BKTreeNode, value: str) -> BKTreeNode:
        """
        Recursive insertion method.

        :param BKTreeNode node: Current node to evaluate.
        :param str value: Value to insert.
        :return BKTreeNode: Current node.
        """
        distance = self._distance_function(node.value, value)
        child = node.get_child(distance)
        if distance == 0:
            return node
        elif child is None:
            node.set_child(distance, BKTreeNode(value))
        else:
            self._insert(child, value)

        return node
        
