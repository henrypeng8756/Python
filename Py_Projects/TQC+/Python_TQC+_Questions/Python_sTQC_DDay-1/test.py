# %%
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print(f'( {x1} , {y1} )')
print(f'( {x2} , {y2} )')
print('Distance = %.4f'%(((x1-x2)**2+(y1-y2)**2)**0.5))

# %%
a = eval(input())
b = eval(input())
opt = input()
if opt == '+':
    print(f'{a+b}')
elif opt == '-':
    print(f'{a-b}')
elif opt == '*':
    print(f'{a*b}')
elif opt == '/':
    print(f'{a/b}')
elif opt == '//':
    print(f'{a//b}')
else:
    print(f'{a%b}')

# %%
numSum = 0
a = eval(input())
for sumTime in range(1,a+1):
    if sumTime % 5 == 0:
        numSum += sumTime
print(numSum)

# %%
evenNum = 0 
for times in range(1,11):
    num = eval(input())
    if num % 2 == 0:
        evenNum += 1
print(f'Even numbers: {evenNum}')
print(f'Odd numbers: {10-evenNum}')

# %%
# (-b+((b**2)-(4*a*c))**0.5)/(2*a)  
def compute():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    proof = b**2-4*a*c
    if proof < 0:
        print('Your equation has no root.')
    elif proof == 0:
        print('%s'%(-b/(2*a)))
    else:
        print('%s, %s'%(((-b+proof**0.5)/(2*a)),((-b-proof**0.5)/(2*a))))
compute()
# %%
cardSum = 0
for card in range(5):
    num = input()
    if num == 'A':
        cardSum += 1
    elif num =='J':
        cardSum += 11
    elif num == 'Q':
        cardSum += 12
    elif num == 'K':
        cardSum += 13
    else:
        cardSum += int(num)
print(cardSum)

# %%
numList = set()
while True:
    n = eval(input())
    if n != -9999:
        numList.add(n)
    else:
        print(f'Length: {len(numList)}')
        print(f'Max: {max(numList)}')
        print(f'Min: {min(numList)}')
        print(f'Sum: {sum(numList)}')
        break

# %%
sentence = input()
print(sentence.upper())
print(sentence.title())

# %%
fn = 'read.txt'
with open(fn,'r') as file:
    contents = file.read()
numList = list(map(int,contents.split(' ')))
print(sum(numList))

#print(sum(numList))
# %%
