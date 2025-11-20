def bubble_sort(L):
    for j in range(len(L)-1, 0, -1):        
        for i in range(0, j):              
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

if __name__=='__main__':
    L = [45,2,55,6]
    bubble_sort(L)
    print(L)
