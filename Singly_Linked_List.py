class Node:
    def __init__(self):
        self.data = None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def newNode(self):
        temp = Node()
        data = input("please enter data you want to add in list: ")
        temp.data = data
        return temp
        
    
    def addNodeAtEnd(self):
        temp = self.newNode()
        if(self.head == None):
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    
    def search(self,element):
        current = self.head
        cnt = 1
        while current:
            if current.data == element:
                print(f"{element} found at {cnt} th position")
                return True
            current = current.next
            cnt+=1
        print(f"{element} is not in list.")
        return False
        
    def addNodeAfterData(self, element):
        if self.search(element):
            temp = self.newNode()
            current = self.head
            while current:
                if current.data == element:
                    temp.next = current.next
                    current.next = temp
                    break
                current = current.next
        else:
            print("Please try again and enter existing element in list")
    
    def __str__(self):
        current = self.head
        while current.next:
            print(f"[ '{current.data}' ] -->", end =" ")
            current = current.next
        print(f"[ '{current.data}' ]")
        return ""

if __name__ == '__main__':
    myList = SinglyLinkedList()
    loop = True
    while(loop):
        ch = input("""
Please enter:
    1. Add Node at end of list
    2. Add element after some element
    3. Display Singly Linked List
    4. Search element in linked list 
    5. Exit
    : 
                    """)
        match ch:
            case "1":
                myList.addNodeAtEnd()
            
            case "2":
                data = input("Please enter after which element you want to add new one?: ")
                myList.addNodeAfterData(data)
            
            case "3":
                print(myList)
            
            case "4":
                data = input("Please enter element you want to search: ")
                myList.search(data)
              

            case "5":
                print("Thank you!")
                loop = False
            
            case _:
                print("Please enter valid choice")


        

        