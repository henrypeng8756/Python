# TODO
numList = []
while True:
    n = eval(input())
    if n != 9999:
        numList.append(n)
    else:
        print(min(numList))