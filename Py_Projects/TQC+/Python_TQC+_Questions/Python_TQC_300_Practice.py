# %%
import re


a = eval(input())
b = eval(input())
sumList = []
sortList = [a,b]
sortList.sort()
for i in range(sortList[0],sortList[1]+1):
    sumList.append(i)
print(sum(sumList))

a = eval(input())
b = eval(input())
sortList = [a,b]
sortList.sort()
numbSum = 0
for i in range(sortList[0],sortList[1]+1):
    numbSum += i
print(numbSum)

# %%
a = eval(input())
b = eval(input())
evenList = []
sortList = [a,b]
for i in range(sortList[0],sortList[1]+1):
    if i % 2 == 0: 
        evenList.append(i)
print(sum(evenList))
    
a = eval(input())
b = eval(input())
sortList = [a,b]
sortList.sort()
numbSum = 0
for i in range(sortList[0],sortList[1]+1):
    if i % 2 == 0:
        numbSum += i
print(numbSum)

# %%
i = eval(input())  
for line in range(1,i+1): 
    for numb in range(1,line+1): 
        print('%4d' %(line*numb), end ='')
    print()

# %%
a = eval(input())
numbSum = 0
for numb in range(1,a+1):
    if numb % 5 == 0:
       numbSum += numb
print(numbSum)

# %%
numb = input()
print(numb[::-1])
# %%
numMulti = 1
n = eval(input())
for times in range(1,n+1):
    numMulti *= times
print(numMulti)

# %%
n = eval(input())
for rows in range(1,n+1):
    for columns in range(1,n+1):
        column_str = '%d * %d = %-4d' %(columns,rows,rows*columns)
        print('%s'%(column_str),end='')
    print('')

# %%
num = []
n = eval(input())
for times in range(n):
    num.clear()
    num_str = input()
    for str_split in num_str:
        num.append(str_split)
        int_num = list(map(int,num))
    print(f'Sum of all digits of {num_str} is {sum(int_num)}')

# %%
amount = eval(input())
returnRate = eval(input())
months = eval(input())
returnNum = 0
print('%s \t  %s' % ('Month', 'Amount'))
for annaulP in range(1,months+1):
    amount += amount*returnRate/1200
    print('%3d \t %.2f' % (annaulP, amount))

# %%
numSum = 0
n = eval(input())
for times in range(2,n+1):
    numSum += 1/((times-1)**0.5+(times)**0.5)
print('%.4f'%(numSum))


# %%