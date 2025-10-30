def binarySearchRec(L,data,low,high):
    if low>high:
        return -1
    
    mid = (low+high)//2
    if L[mid] == data:
        return mid
    elif L[mid] < data:
        return binarySearchRec(L,data,mid+1,high)
    elif L[mid] > data:
        return binarySearchRec(L,data,low,mid-1)

if __name__=="__main__":
    L = [1,2,3,9,78,88]
    if binarySearchRec(L,9,0,len(L)+1) == -1:
        print("9 is not in list")
    else:
        print(f"9 is found at {binarySearchRec(L,9,0,len(L)+1)} position")