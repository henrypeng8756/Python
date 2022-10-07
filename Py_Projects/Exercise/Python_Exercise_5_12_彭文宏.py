# %%
list = []
itemNumber = eval(input('How much items do you want to create?: '))
for valueNumber in range(1,itemNumber+1):
    valueNumber = eval(input('Please enter %d number: ' % valueNumber))
    list.append(valueNumber)
    list.sort()
print(list)
print(tuple(list))
print(set(list))

# %%
