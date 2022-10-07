# %%
letterList = set()
allletterList = set()
k = eval(input())
for times in range(1,k+1):
    sentence = str.lower(input())
    for letters in 'abcdefghijklmnopqrstuvwxyz ':
        allletterList.add(letters)
        letterList.discard(letters)
    for alpha in sentence:
        letterList.add(alpha)
    if letterList == allletterList:
        print('True')
    else:
        print('False')    
# %%
