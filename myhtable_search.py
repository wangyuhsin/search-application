# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    table = htable(4011)
    for i in range(len(files)):
        data = words(get_text(files[i]))
        for j in range(len(data)):
            if htable_get(table, data[j]) == None:
                htable_put(table, data[j], {i})
            else:
                htable_get(table, data[j]).add(i)
                htable_put(table, data[j], htable_get(table, data[j]))
    return table


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    return_lst = []
    s = htable_get(index, terms[0])
    if s == None:
        return return_lst
    for i in range(len(terms)):
        s = s.intersection(htable_get(index, terms[i]))
    for i in range(len(list(s))):
        return_lst.append(files[list(s)[i]])
    return return_lst
