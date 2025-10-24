class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            temp.prev = self.tail
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
    
    def deleteElement(self,element):
        if self.search(element):
            current = self.head
            prev = None
            while current:
                if current.data == element and prev:
                    prev.next = current.next
                    print(f"a node with '{element}' is deleted")
                elif current.data == element and not prev:
                    self.head = self.head.next
                    print(f"a head node with '{element}' is deleted")
                prev = current
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
    
    def displayFromEndToStart(self):
        current = self.tail
        while current.prev:
            print(f"[ '{current.data}' ] -->", end =" ")
            current = current.prev
        print(f"[ '{current.data}' ]")
        return ""

if __name__ == '__main__':
    myList = DoublyLinkedList()
    loop = True
    while(loop):
        ch = input("""
Please enter:
    1. Add Node at end of list
    2. Add element after some element
    3. Display Doubly Linked List (from Start to end)
    4. Display Doubly Linked List (from end to start)
    5. Search element in linked list 
    6. Delete element from list
    7. Exit
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
                myList.displayFromEndToStart()
            
            case "5":
                data = input("Please enter element you want to search: ")
                myList.search(data)
              
            case "6":
                data = input("Please enter element you want to delete: ")
                myList.deleteElement(data)
            case "7":
                print("Thank you!")
                loop = False
            
            case _:
                print("Please enter valid choice")


        

        