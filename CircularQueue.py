
n=5
queue=[None]*n
front=-1
rear=-1

def enqeue(x):
    global front, rear
    if rear==-1 and front==-1:
        rear=0
        front=0
        queue[rear] = x
        print(x, "is inserted")
    elif (rear+1)%n == front:
        print("Queue is Full")
    else:
        rear=(rear+1)%n
        queue[rear]=x
        print(x,"is inserted")
def dequeue():
    global front, rear
    if front==-1 and rear==-1:
        print("queue is empty")
    elif front==rear:
        front=-1
        rear=-1
        print(queue[front],"is deleted")
    else:
        print(queue[front],"is deleted from the queue")
        front=(front+1)%n
def display():
    if  front==-1 and rear==-1:
        print("Queue is empty")
    else:
        i=front
        print("Queue is:")
        
        while i!=rear:
            print(queue[i])
            i=(i+1)%n
        print(queue[i])
enqeue(2)
enqeue(3)
enqeue(-1)
enqeue(-5)
enqeue(8)
enqeue(4)
dequeue()
enqeue(4)
display()
