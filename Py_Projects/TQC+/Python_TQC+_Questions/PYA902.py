# %%
#f = open("read.txt")
# TODO
with open('read.txt','r') as file:
    content = file.read()
    numSum= sum(list(map(eval,(content.split(' ')))))
    print(numSum)