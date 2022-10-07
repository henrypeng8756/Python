# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print(f'|{a:5d} {b:5d}|')
print(f'|{c:5d} {d:5d}|')
print('|%-5d %-5d|'%(a,b))
print('|%-5d %-5d|'%(c,d))


# %%
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print(f'( {x1} , {y1} )')
print(f'( {x2} , {y2} )')
print('Distance = %.4f' %(((x1-x2)**2+(y1-y2)**2)**0.5))

# %%
a = eval(input())
b = eval(input())
opt = eval(input())
if opt == '+':
    print('%d' %(a+b))
elif opt == '-':
    print('%d' %(a-b))
elif opt == '*':
    print('%d' %(a*b))
elif opt == '/':
    print('%d' %(a/b))
elif opt == '//':
    print('%d' %(a/b))
else:
    print('%d')
