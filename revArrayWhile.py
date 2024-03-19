a=[1,2,3,4,5]
k=len(a)
l=0
r=len(a)-1
while(l<r):
  temp=a[l]
  a[l]=a[r]
  a[r]=temp
  l+=1
  r-=1
print(a)
  
    
  