def bubble_sort(L):
    for j in range(len(L)-1, 0, -1):        
        for i in range(0, j):              
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

if __name__=='__main__':
    L = [45,2,55,6]
    bubble_sort(L)
    print(L)

'''
1) Repeat the process for (n−1) passes.
2) In each pass, compare element i with element i+1.
3) If arr[i] > arr[i+1], swap them.
4) After each pass, the largest element of the unsorted part moves to the correct position at the end.
5) Reduce the inner loop range after each pass because last elements are already sorted.
'''