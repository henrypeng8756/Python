#TODO
nameDict = {}
while True:    
    #Key: (後方有一空白格)
    key = input("Key: ")
    if key != 'end':
    #Value: (後方有一空白格)
        value = input("Value: ")
        nameDict = {key:value}
    else:
        findKey = input('Search key: ')
        if findKey in nameDict:
            print('True')
        else:
            print('False')
        break
        
    