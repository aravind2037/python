class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    
    def push(self,val):
        if self.top==4:
            print("Stack Overflow!")
        else:
            self.stack.append(val)
            self.top+=1
            print(f"{val} inserted successfully!")
    def POP(self):
        if self.top==0:
            print("Stack is empty")
        else:
            r=self.stack[self.top]
            self.stack.pop()
            self.top-=1
            print(f"{r} is poped!")
            
    def displaystk(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
stackObj=Stack()
stackObj.push(10)
stackObj.push(20)
stackObj.push(30)
stackObj.push(40)
stackObj.displaystk()
stackObj.push(50)
stackObj.push(60)
stackObj.push(70)