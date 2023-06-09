from collections import defaultdict
from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    dic = defaultdict(lambda: set())
    for i in range(len(files)):
        data = words(get_text(files[i]))
        for j in range(len(data)):
            dic[data[j]].add(i)
    return dic


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    return_lst = []
    s = index[terms[0]]
    for i in range(len(terms)):
        s = s.intersection(index[terms[i]])
    for i in range(len(list(s))):
        return_lst.append(files[list(s)[i]])
    return return_lst
