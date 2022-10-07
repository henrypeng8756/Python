# %%
answer = eval(input())

if answer % 2 == 0 and answer % 7 == 0:
    print(answer, 'is multiple of 2 and 7!')
elif answer % 2 == 0:
    print(answer, 'is a multiple of 2!')
elif answer % 7 == 0:
    print(answer, 'is a multiple of 7!') 
else:
    print(answer, 'is not multiple of 2 and 7!')
# %%
answer = eval(input())

if answer % 2 != 0 and answer % 7 != 0:
    print(answer, 'is not multiple of 2 and 7!')
else:
    if answer % 2 == 0 and answer % 7 == 0:
        print(answer, 'is a multiple of 2 and 7')
    elif answer % 2 == 0:
        print(answer, 'is a multiple of 2')
    else:
        print(answer, 'is a multiple of 7')
# %%
