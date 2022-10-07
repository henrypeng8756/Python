# %%
sum = 0
a = eval(input('Please enter a number: '))
for i in range(0,a+1,7):
    sum += i
print('The sum of multiples of 7 from 1 to',a,'is',sum )

# %%
i = eval(input('Please give a number: '))
sumList = list((i for i in range(0,i+1,7)))
print('The sum of multiples of 7 from 1 to %d is %d' %(i,sum(sumList)))
