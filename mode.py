# increase to decrrese  
a=[1,2,3,4,5,6,7,8,4,6,8,33,33,33]
length=len(a) 
set_nums=set(a)
mode_list=sorted(set_nums, key=a.count, reverse=True)
print(mode_list)

    