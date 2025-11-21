
def insertion_sort(L):
    n = len(L)
    for j in range(1,n):
        key = L[j]
        i = j-1
        while i>=0 and L[i] > key:
            L[i+1] =L[i]
            i = i - 1
        L[i+1] = key

if __name__=='__main__':
    L = [45,2,55,6]
    insertion_sort(L)
    print(L)



'''
1) Start from index 1 (second element).
2) Treat index 0 as the sorted portion.
3) Store the current element in a temporary variable (key).
4) Compare it with elements in the sorted portion (left side).
5) Shift each element that is larger than key one position to the right.
6) When a smaller element is found or we reach start, insert key there.
7) Continue for all elements until the array is sorted.
'''