list=[1,2,2,5,8,4,4,8]
b=[]
i=0
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i+=1
print(b)







