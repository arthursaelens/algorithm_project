"""
Group: 5

Template for ranker. 
"""

from binarytree import BinaryTree
from bktree import BKTree
from bktree import BKTreeNode
from levenshtein import lev_dp
from collections import Counter

class Ranker():

    avltree: BinaryTree
    bktree: BKTree

    def __init__(self, avltree: BinaryTree, bktree: BKTree) -> None:
        """
        :param BinaryTree binary_search_tree: Initialized binary search tree, mapping title words to book IDs.
        :param BKTree bk_tree: Initialized BK tree.
        """
        self.avltree = avltree
        self.bktree = bktree


    def get_ranking(self, tokenized_query: list, string_matching_threshold: int) -> dict:
        """
        Get a ranking of matching books IDs based on a query.

        :param list tokenized_query: Tokenized query.
        :param int string_matching_threshold: Threshold to respect when matching words.
        :return: Collected results.
        """

        avltree = self.avltree
        bktree  = self.bktree

        wordsUnderThreshold = []
        idUnderThreshold = []

        for i in tokenized_query:
            tuplelijst = bktree.get(i, string_matching_threshold)
            woordlijst = []
            for e in tuplelijst:
                
                woordlijst.append(e[0])
            wordsUnderThreshold.extend(woordlijst)

        for i in wordsUnderThreshold:
            idlijst = avltree.get(i)
            idUnderThreshold.extend(idlijst)
        
        
        counter = Counter(list(set(idUnderThreshold)))
        
        
        koelelijst = sorted(idUnderThreshold, key = lambda x : counter[x], reverse = True)
        
        return koelelijst[:min(5,len(koelelijst))]
    

    #mss vergeten token omzetten in string? zoals regel 28 in script: tokenized_title = qp.process(book_title) 
    #normaal is list vergelijkbaar met string
    

