# %%
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print('(',x1,',',y1,')')
print('(',x2,',',y2,')')
print('Distance = %.4f' %(((x1-x2)**2+(y1-y2)**2))**0.5)


# %%
num = eval(input())
if num >= 10 and num <= 15:
    print((str.upper(hex(num))).lstrip('0X'))
else:
    print(num)

# %%
numSum = 0
n = eval(input())
for numValue in range(2,n+1): #8
    numSum += 1/((numValue-1)**0.5+(numValue)**0.5)
print('%.4f' %numSum)

# %%
evenCount=0
for numCount in range(10):
    i = eval(input())
    if i % 2 == 0:
        evenCount += 1
print('Even numbers: %d' %(evenCount))
print('Odd numbers: %d' %(10-evenCount))

# %%
def compute():
    a = eval(input())
    b = eval(input())
    print('%d' %(a**b))
compute()

# %%
k = eval(input())
for times in range(k):
    data = input().split(' ')
    new_data = list(map(eval,data))
    print('%.2f' % (max(new_data)-min(new_data)))

# %%
