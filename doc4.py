# # list=[6,1,3,5,3,1,6]

list=[6,1,3,5,3,1,6]
b=[]
i=0
while i<len(list):
    if list[i] not in b:
        b.append(list[i])
    i+=1
j=0
product=1
while j<len(b):
    product=product*b[j]
    j+=1
print(product)



    


