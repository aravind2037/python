class Node:
    def __init__(self):
        self.firstname=None
        self.secondname=None
        self.phone=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None
    #create your node dynamically
    def appendNode(self):
        newnode=Node()
        newnode.firstname=input("Enter first name: ")
        newnode.secondname=input("Enter second name: ")
        newnode.phone=int(input("Enter phone num: "))
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next
    
    
    def sortlistbyname(self):
        if self.head is None or self.head.next is None:
            # The list is already sorted or empty
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next

            if sorted_head is None or sorted_head.firstname >= current.firstname:
                # Insert at the beginning
                current.next = sorted_head
                sorted_head = current
            else:
                # Search for the correct position to insert
                temp = sorted_head
                while temp.next is not None and temp.next.firstname < current.firstname:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head
        self.displayLst()
    
    
    def sortlistbynum(self):
        if self.head is None or self.head.next is None:
            # The list is already sorted or empty
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next

            if sorted_head is None or sorted_head.phone >= current.phone:
                # Insert at the beginning
                current.next = sorted_head
                sorted_head = current
            else:
                # Search for the correct position to insert
                temp = sorted_head
                while temp.next is not None and temp.next.phone< current.phone:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head
        self.displayLst()

    #display nodes
    def displayLst(self):
        c=0
        if self.head==None:
            print("list is empty")
        else:
            self.temp=self.head
            while self.temp is not None:
                c+=1
                print("S.No:",c,self.temp.firstname,self.temp.phone)
                self.temp=self.temp.next 

LLObj=LinkedList()
LLObj.appendNode()
LLObj.appendNode()
LLObj.appendNode()
LLObj.appendNode()
print("Original List:")
LLObj.sortlistbyname()
LLObj.sortlistbynum()

# LLObj.Delteval(30)
# LLObj.displayLst()




