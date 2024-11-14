def main():
    from util import TextProcessor
    qp  = TextProcessor()
    s   = "This is some sample string"
    bow = qp.process(s)                             # NOTE: You can use the given method to process a sentence into a tokenized bag-of-words

    #from avltree import AVLTree 
    from avltree_x1 import AVLTreeX1 as AVLTree   # NOTE: Uncomment to use AVLTreeX1
    avltree = AVLTree()

    from bktree import BKTree
    #from levenshtein import lev
    from levenshtein import lev_dp as lev         # NOTE: Uncomment to use dynamic programming version of Levenshtein distance
    bktree = BKTree(lev)

    from util import Dataset
    dataset = Dataset("brooklyn_public_library_catalog_selected.csv", -1)



    print("Indexing: Load in the data")

    # Easy iteration over dataset.
    for book in dataset:        
        book_id = book['ID']
        book_title = book['TITLE']
        
        tokenized_title = qp.process(book_title)
        for i in tokenized_title:
            avltree.insert(i,book_id)                # TODO: 1. Construct a binary search tree to map title words to book ID
            bktree.insert(i)                         # TODO: 2. Construct a BK-tree to structure similar words.



    print("Ranking: Demonstrate search engine")
    
    from ranker import Ranker
    ranker = Ranker(avltree, bktree)

    while True:
        result = []
        query = input("Query: ")
        string_matching_threshold = int(input("String matching threshold: "))
     
        tokenized_query = qp.process(query)
        ranking = ranker.get_ranking(tokenized_query, string_matching_threshold=string_matching_threshold)
        
        for i in ranking:
            
            result.append(dataset.get_book(i))                               # TODO: 3. Retrieve the book information for the best ranking books.
             
        for i in result:
            print(i)


    


if __name__ == "__main__":
    main()
