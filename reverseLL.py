class Node:
    def __init__(self): #structure of a Node
        self.data=None
        self.next=None


class LinkedList: 
    def __init__(self):
        self.head=None
        self.temp=None
    
    #create your node dynamically
    def appendNode(self):
        newnode=Node()
        newnode.data=int(input("Enter data: "))
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next

        
    #displayLinkedList
    def displayLst(self):
        c=0
        if self.head==None:
            print("list is empty")
        else:
            self.temp=self.head
            while self.temp is not None:
                c+=1
                print(self.temp.data,end="->")
                self.temp=self.temp.next 
            print("NULL")
    
    #DeleteNode
    def deleteNode(self,val):
        self.slow=None
        self.fast=self.head
        if self.head.data ==val:
            self.head=self.head.next
        else:

            while self.fast and self.fast.data != val:
                self.slow=self.fast
                self.fast=self.fast.next
            if self.fast ==None:
                print(f"{val} not found in the List!")
                return
            self.slow.next=self.fast.next
            
    #reverseTheList
    def reverseLst(self):
        self.prev = None
        self.current = self.head
        while self.current is not None:
            self.nextNode = self.current.next
            self.current.next = self.prev
            self.prev = self.current
            self.current = self.nextNode
        self.head = self.prev

        


LLObj=LinkedList()
LLObj.appendNode()
LLObj.appendNode()
LLObj.appendNode()
LLObj.appendNode()
print("Original List: ",)
LLObj.displayLst()
print()
LLObj.deleteNode(5)
LLObj.displayLst()
