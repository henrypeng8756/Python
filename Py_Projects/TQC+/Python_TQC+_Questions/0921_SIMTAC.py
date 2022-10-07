# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|%5d %5d|'% (a,b))
print('|%5d %5d|'% (c,d))
print('|%-5d %-5d|'% (a,b))
print('|%-5d %-5d|'% (c,d))


# %%
a = eval(input())
b = eval(input())
opt = input()
if opt == '+':
    print('%d'%(a+b))
elif opt == '-':
    print('%d'%(a-b))
elif opt == '*':
    print('%d'%(a*b))
elif opt == '/':
    print('%d'%(a/b))
elif opt == '//':
    print('%d'%(a//b))
else:
    print('%d'%(a%b))

# %%
numbSum = 0
a = eval(input())
for divsum in range(1,a+1):
    if divsum % 5 == 0:
        numbSum += divsum
print(numbSum)

# %%
numbSum = [] 
while True:
    n = eval(input())
    if n != 9999:
        numbSum.append(n)
        continue
    else:
        print(min(numbSum))
        break

# %%
# (-b+((b**2)-(4*a*c))**2)/2a
def compute():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    proof = b**2-4*a*c
    if proof < 0:
        print('Your equation has no root.')
    elif proof == 0:
        print('%.1f'%(-b/(2*a)))
    else:
        print('%.1f, %.1f' % (((-b+((b**2)-(4*a*c))**0.5)/(2*a)),((-b-((b**2)-(4*a*c))**0.5)/(2*a))))
compute()

# %%
a = input()
print(a.upper())
print(a.title())


# %%
