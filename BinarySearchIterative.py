"""
1) This algorithm needed sorted list to search element from it
2) basic idea is to find middle value, check whether middle is same as required value or not. 
if not then change value for "low" and "high"
if middle is less than required then choose "low" and "high" as end values of current second half.
or 
if middle is greater than required then choose "low" and "high" as end values of current first half.
"""
"""
Binary Search Algorithm (Iterative):
1) Works only on SORTED arrays
2) Find middle element and compare with target:
   - If middle == target: found it, return index
   - If middle < target: search right half (target is bigger)
   - If middle > target: search left half (target is smaller)
3) Repeat until found or no elements left to search
"""

def binarySearchIter(List, data):
    low =0
    high = len(List)-1

    while low <= high:
        
        """mid = low + (high - low) // 2
        The Integer Overflow Problem
            ->
            In languages like C, C++, or Java, integers have a maximum value they can store:

            32-bit signed integer max: 2,147,483,647
            If you exceed this, the number "wraps around" to negative values (overflow)
        In Python, integers can be arbitrarily large - they automatically expand to hold any value
        
        Array:  [2,  3,  4,  10,  40]
            Index:   0   1   2   3    4
                    ↑        ↑        ↑
                    low      mid     high

            Distance from low to high = 4 - 0 = 4
            Half the distance = 4 // 2 = 2
            Middle = start from low and go 2 steps = 0 + 2 = 2"""
        
        mid = (low +high)//2

        if List[mid] == data:
            return mid
        
        elif List[mid] < data:
            low = mid +1
        
        elif List[mid] > data:
            high = mid -1
    
    return -1

if __name__=="__main__":
    l = [1,2,3,5,8,9,9]
    if binarySearchIter(l,9) == -1:
        print("9 is not in list")
    else:
        print(f"9 is found at {binarySearchIter(l,9)} position")