a = [1,2,3,4,5]
b = [1,2,3,8]
i=0
for i in range(len(b)):
    j = 0
    while j<len(a):
        if b[i] == a[j]:
            break
        j=j+1
        
if j == len(a):
    print("not subset")
else:
    print("subset")
        
        
            
        
