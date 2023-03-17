#mean means average.aveage=sum of the num/leangth of the num
# a=list(map(int,input().split()))
# sum=sum(a)
# length=len(a)
# mean=(sum/length)
# print("mean:"+str(mean))

# O/P: 2 4 5 6 7 8 2 4 5 2 3 8
#      mean:4.666666666666667

a=list(map(int,input().split()))
sum=sum(a)
length=len(a)
mean=round((sum/length),2)
print("mean:"+str(mean))

# O/P: 