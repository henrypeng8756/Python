
f = open('read.txt')
w = f.read()
data = w.split()
data = list(map(eval, data))
print(sum(data))
