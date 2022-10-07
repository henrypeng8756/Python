# %%
nameDict = {}
while True:
    key = input("Key: ")
    if key != 'end':
        value = input("Value: ")
        nameDict[key] = value
        continue
    else:
        i = input('Search key: ')
        if i == nameDict[key]:
            print('True')
        else:
            print('False')
        break

# %%