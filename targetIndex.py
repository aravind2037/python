l1=[1,4,0,0,3,10,5]
target=8
for i in range(0,len(l1)):
  sum=0
  l=[]
  for k in range(i,len(l1)):
    if sum==target:
      print(l)
      break
    else:
      sum=sum+l1[k]
      l.append(k)


    
    
