# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|%5d %5d|'%(a,b))
print('|%5d %5d|'%(c,d))
print('|%-5d %-5d|'%(a,b))
print('|%-5d %-5d|'%(c,d))

# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|{:5d} {:5d}|'.format(a,b))
print('|{:5d} {:5d}|'.format(c,d))
print('|{:<5d} {:<5d}|'.format(a,b))
print('|{:<5d} {:<5d}|'.format(c,d))

# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|{:7.2f} {:7.2f}|'.format(a,b))
print('|{:7.2f} {:7.2f}|'.format(c,d))
print('|{:<7.2f} {:<7.2f}|'.format(a,b))
print('|{:<7.2f} {:<7.2f}|'.format(c,d))

# %%
a = 23.12
b = 395.3
c = 100.4617
d = 564.329
print('|%7.2f %7.2f|' % (a,b))
print('|%7.2f %7.2f|' % (c,d))
print('|%-7.2f %-7.2f|' % (a,b))
print('|%-7.2f %-7.2f|' % (c,d))

# %%
a = str(input())
b = str(input())
c = str(input())
d = str(input())
print('|{:>10s} {:>10s}|'.format(a,b))
print('|{:>10s} {:>10s}|'.format(c,d))
print('|{:<10s} {:<10s}|'.format(a,b))
print('|{:<10s} {:<10s}|'.format(c,d))

# %%
a = str(input())
b = str(input())
c = str(input())
d = str(input())
print('|%10s %10s|' % (a,b))
print('|%10s %10s|' % (c,d))
print('|%-10s %-10s|' % (a,b))
print('|%-10s %-10s|' % (c,d))

# %%
from importlib import import_module
import math
r = eval(input())
print('Radius =', '{:.2f}'.format(r))
print('Perimeter =', '{:.2f}'.format(2*math.pi*r))
print('Area =', '{:.2f}'.format(math.pi*r**2))

# %%
h = eval(input())
w = eval(input())
print('Height =','{:.2f}'.format(h))
print('Width =','{:.2f}'.format(w))
print('Perimeter =','{:.2f}'.format(2*(h+w)))
print('Area =','{:.2f}'.format(h*w))

# %%
x = eval(input())
y = eval(input())
z = eval(input())
print('Speed = ','{:.1f}'.format((z / 1.6) / ( (y / 60 + x) / 60)))

# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())
vSum = a+b+c+d+e
print('Sum =','{:.1f}'.format(vSum))
print('Average =','{:.1f}'.format(vSum/5))


# %%
import math
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print('(', x1,',', y1, ')' )
print('(', x2,',', y2, ')' )
print('Distance =', '{:.4f}'.format(math.sqrt((x1-x2)**2+(y1-y2)**2)))

# %%
import math
s = eval(input())
print('Area =','{:.4f}'.format((5*math.pow(s,2))/(4*math.tan(math.pi /5))))

# %%
import math
n = eval(input())
s = eval(input())
print('Area =','{:.4f}'.format(n*math.pow(s,2)/(4*math.tan(math.pi/n))))

# %%
