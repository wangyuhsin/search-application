"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""


def htable(nbuckets):
    """Return a list of nbuckets lists"""
    buckets = [[] for i in range(nbuckets)]
    return buckets


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if type(o) == int:
        return o
    elif type(o) == str:
        h = 0
        for c in o:
            h = h * 31 + ord(c)
        return h
    else:
        return None


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    for i in range(len(table[hashcode(key) % len(table)])):
        if key == table[hashcode(key) % len(table)][i][0]:
            return i
    # return None


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    n = 0
    for i in range(len(table[hashcode(key) % len(table)])):
        if key == table[hashcode(key) % len(table)][i][0]:
            # table[hashcode(key) % len(table)][i][1].add(value)
            # table[hashcode(key) % len(table)][i] = (key, table[hashcode(key) % len(table)][i][1])
            table[hashcode(key) % len(table)][i] = (key, value)
            break
        n += 1
    if n == len(table[hashcode(key) % len(table)]):
        table[hashcode(key) % len(table)].append((key, value))


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    if type(bucket_indexof(table, key)) == int:
        return table[hashcode(key) % len(table)][bucket_indexof(table, key)][1]
    else:
        return None
    # if table[hashcode(key) % len(table)][bucket_indexof(table, key)] != None:
    #     return table[hashcode(key) % len(table)][bucket_indexof(table, key)][1]
    # else:
    #     return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    return_str = ""
    for i in range(len(table)):
        return_str += "000" + str(i) + "->"
        if len(table[i]) == 0:
            return_str += "\n"
        for j in range(len(table[i])):
            if j != (len(table[i]) - 1):
                return_str += str(table[i][j][0]) + \
                    ":" + str(table[i][j][1]) + ", "
            else:
                return_str += str(table[i][j][0]) + \
                    ":" + str(table[i][j][1]) + "\n"
    return return_str


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    return_str = ""
    return_str += "{"
    for i in range(len(table)):
        for j in range(len(table[i])):
            return_str += str(table[i][j][0]) + ":" + \
                str(table[i][j][1]) + ", "
    if return_str != "{":
        return_str = return_str[:-2]
    return_str += "}"
    return return_str
