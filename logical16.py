a=[[1,2,3],[3,4,5]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j+=1
    b.append(sum)
    i+=1
print(b)

# O/P:[6, 12]