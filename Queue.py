class node:
    def __init__(self):
        self.data = None
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False
        

    def Enqueue(self, data):
        temp = node()
        temp.data = data
        if self.isEmpty():
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(f"{self.front.data} is removed from list")
            self.front = self.front.next
            if(self.front == None):
                self.rear = None
    
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty, hence nothing to show!")
        else:
            print(f"{self.front.data} is front element in queue.")
    
    def count(self):
        cnt = 0
        current = self.front
        while current:
            cnt+=1
            current = current.next
        return cnt
    
        
    def __str__(self):
        if self.isEmpty():
            print("Queue is Empty, hence nothing to show")

        else:
            current = self.front
            while current:
                print(f"[ {current.data} ] <- ",end="")
                current = current.next
        return ""


if __name__ == '__main__':
    q = Queue()
    loop = True

    while loop:
        ch = input("""
Please enter:
    1. Enqueue (Add element)
    2. Dequeue (Remove element)
    3. Peek (Show front element)
    4. Count total elements
    5. Display Queue
    6. Exit
    :
""")

        match ch:
            case "1":
                data = input("Enter the element you want to enqueue: ")
                q.Enqueue(data)

            case "2":
                q.dequeue()

            case "3":
                q.peek()

            case "4":
                print(f"Total elements in queue: {q.count()}")

            case "5":
                print(q)

            case "6":
                print("Thank you! Exiting the program.")
                loop = False

            case _:
                print("Please enter a valid choice.")
