stack = [None]*5
top = 0

def pushs(a):
    global top
    if top < 5:
        val = a
        
        stack[top] = val
        top += 1
    else:
        print("Stack overflow!")
pushs(1)
pushs(2)
pushs(3)
pushs(4)
pushs(5)
# print(stack)
print(stack[top-1::-1])