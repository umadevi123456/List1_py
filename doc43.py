a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
x=20
n=4     
i=1
while i<=4:
    a.insert(n,x)
    i+=1
    n+=5
print(a)

#   O/P : [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

#    OR 
   
# a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# i=0
# n=4
# while i<=4:
#     a.insert(n,20)
#     i+=1
#     n+=5
# print(a)



