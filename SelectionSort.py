def selection_sort(L):
    n =len(L)
    for i in range(n-1):
        mini = L[i]
        pos = i
        for j in range(i+1, n):
            if L[j] < mini:
                mini = L[j]
                pos = j
        
        L[pos],L[i] = L[i],L[pos]

if __name__=='__main__':
    L = [45,2,55,6]
    selection_sort(L)
    print(L)





'''
1) For each position i from 0 to n−2:
2) Assume the element at i is the smallest.
3) Scan the rest of the array (i+1 to n−1) to find the actual smallest element.
4) Keep track of the index of the minimum element.
5) After the inner scan ends, swap the smallest element with the element at position i.
6) Continue with the next position.
'''