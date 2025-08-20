a="poiuytrewqasdfghjklxcvbnm"
char_set=set()
m=0
l=0
r=0
while r<len(a):
    while a[r] in char_set:
        char_set.remove(a[l])
        l+=1
    char_set.add(a[r])
    m=max(m,r-l)
    r+=1
print(m)
