def LinearSearch(List, data):
    found = []
    for i in range(len(List)):
        if data == List[i]:
            found.append(i+1)
    return found

if __name__=="__main__":
    l = [1,2,3,4,5,1,7,1]
    l2 = [1,2,3,4,5,6,7,8]
    print(f"1 is found at ",end = " ")
    for i in LinearSearch(l,1):
        print(i,end = ", ")
    print("position in list.")

    print(f"1 is found at ",end = " ")
    for i in LinearSearch(l2,1):
        print(i,end = ", ")
    print("position in list.")
    