class Stack:
    def __init__(self,n):
        self.stack = [None]*n
        self.top = -1
    
    def is_Empty(self):
        if self.top < 0:
            return True
        else:
            False

    def is_Full(self):
        if self.top == len(self.stack)-1:
            return True
        else:
            return False
    
    def mni_push(self, element):
        if not self.is_Full():
            self.top+=1
            self.stack[self.top] = element
        else:
            print("Ahh sorry but Stack is already full.")
            
    
    def mni_pop(self):
        if not self.is_Empty():
            self.top-=1
            return self.stack[(self.top + 1)]
        else:
            print("ummm sorry but Stack is empty.")
    
    def __str__(self):
        print("Stack: ")
        
        for i in self.stack[::-1]:
            print(f"| {i} |")
       
        return ""

if __name__ == "__main__":
    n = int(input("Please enter the size of the Stack: "))
    sk = Stack(n)
    loop = True
    while(loop):
        ch = input("""
Please enter:
    1. Push
    2. Pop
    3. Display Stack
    4. Exit
    : 
                    """)
        match ch:
            case "1":
                element = int(input("Please enter integer to add in stack: "))
                sk.mni_push(element)
            
            case "2":
                print(f"Poped element: {sk.mni_pop()}")
            
            case "3":
                print(sk)

            case "4":
                print("Thank you!")
                loop = False
            
            case _:
                print("Please enter valid choice")




