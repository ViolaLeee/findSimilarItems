# calculate jaccard similartiy
def jaccard(list1, list2):
    intersets = calIntersets(list1, list2)
    unionsets = calUnionsets(list1, list2)
    jSimilarity = float(len(intersets))/len(unionsets)
    return jSimilarity

# calculate intersection
def calIntersets(lista, listb):
    intersection = []
    for items in lista:
        if (items in listb):
            intersection.append(items)
    return intersection

# calculate union sets
def calUnionsets(lista, listb):
    unionsection = []
    for items in lista:
        unionsection.append(items)
    for item in listb:
        if (item not in lista):
            unionsection.append(item)
    return unionsection

if __name__=="__main__":
    A = ['a', 'd']
    B = ['c']
    C = ['b', 'd', 'e']
    D = ['a', 'c', 'd']
    # print(calIntersets(A, B))
    # print(calUnionsets(A, B))
    print(jaccard(A, B))
    print(jaccard(A, C))
    print(jaccard(A, D))
    print(jaccard(B, C))
    print(jaccard(B, D))
    print(jaccard(C, D))