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
    myList.addNodeAtEnd()
    myList.addNodeAtEnd()
    myList.addNodeAtEnd()
    myList.addNodeAtEnd()
    myList.addNodeAtEnd()
    print(myList)
    myList.addNodeAfterData("ak")
    print(myList)

        

        