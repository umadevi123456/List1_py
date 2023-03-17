#leanth of list odd
# a=[6,7,4,3,5,2,9,7,3]
# a.sort()
# if (len(a)%2 !=0):
#     mid =len(a)//2
#     print("medium =",a[mid])
    
# O/P: medium = 5

    
    
#leanth of list even
# a=[1,2,3,4,5,6,7,8]
# if (len(a)%2 !=0):
#     mid =len(a)//2
#     print("medium =",a[mid])   
# else:
#     mid1=len(a)//2
#     mid2=mid1-1
#     median=(a[mid1]+a[mid2])/2
#     print("median:",median)
    
# O/P: median: 4.5

a=[1,2,3,4,5,6,7,8]
length=len(a) 
sorted_list=sorted(a)
size=int(length/2)
if length%2==0:
    median=(sorted_list[size]+sorted_list[size-1])/2
    print("median:",median)
else:
    median=sorted_list[size]
    print("median:",median) 
    