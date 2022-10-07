# %% 
def compute():
    department = input()
    studentID = input()
    sName = input()
    print('Department: %s'%(department))
    print('Student ID: %s'%(studentID))
    print('Name: %s'%(sName))
compute()

# %%
x = eval(input())
y = eval(input())
def compute(a,b):
    print('%d'%(a*b))
compute(x,y)


# %%
a = eval(input())
b = eval(input())
def compute(i,j):
    numSum = 0
    for counts in range(i,j+1):
        numSum += counts
    print(numSum)
compute(a,b)

# %%
def compute():
    a = eval(input())
    b = eval(input())
    print('%d'%(a**b))
compute()

# %%
def compute():
    char = input()
    x = eval(input())
    y = eval(input())
    charList = ''
    for char_row in range(x):
        charList += '%s '%(char) 
    for rows in range(y):
        print(charList)
compute()    

# %%
# -b+(((b**2)-(4*a*c))**0.5)/(2*a)
# -b-(((b**2)-(4*a*c))**0.5)/(2*a)
def compute():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    proof = (b**2)-(4*a*c)
    if proof < 0: 
        print('Your equation has no root.')
    elif proof == 0:
        print(f'{-b/(2*a)}')
    else:
        print(f'{(-b+proof**0.5)/(2*a)}, {(-b-proof**0.5)/(2*a)}')
compute()

# %%
def compute():
    x = eval(input())
    for num in range():
        if x % x == 0:
            print('Prime')
        else:
            print('Not Prime')
compute()

# %%
