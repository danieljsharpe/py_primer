'''
A collection of sorting algorithms
'''
# Insertion sort (recursive implementation)
def ins_sort_rec(seq, i):
    if i == 0: return # base case
    ins_sort_rec(seq, i-1) # sort 0...i-1
    j = i # start 'walking' down
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

# Insertion sort (iterative implementation)
def ins_sort(seq):
    for i in range(1,len(seq)): # 0...i-1 sorted so far
        j = i # start 'walking' down
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1

# Selection sort (recursive implementation)
def sel_sort_rec(seq, i):
    if i == 0: return # base case
    max_j = i # index of largest value so far
    for j in range(i): # look for a larger value
        if seq[j] > seq[max_j]: max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1) # sort 0...i-1

# Selection sort (iterative implementation)
def sel_sort(seq):
    for i in range(len(seq)-1,0,-1): # n...i+1 sorted so far
        max_j = i # index of largest value so far
        for j in range(i): # look for a larger value
            if seq[j] > seq[max_j]: max_j = j
        seq[i], seq[max_j] = seq[max_j], seq[i]    

# Gnome sort
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]: i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

# merge sort
def mergesort(seq):
    mid = len(seq) // 2 # midpoint for division
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft) # sort by halves
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt: # neither half is empty
        if lft[-1] >= rgt[-1]: # lft has greatest last value
            res.append(lft.pop()) # append it
        else:
            res.append(rgt.pop()) # rgt has greatest last value so append it
    res.reverse() # since result is backward
    return (lft or rgt) + res # also add the remainder

# Quicksort
# Hoare partitioning scheme - more efficient for average case
def hoare_partition(seq, lo, hi):
    piv = seq[lo]
    i = lo - 1 # idx at lower end of array
    j = hi + 1 # idx at upper end of array
    # indices move towards one another until they correspond to a pair of elems both on the wrong side of the pivot
    while True:
        j -= 1
        while seq[j] <= piv:
            i += 1
            while seq[i] >= piv:
                if i < j:
                    seq[i], seq[j] = seq[j], seq[i]
                    break
                else:
                    return j
def quicksort_hoare(seq, lo=0, hi=None):
    if hi is None: hi = len(seq)-1
    if lo < hi:
        p = hoare_partition(seq, lo, hi)
        quicksort_hoare(seq, lo, p)
        quicksort_hoare(seq, p+1, hi)
    return seq
# Lomuto partitioning scheme - always choose last elem to be pivot
def lomuto_partition(seq, lo, hi):
    piv = seq[hi]
    i = lo - 1 # idx such that elems seq[lo] - seq[i] (inclusive) are < piv
               # and elems seq[i+1[ - seq[hi] inclusive are > piv
    for j in range(lo, hi):
        if seq[j] <= piv:
            i += 1
            seq[i], seq[j] = seq[j], seq[i]
    # elem seq[i+1] is the leftmost element that is greater than pivot, so swap
    seq[i+1], seq[hi] = seq[hi], seq[i+1]
    return i+1
def quicksort_lomuto(seq, lo=0, hi=None):
    if hi is None: hi = len(seq)-1
    if lo < hi:
        p = lomuto_partition(seq, lo, hi)
        quicksort_lomuto(seq, lo, p-1)
        quicksort_lomuto(seq, p+1, hi)
    return seq

#Quicksort - alternative implementation
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [ x for x in seq if x <= pi]
    hi = [ x for x in seq if x > pi]
    return lo, pi, hi
def quicksort2(seq):
    if len(seq) <= 1: return seq # base case
    lo, pi, hi = partition(seq)
    return quicksort2(lo) + [pi] + quicksort2(hi) # sort lo and hi separately
#Simple implementation of 'select' (find (k+1)th lowest elem) also making
#use of partition
def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k: return pi
    elif m < k:
        return select(hi, k-m-1)
    else:
        return select(lo,k)


# Driver code
#seq = [ 170, 45, 75, 90, 802, 24, 2, 66]
seq = [ 3, 7, 8, 5, 2, 1, 9, 5, 4]
seq = [ 2, 8, 7, 1, 3, 5, 6, 4]
print seq
#ins_sort_rec(seq, len(seq)-1)
#ins_sort(seq)
#sel_sort_rec(seq, len(seq)-1)
#sel_sort(seq)
#gnomesort(seq)
#seq = mergesort(seq)
#seq = quicksort_lomuto(seq)
seq = quicksort_hoare(seq)
#seq = quicksort2(seq)
#print select(seq,3)
print seq
