#f = open("read.txt")
# TODO
with open('read.txt','r') as file:
    content = file.read()
    print(sum(list(map(int,(content.split(' '))))))
    