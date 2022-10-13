# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%

from cmath import pi
from email.contentmanager import raw_data_manager
from encodings import utf_8, utf_8_sig
from importlib import import_module
from re import M
from tkinter import N, Y
from tkinter.tix import InputOnly
from turtle import left
from urllib import response
from xml.dom import registerDOMImplementation

from mysqlx import SqlResult

from symbol import import_from


print(1)
print(1+2)
print(1-25*12345)
print(12.345*98.7864541)

# %%

num1=50
num2='50'
num3=50>60
num4=15.51

print(num1)
print(num2)
print(num3)
print(num4)
print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))

# %%

print(int('10'))
print(int(3.14))
print(int(True))
print(int(False))
print(str(1.23))

# %%
print(1+2)
print(1.5+2.3)

print(15-3)
print(20-True)

print(12*21)
print('ABC'*2)

print(6/3)
print(12/True)

print(8//3)
print(108//11)

print(28%10)
print(12.5%10)

print(5**3)
print(3**5)

# %%
print(123 == '123')
print('ABC' == 'abc')

''' == = 是不是, = = 右邊數值等於左邊
'''
print(True == 1)
print(False == 0)

print ((3>2) == True)
print(3>2 == True)

# %%
print((1>2) & (3>2))
print((1>2) and (3>2))

print((1>2) | (3>2))
print((1>2) or (3>2))

print(not(1>2))

# %%
a=3
b=5
c=7
a,b,c = 3,5,7
a *= b
print(a)
c %= 5
print(c)


# %%
# single line comment

'''multiple line comment 
just like this
'''

# %%
name=input()
print(name)

# %%
name=input('Please insert your name:')
print(name)

# %%
PI = 3.1415926
radius = eval(input("Please enter radius value:"))
print('Radius is', radius, "Circular Area is", PI * radius**2 )

# eval 會協助自動轉換至對應的資料型態, 可以使用變數的string, 但是無法單用strings 
#%%
numA=eval(input('First Number'))
numB=eval(input('Second Number'))
numC=eval(input('Third Number'))
numD=eval(input('Forth Number'))

# %%
print(1)
print(1,2,5,True,'xyz')

# %%
name1='Henry'
print('Hello', name1, sep='^^^', end='\n')
print('nice to meet you', end=' ')
print('too')
print('So, ', end='')
print('What is your name', end='???')
print('Hello', name1, sep='', end='\n')

# %%
yourName = input('what is your name')
print(yourName)

# %%
print('Hello, %s' % 'World!')
print('you only have $%d' % 666)
print('%d divide %d is %f' % (20,7,20/7))
print('%5d divide %5d is %.3f' % (20,7,20/7))
print('%-5d divide %-5d is %.3f' % (20,7,20/7))
print('%-8d divide %-8d is %10.3f' % (20,7,20/7))

# %%
PI=3.1415926
print('{:.2f}'.format(PI))
print('{:+.2f}'.format(PI))
print('{:.0f}'.format(PI))
print('{:0>2d}'.format(5))
print('{:x<4d}'.format(10))
print('{:,}'.format(1000000))
print('{:10d}'.format(13))
print('{:<10d}'.format(13))
print('{:^10d}'.format(13))
print('{:.2%}'.format(PI))
print('{:.2e}'.format(100000000000))

# %%
print('{0:d}-{2:b}-{1:o}-{0:x}'.format(10,20,30))
# d eicmal
# b inary
# o ctal
# he x 
# f loat
# s tring 

# %%
print('{0:d} divide {1:d} is {2:f}'.format(10, 3, 10/3))
print('{0:5d} divide {1:5d} is {2:10.2f}'.format(10, 3, 10/3))
print('{n1:5d} divide {n2:5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:<5d} divide {n2:<5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:>5d} divide {n2:>5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:!^5d} divide {n2:?^5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))

# %%
#print('n1%!^5d divide n2%?^5d is r%.2f' % (n1=10, n2=3, r=10/3))
#print('0%!^5d divide 1%?^5d is 2%.2f' % (10, 3, 10/3))
#print('0%^5d divide 1%?^5d is 2%.2f' % (10, 3, 10/3))
#print('0%5d divide 1%?^5d is 2%.2f' % (10, 3, 10/3))
#print('0%5d divide 1%^5d is 2%.2f' % (10, 3, 10/3))

print('0%5d divide 1%5d is 2%.2f' % (10, 3, 10/3))

# %%
sideLength= eval(input('Please Enter Side of the Square: '))
print('Square Side Lengths: ', '{:.2f}'.format(sideLength))
print('Square Perimeter: ', '{:.2f}'.format(sideLength*4))
print('Square Area:', '{:.2f}'.format(sideLength**2))

# %%
long = eval(input('請輸入正方形邊長:'))
print("邊長為:"+'{:.2f}'.format(long), 
      "\n周長為:"+'{:.2f}'.format(4*long), 
      "\n面積為:"+'{:.2f}'.format(long**2), 
            )

# %%
def CtoF1(degreeC):
      degreeF = degreeC * 1.8 + 32 
      print('{:.1f}'.format(degreeC), 'Celcius is ', '{:.1f}'.format(degreeF), 'Fahrenheit')
tempertureC = eval(input('Please Enter Celcius: '))
CtoF1(tempertureC)

# %%
def CtoF2(degreeC2):
      degreeF2 = degreeC2 * 1.8 + 32
      return '{:.1f}'.format(degreeF2)
tempertureC2 = eval(input('Please Enter Celcius: '))
CtoF2(tempertureC2)

# %%
def CtoF2(degreeC2):
      degreeF2 = degreeC2 * 1.8 + 32
      return '{:.1f}'.format(degreeF2)
CtoF2(35.666)

# %%
def teaTime(dessert, drink = 'Black Tea'):
      print('My Dessert: ', dessert, ' ; My Drink: ', drink, sep="")
teaTime('Macaron','Coffee')
teaTime('Panini')
teaTime(drink = 'Milk Tea', dessert= 'Sandwich')
teaTime('Red Bean Cake', drink= 'Green Tea')
# teaTime(drink= 'Green Tea', 'Red Bean Cake')
#      teaTime(drink= 'Green Tea', 'Red Bean Cake')
#                                                 ^
#SyntaxError: positional argument follows keyword argument

# %%
def autoteaTime(myDessert = 'Cheese Cake', myDrink = 'Water'):
      print('Your Dessert: ', '{:s}'.format(myDessert), ' ; Your Drink: ', '{:s}'.format(myDrink), sep="")
orderDessert = str(input('Please Select Your Dessert: '))
orderDrink = str(input('Please Select Your Drink: '))
autoteaTime(orderDessert, orderDrink)

# %%
def cal(x,y):
      div = x // y
      mod = x % y
      return div, mod
a, b = cal(120, 7)
print('120 divide 7 | floor division =', a, ', modulus =',b )
c, d = cal(250, 15)
print('250 divide 15 | floor division =', c, ', modulus =',d )

# %%
x = eval(input())
y = eval(input())
def cal(x,y):
      div = x // y
      mod = x % y
      return div, mod
a, b = cal(x, y)
print( x, 'divide', y, '| floor division =', a, ', modulus =',b )
c, d = cal(x, y)
print( x, 'divide', y, '| floor division =', c, ', modulus =',d )
# %%
x = 100
def test():
      print(x)
test()

# %%
X = 100
def test():
      Y = 200
      return Y
test()
print(test())
Y = test()
print(Y) 

# %%
a = 'Happy' + 'Birthday' + 'to' + 'you'
print(a)

b = 3*'Yeah!'
print(b)

c = 'X' > 'M'
print(c)
# Due to unicode X unicode value is larger than M in unicode 

d = '123' > '456'
print(d)

e = 'for' not in 'forever'
print(e)

# %%
def int01():
      A = 'HENRY'
      return A

def int02():
      B = 'henry'
      return B
A = int01()
B = int02()
print(int01()>int02())
print(X > Y)

# %%
def int01():
      A = str(input())
      return A

def int02():
      B = str(input())
      return B
A = int01()
B = int02()
int01()
int02()
print(A)
print(B)
print(int01()>int02())
print(A > B)

# %%
def a():
      a = 'for'
      return a
def b():
      b = 'forever'
      return b
print(a())
print(b())
print(a() not in b())
a = a()
b = b()
print(a)
print(b)
print(a not in b)

# %%
S = 'Python程式運算'
print(S[2:5])
# expecting tho
print(S[3:8])
# expecting hon程式
print(S[5:-1])
# expecting n程式運
print(S[:-2])
# expecting Python程式
print(S[2:])
# expecting thon程式運算

# %%
S1 = 'HappyNewYear'
S2 = 'happynewyear'
S3 = 'new'
len(S1)
print(S1==S2)
max(S1)
print(S3 in S1)
print(S1[4:9])

# %%
print(ord('A'))
print(ord('$'))

print(chr(65))
print(chr(36))

# %%
X = 'Good Afternoon! How Are you?'
print(X.upper())
print(X.lower())
print(X.swapcase())
print(X.capitalize())
print(X.title())
print(X.replace('oo','xx'))
print(X)

# %%
print(str.isupper('abcde'))
print(str.isupper('ABCDE'))
print(str.islower('abcde'))
print(str.islower('Abcde'))
print(str.isidentifier('a1bcde'))
print(str.isidentifier('1abcde'))
print(str.isspace('  a    '))
print(str.isspace('       '))
print(str.istitle('It Is ok'))
print(str.istitle('It Is Ok'))
print(str.isalpha('ABCDE'))
print(str.isalpha('abcde'))
print(str.isalpha('abcde1'))
print(str.isdigit('12345'))
print(str.isdigit('123.45'))
print(str.isdigit('I'))
print(str.isdigit('一'))
print(str.isdecimal('12345'))
print(str.isdecimal('123.45'))
print(str.isdecimal('I'))
print(str.isdecimal('一'))
print(str.isnumeric('12345'))
print(str.isnumeric('123.45'))
print(str.isnumeric('I'))
print(str.isnumeric('一'))

print('----------------------------')

print('abcde'.isupper())
print('ABCDE'.isupper())
print('abcde'.islower())
print('ABCDE'.islower())
print('a1bcde'.isidentifier())
print('1abcde'.isidentifier())
print('  a   '.isspace())
print('      '.isspace())
print('It Is ok'.istitle())
print('It Is Ok'.istitle())
print('ABCDE'.isalpha())
print('abcde'.isalpha())
print('abcde1'.isalpha())
print('12345'.isdigit())
print('123.45'.isdigit())
print('I'.isdigit())
print('一'.isdigit())
print('12345'.isdecimal())
print('123.45'.isdecimal())
print('I'.isdecimal())
print('一'.isdecimal())
print('12345'.isnumeric())
print('123.45'.isnumeric())
print('I'.isnumeric())
print('一'.isnumeric())

# %%
Y = 'HiHiHiHiHi'
print(Y.count('Hi'))
print(Y.startswith('Hi'))
print(Y.startswith('HiH'))
print(Y.endswith('HiH'))
print(Y.endswith('iHi'))
print(Y.find('iHi'))
print(Y.rfind('iHi'))

# %%
X = 'A B C D E'
Y = X.split()
print(Y)

# %%
X = '1,3,5,7,9'
Y = X.split(',')
print(Y)

# %%
print('     abcde       '.strip())
print('abcxyzd ef'.strip('abcdef'))

# %%
Z = 'tw.yahoo.com'
print(Z.strip('.omtw'))
print(Z.rstrip('tomw'))
print(Z.strip('tomw'))

# %%
X = 'Hello Python'
print(X.center(20))
print(X.ljust(20))
print(X.rjust(20))
print(X.zfill(6))
print(X.zfill(20))

# %%
PI=3.1415926
print('{:.2f}'.format(PI))
print('{:+.2f}'.format(PI))
print('{:.0f}'.format(PI))
print('{:0>2d}'.format(5))
print('{:x<4d}'.format(10))
print('{:,}'.format(1000000))
print('{:10d}'.format(13))
print('{:<10d}'.format(13))
print('{:^10d}'.format(13))
print('{:.2%}'.format(PI))
print('{:.2e}'.format(100000000000))

# %%
print('{0:d}-{2:b}-{1:o}-{0:x}'.format(10,20,30))
# d eicmal
# b inary
# o ctal
# he x 
# f loat
# s tring 

# %%
print('{0:d} divide {1:d} is {2:f}'.format(10, 3, 10/3))
print('{0:5d} divide {1:5d} is {2:10.2f}'.format(10, 3, 10/3))
print('{n1:5d} divide {n2:5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:<5d} divide {n2:<5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:>5d} divide {n2:>5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))
print('{n1:!^5d} divide {n2:?^5d} is {r:.2f}'.format(n1=10, n2=3, r=10/3))

# %%
print(abs(50))
print(abs(-50))
print(pow(2,5))
print(pow(3,4))
print(divmod(100,8))
print(divmod(125,9.5))

# %%
print(max(10,20,30))
print(max(-10,-20,-30))
print(max(True,-20,-30))
print(min(1,3,False))
print(max('a','b','c'))
print(min('A','b','c'))

# %%
print(bin(100))
print(oct(100))
print(hex(100))

# %%
print(int(666.666))
print(int('666'))
# print(int('666.666'))
# print(int('六六六'))

# %%
print(float(666))
print(float('666'))
print(float('666.666'))
# print(float('六六六'))

# %%
print(round(123.123))
print(round(123.123,2))
print(round(-567.567))
print(round(-567.567,2))
print(round(5.5))
print(round(6.5))
print(round(-5.5))
print(round(-6.5))
# print(round('999'))

# %%
import random
num = random.randint(1,3)
answer = eval(input('Please Guess the Number from 1 ~ 3: '))
print(num,'==',answer, 'is', num == answer)

# %%
import math
print(max(10,9,-8,200,77,-120,50))
print(min(10,9,-8,200,77,-120,50))
print(10**2*math.pi)
print(math.gcd(616,1331))

# %%
print(format(123,'^10'))
print(format(123,'!^10'))
print(format(123456789,','))

# %%
print(format(1234.5678,'10.2f'))
print(format(1234.5678,'<10.2f'))

# %%
def compute(x,y):
      multi = x*y
      return multi
x = eval(input())
y = eval(input())
print(compute(x,y))

# %%
a = 100
b = 200
if a>b:
      print(a)

# %%
x = 15
y = 10 
if x > y :
      z = x - y
      print('x is',z ,'more than y')

# %%
score = eval(input('Please Insert Your Math Score: '))
if score >= 60:
      print('Pass!')
else:
      print('Fail!')

# %%
num1 = 50
num2 = 40
if num1 > num2:
      print('True !')

print('===========')
if bool(num1 > num2):
      print('True !')

# %%
num2 = eval(input())
if num2 > 100:
      num3 = 30
print(num3)
# %%
# def test():
#       numa = 30
# print(numa)
# will Fail

# %%
score = eval(input('Please Insert Your Math Score: '))
if score >= 90:
      print('You got an A!')
elif score >= 80:
      print('You got a B!')
elif score >= 70:
      print('You got a C!')
elif score >= 60:
      print('You got a D!')
else:
      print('You failed!')

# %%
score = eval(input('Please Insert Your Math Score: '))
if score >= 90:
      print('You got an A!')
else:
      if score >= 80:
            print('You got a B!')
      else:
            if score >= 70:
                  print('You got a C!')
            else:
                  if score >= 60:
                        print('You got a D!')
                  else:
                        print('You failed!')
# %%
i = 0
while i < 5:
      print(i)
      i = i + 1

# %%
x = 'Please Spell 快樂 in English:'
answer = input(x)
while answer.upper() != "HAPPY":
      answer = input('Wrong! Please try again!\n %s' % x)
else:
      print('Correct!')

# %%
list(range(5))
print(list(range(5)))
# range(stop)
list(range(1,10))
# range(start,stop)
list(range(10,-10,-2))
# range(start,stop,step)

# %%
for i in range(5):
      print(i)

# %%
name = 'Bob'
for i in range(len(name)):
      print(i,name[i])

# %%
name ='Bob'
for i in name:
      print(i, name[0:3])
      
# %%
word = 'Please Spell 好 in English: ' 
answer = input(word)
while answer.upper() != 'GOOD':
      if answer.upper() == 'QUIT':
            print('Practice makes perfect!\nSee you next time!')
            break
            print('Bye!')
      elif answer.upper() == 'FUCK':
            print('FUCK YOU')
            break
            print('FUCK OFF')
      answer = input('Wrong,\n%s' % word)
else:
      print('Correct!')

# %%
i = 0
while i < 10:
      i = i + 1
      if i % 3 != 0:
            continue
            i = i + 2
      print(i)

# %%
for n in range(1,5,2):
      print(n, end='')
print(n)

# %%
sum = 0
n = 8 
for i in range(1,n+1,2):
      sum += i
print(sum)

# %%
# list = []
# tuple = ()
# dict = {}

# %%
X = list()
print(X)

Y = list([1,2,3])
print(Y)

# %%
X2 = []
print(X2)

Y2 = [1,2,3]
print(Y2)

# %%
list1 = [1, 2.5, 'xyz', False]
print(type(list1))
print(list1[0])
print(list1[2])

# %%
L = [3,6,9,12,15,18,21,24,27,30]
del L[2]
del L[3]
print(L)

# %%
a = [3,6,9]
b = [2,5,8.5,'Hello']
c = []
d = [16,[a,b]]
e = a + b

b[0] = 42
x = a[1]
y = b[1:3]
z = d[1][0][1]
print(x)
print(y)
print(z)


# %%
print([1,2,3]+[4,5,6])
print([1,2,3]+['A','B','C'])
print([1,2,3]+['A', True, 2.5, 0])

# %%
print(3*[1,2,3])
print(['A', 2, 10.5, True]*3)

# %%
print([1,3,4,'X']==['X',3.5,1])
print([1,2,3]==[3,2,1])

# %%
print(3 in [1,2,3,4,5])
print('Y' in ['XYZ','ABC'])
print('XYZ' in ['XYZ','ABC'])

# %%
L = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(L[1:5])
print(L[2:-2])

# %%
listc=[i for i in range(10)]
print(listc)
listc2=[j+3 for j in range(10)]
print(listc2)

# %%
list1 = [1,3,5,7,9]
list2 = [2,5,8,11,14]
list1.append(11)
print(list1)
list1.extend(list2)
print(list1)
print(list1.count(11))
print(list1.index(9))
list1.insert(3,999)
print(list1)
list1.pop()
print(list1)
list1.remove(5)
print(list1)
list1.reverse()
print(list1)
list1.pop(5)
print(list1)

# %%
X = [1,3,2,4,5]
print(sorted(X))
print(X)
X.sort()
print(X)

# %%
print(pow(2,7,6))
print(2**7%6)

# %%
tup = tuple()
print(tup)
tup2 = tuple((1,3,5))
print(tup2)
tup3 = ()
print(tup3)
tup4 = (2,4,6)
print(tup4)

# %%
a = (3,5,2,6)
b = ()
c = (2,[4,6],(10,11,12))
print(a[1])
print(a[1:3])
print(c[1][1])

# %%
tup = (3,False,'XYZ')
# tup = a,b,c
a,b,c = tup
print(a)
print(b)
print(c)

# %%
a, *b=(1,3,5,7,9)
print(a)
print(b)
x, *y, z=(2,4,6,8,10)
print(x)
print(y)
print(z)

# %%
x1 =[(1,2),[3,4]]
y1 =([5,6],(7,8))
x1[0] = 20
print(x1)
# y1[0] = 30

# %%
x2 =[(1,2),[3,4]]
y2 =([5,6],(7,8))
# x2[0][0] = 20
y2[0][0] = 30
print(y2)

# %%
x3 = [(1,2),[3,4]]
y3 = list((i for i in range(10)))
print(x3)
print(y3)

# %%
i = eval(input('Please give a number: '))
sumList = list((i for i in range(0,i+1,7)))
print('The sum of multiples of 7 from 1 to %d is %d' %(i,sum(sumList)))

# %%
A = set()
A.add(3)
A.add('ABC')
A.add(True)
print(A)

# %%
X = {'a','b',1,2}
Y = {1,2,'a','b'}
print(X==Y)
print(X)
print(Y)

# %%
S1 = {1,1,2,2,2,2,3,3,5,5,6,6,6,}
S2 = {6,3,1,5,2,2,5,3,1,2}
print(S1==S2)
print(S1)
print(S2)

# %%
S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7}
# S3 = S1 +S2 
print(S1-S2)
# print(S1[1:3])
# print(S2[2])

# %%
A = {1,5,3,7,9,5,7,3}
print(len(A))
print(max(A))
print(min(A))
print(sum(A))

# %%
X = {'A':567,'B':789}
Y = {'B':789, 'A':567}
print(X==Y)
print(X)
print(Y)

# %%
A = {'one':1, 'two':2, 'three':3}
B = dict({'three':3, 'one':1, 'two':2 })
C = dict(one=1, two=2, three=3)
D = dict([('two',2),('one',1),('three',3)])
print(A==B==C==D)
print(A)
print(B)
print(C)
print(D)

# %%
A = {}
A['1']=10
A['2']=20
A['3']=30
print(A)

# %%
A = {'one':1, 'two':2, 'three':3}
del A['one']
print(A)

# %%
A = {'one':1, 'two':2, 'three':3}
X=A['one']
print(X)
A['two']=200
print(A['two'])

# %%
A = {'a':1, 'b':2, 'c':3}
B = {'a':1, 'b':2, 'c':9}
print(A['a']==B['a'])
print(A['b']==B['b'])
print(A['c']==B['c'])
print(1 in A)
# print(a in A)
print('a' in A)

# %%
A = {'a':1, 'b':2, 'c':3}
B = {'a':7, 'b':2, 'c':9}
# print(A+B)
# print(A*2)
# print(A[0])
# print(A['a':'c'])

# %%
dic = {'X':123, 'Y':456, 'Z':789}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

# %%
text = '''save the text to output
1. A
2. B
3.C'''
print(text,file=open('data.txt','w'))

# %%
file = open('Output/data.txt','r')
content = file.read()
print(content)
file.close()

# %%
data = {"name":"CityParkMsYaHei1602","dataColors":["#73B761","#4A588A","#ECC846","#CD4C46","#71AFE2","#8D6FD1","#EE9E64","#95DABB","#8FC581","#6E79A1","#F0D36B","#D7706B","#8DBFE8","#A48CDA","#F1B183","#AAE1C9","#568949","#384268","#B19635","#9A3935","#5583AA","#6A539D","#B3774B","#70A48C","#3A5C31","#252C45","#766423","#672623","#395871","#473869","#774F32","#4B6D5E"],"background":"#FFFFFF","foreground":"#070f25","tableAccent":"#0F1934","textClasses":{"label":{"fontFace":"'Microsoft Yahei'","fontSize":14},"callout":{"fontFace":"'Microsoft Yahei'","fontSize":23},"title":{"fontFace":"'Microsoft Yahei'","fontSize":14},"header":{"fontFace":"'Microsoft Yahei'","fontSize":14}}}
for i in data:
    print(i)
    print(data[i],'\n')

# %%
print(open('/Users/henrypeng/Desktop/CDRI/Python/Py_Projects/Output/data.txt'))

# %%
file = open('/Users/henrypeng/Desktop/CDRI/Python/Py_Projects/Output/writedata.txt','w')
file.write('寫入檔案\n')
file.write('ABCDE\n')
file.write('12345')
file.close()

file = open('Output/writedata.txt','r')
content = file.read()
print(content)
file.close()

# %%
with open('Output/writedata.txt','w') as file:
      file.write('寫入檔案\n')
      file.write('ABCDE\n')
      file.write('12345')

file = open('Output/writedata.txt','r')
content = file.read()
print(content)
file.close()

# %%
import random
file = open('/Users/henrypeng/Desktop/CDRI/Python/Py_Projects/Output/rand_num.txt','w')
for i in range(10):
      file.write(str(random.randint(1,100))+'\n')
file.close()

file = open('Output/rand_num.txt','r')
content = file.read()
print(content)
file.close()

nameList = ['Henry', 'Ken', 'Wen']
for i, name in enumerate(nameList):
    print('No.%d : %s ' % (i+1, name))

# %%
nameList = ['Henry', 'Ken', 'Wen']
for i, name in enumerate(nameList, 1):
    print('No.%d : %s' % (i, name))

# %%
countryCode = ['TW', 'JP', 'US', 'UK', 'AU']
countryNum = ['886', '81', '1', '44', '62']
code = zip(countryCode, countryNum)
for i in code:
    print(i)

# %%
countryCode = ['TW', 'JP', 'US', 'UK', 'AU']
countryNum = ['886', '81', '1', '44', '62']
info = {}
for name, i in zip(countryCode, countryNum):
    info[name] = i
print(info)

# %%
numList = [1, 2, 3, 4, 5]


def cal(x):
    return x**2


result1 = list(map(cal, numList))
print(result1)

result2 = list(map(lambda x: x**3, numList))
print(result2)

# %%
numList1 = [1, 2, 3, 4, 5]
numList2 = [10, 20, 30]


def cal(x, y):
    return x+y


result = list(map(cal, numList1, numList2))
print(result)

# %%
numList1 = ['100', '200', '300', '400']
newList = list(map(int, numList1))
print(newList)

# %%
list1 = [0, 2.5, False, 30]


def cal(x):
    if x > 0:
        return x


ans1 = list(filter(cal, list1))
print(ans1)

ans2 = list(filter(lambda x: x > 1, list1))
print(ans2)

# %%
ans1 = list(filter(None, [0, 1, 2, 3, 4, 5]))
print(ans1)

list1 = [i for i in range(6)]


def cal(x):
    if x % 2 == 0:
        return x


ans2 = list(filter(cal, list1))
print(ans2)

ans3 = list(filter(lambda x: x % 2 == 0, list1))
print(ans3)

# %%


def show(*args):
    print(args)


show(3)
show(3, 12, 41)

# %%
########


def show(*aa):
    for i in aa:
        return aa


# %%
def ans1(): return 2020


print(ans1())

# %%
ans2 = list(map(lambda x: x*10, [i for i in range(1, 6)]))
print(ans2)

# %%


def ans3(x, y): return x+y


print(ans3(2, 9))

# %%
ans4 = lambda *args: sum(args)
print(ans4)

#%%
ans5 = lambda **kwargs: kwargs
print(ans5(name='Henry', age=15))

# %%
x = []
for i in range(1, 6):
    x.append(i)
print(x)

# %%
x = [i for i in range(1, 6)]
print(x)

# %%
x = [eval(i) for i in range(1, 6)]
print(x)

# %%
x = [1 for i in range(1, 6)]
print(x)

# %%
x = [0 for _ in range(1, 6)]
print(x)

# %%
x = [i == 0 for i in range(1, 6)]
print(x)

# %%
x = [1 for _ in range(1, 6)]
print(x)
# %%
# %%
import calendar
print(calendar.month(2022,9))

# %%
import calendar as cal
print(cal.month(2022,9))


# %%
from calendar import month
print(month(2022,9))

# %%
from calendar import *
print(month(2022,9))

# %%
import csv
loc = 'Output/csv_test.csv'
with open(loc,encoding='utf8') as csvFile:
      csvReader = csv.reader(csvFile)
      listReport = list(csvReader)
print(listReport)

# %%
data=['1','2',3.545]
convtintData = map(int,data)
print(convtintData)

# %%
data = ['1', '2', 3.545]
data = list(data)
convtlistData = list(map(int, data))
print(convtlistData)

# %%
import csv
i = 'Output/Scenic_Spot_C_f.csv'
with open(i) as file:
      content = csv.reader(file)
      convrtList = list(content)
print(convrtList)

with open(i) as file:
    data = list(csv.reader(file))
print(data)

# %%
import csv
i = 'Output/Scenic_Spot_C_f.csv'
with open(i) as file:
      content = csv.reader(file)
      convrtList = list(content)
print(convrtList[:8])

# %%
i = 'Output/Scenic_Spot_C_f.csv'
with open(i) as file:
    content = csv.reader(file)
    convrtList = list(content)
print(convrtList[13])

# %%
i = 'Output/Scenic_Spot_C_f.csv'
with open(i) as file:
    content = csv.reader(file)
    convrtList = list(content)
print(list(convrtList))
print(max(convrtList))

with open(i) as file:
    data = list(csv.reader(file))
print(data)

# %%
import csv
fn = 'Output/csvoutput.csv'
with open(fn,'w',newline='',encoding='utf_8_sig') as csvFile:
      csvWriter = csv.writer(csvFile)
      csvWriter.writerow(['姓名','電話','ID','費用','是否前往'])
      csvWriter.writerow(['李小明','(886)9739238434','C123218934',100,True])
      csvWriter.writerow(['李大強','(886)9328458723','C678342345',200,False])
with open(fn,'r') as csvFile:      
      csvReader = csv.reader(csvFile)
      csvList = list(csvReader)
      print(csvList)

# %%
import csv
infn = 'Output/csvoutput.csv'
outfn = 'Output/csvOReport.csv'
with open(infn,encoding='utf_8_sig') as csvRFile:
      csvReader = csv.reader(csvRFile)
      listReport = list(csvReader)

with open(outfn,'w',newline='',encoding='utf_8_sig') as csvOFile:
      csvWriter = csv.writer(csvOFile)
      for row in listReport:
            csvWriter.writerow(row)

# %%
import xml.etree.ElementTree as et
tree = et.ElementTree(file='Samples/menu.xml')
menu = tree.getroot()
print(menu.tag)
for breakfast in menu:
      print(f'tag: {breakfast.tag} attributes: {breakfast.attrib}')
      for item in breakfast:
            print(f'\ttag: {item.tag} attributes {item.attrib}')
print(len(menu))
print(len(menu[0]))

# %%
import xml.etree.ElementTree as et
tree = et.ElementTree(file='Samples/country_data.xml')
root = tree.getroot()
for country in root.findall('country'):
      rank = int(country.find("rank").text)
      if rank > 50:
            root.remove(country)
tree.write("Output/xmloutput.xml", encoding='utf_8')

# %%
import json
fn = 'Output/jsonObject.json'
with open(fn) as fnObj:
      data = json.load(fnObj)
print(data)
print(type(data))

# %%
fn = 'Output/jsonArray.json'
with open(fn) as fnArry:
      data = json.load(fnArry)
print(data)
print(type(data))

# %%
import json
dictobject = {'x':60, 'y':55, 'z':90}
fn= 'Output/pytojsonObject.json'
with open(fn, 'w') as fnObj:
      json.dump(dictobject, fnObj)

# %%
listarray = [{'x':"一二三", 'y':55, 'z':90},{'a':10, 'b':25, 'c':30}]
fn= 'Output/pytojsonArray.json'
with open(fn,'w') as fnArry:
      json.dump(listarray,fnArry,ensure_ascii=False)

# %%
import json
fn = 'Samples/jobasEdu.json'
with open(fn,encoding='utf8') as jsonFile:
      jsonContent=json.load(jsonFile)
      for item in jsonContent:
            print([item['年度'],item['大職業別'],item['經常性薪資-薪資']])

# %%
import urllib.request
res = urllib.request.urlopen('http://python.org')
content=res.read()
print(content)

# %%
res = urllib.request.urlopen('https://google.com.tw')
content = res.read()
print(content)

# %%
import requests
website = 'https://bit.ly/2OU9LQb'
#website = 'https://reurl.cc/xQbq6z'
response = requests.get(website)
print(response.status_code)
record = response.headers
print(record)
data = response.json()
print(data['success'])
print(data['result'])

# %%
import requests
url = 'https://data.gov.tw/'
html_body = requests.get(url)
html_body.encoding='utf_8'
print(html_body.text)

# %%
data = '''<html><head><title>The Dormouse's story</title></head> <body> <p class="title"><b>The Dormouse's story</b></p> <p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> <p class="story">...</p>

'''
from bs4 import BeautifulSoup as bs
soup = bs(data,'lxml')
#print(soup)
print(type(soup))
# print(data.prettify()) # wrong 
#print(soup.prettify())
print(soup.b.prettify())
print(soup.p.prettify())
print(soup.a)
print(soup.find('a'))
print(soup.find('a').text)
print(soup.find(id='link1').text)
#print(soup.find(class='link1').text) #wrong
print(soup.find(class_='title').text)
print(soup.find(class_='sister').text)
print(soup.find(href='http://example.com/tillie').text)
print(soup.p.text)
print(soup.title.string)

# %%
data = '''<html><head><title>The Dormouse's story</title></head> <body> <p class="title"><b>The Dormouse's story</b></p> <p class="story">Once upon a time there were three little sisters; and their names were <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p> <p class="story">...</p>

'''
soup = bs(data, 'lxml')
print(soup.title)
print(soup.head)
print(soup.head.title)
print(soup.title.string)
print(soup.find_all('p'))
for link in soup.find_all('a'):
      print(link.get('href'))
for className in soup.find_all('p'):
      print(className.get('class'))
print(soup.prettify)

# %%
from bs4 import BeautifulSoup
html_text = '''
<html><head><title>國立臺灣大學系統</title></head>
<body>
<p class="title"><b>三校聯盟 NTU SYSTEM</b></p>
<p class="ntu_system">
<a href="http://www.ntu.edu.tw" class="union" id="link1">臺灣大學</a>
<a href="http://www.ntnu.edu.tw" class="union" id="link2">臺灣師範大學</a>
<a href="http://www.ntust.edu.tw" class="union" id="link3">臺灣科技大學</a>
</p></body></html>
'''
bs = BeautifulSoup(html_text,'html.parser')
print('1:',bs.title)
print('2:',bs.find('a'))
print('3:',bs.find('b'))
print('4:',bs.find_all('a',{'class':'union'}))
print('5:',bs.find('a',{'id':'link1'}))
print('6:',bs.find('a',{'href':'http://www.ntust.edu.tw'}))
web = bs.find('a',{'id':'link1'})
print('7_1:',web)
print('7:',web.get('href'))
data = bs.select('.union') # due to CSS | .union == class='union' | . == class= |
print('8_1:', data)
print('8:',data[0].text)
print('9:',data[1].text)
print('10:',bs.select("#link3")) # due to CSS | #link3 == id='link3' | # == id= |

# %%
import time
import numpy as np
def calculatetime():
      a = np.random.rand(1000000)
      b = list(a)
      start_time = time.time()
      for _ in range(100):
            sum1 = np.sum(a)
      print('Using NumPy\t %f sec' %(time.time()-start_time))
      
      start_time = time.time()
      for _ in range(100):
            sum2 = sum(b)
      print('Not using NumPy\t %f sec' %(time.time()-start_time))
calculatetime()

# %%
import numpy as np
X = np.array(([1,2,3],[4,5,6]))
Y = np.array([(1,2,3),(4,5,6)])
print(type(X))
print(type(Y))
print(X)
print(Y)

# %%
import numpy as np
data1 = [1,2,3,4,5]
array1 = np.array(data1)
print(array1)

# %%
import numpy as np
data2 = [[1,2,3,4,5],[6,7,8,9,10]]
array2 = np.array(data2)
print(array2)

# %%
import numpy as np
data = [1,2,3,4,5]
array1 = np.array(data)
array2 = np.array(data, dtype=float)
array3 = np.array(data, dtype=bool)
print(type(array1))
print(array1)
print(type(array2))
print(array2)
print(type(array3))
print(array3)

# %%
import numpy as np
print(np.zeros((3,5)))
print()
print(np.ones((3,2)))
print()
print(np.arange(3,20,2))
print()
print(np.linspace(0,100,21))

# %%
import numpy as np
a = np.array([[3,6,9],[2,4,6]])
print(a)
print('T\n',a.T,'\n')
print('ndim:', a.ndim)
print('shape:',a.shape)
print('type:',type(a))
print('dtype:',a.dtype)
print('data:',a.data)
print('size:',a.size)
print('itemsize',a.itemsize)
print('nbytes',a.nbytes)

# %%
import numpy as np
x = np.random.randn(5,4)
print(x)
print()
print(type(x))
print()
print(x.mean())
print()
print(x.sum())
print()
print(x.min())
print()
print(x.max())
print()
print(x.std())
print()
print(x.ptp())
print()
x = np.array([[2,3,4],[5,6,7]])
print(x.cumsum)
print()
print(x.cumsum())
print()
print(np.std(x))

# %%
a = [i for i in range(1,6)]
b = [j for j in range(6,12)]
x = [a,b]
print(type(x))
print(x)
y = x[1][1:]
print(type(y))
print(y)

y[1]=200
print(type(y))
print(y)
print(type(x))
print(x)


# %%
import numpy as np
x = np.arange(12).reshape(2,6)
print(type(x))
print(x)
y = x[1][1:]
print(type(y))
print(y)

y[1]=200
print(type(y))
print(y)
print(type(x))
print(x)

# %%
import numpy as np
rowList = []
for row in range(6):
      rowList.append(np.array(row))
      for column in range(0,51,10):
            rowList.append(np.array(row+column))
print(rowList)

# %%
import numpy as np
x = np.arange(12).reshape(3,4)
print(x)
y = x[[0,1,2],[2,1,0]]
print(y)

# %%
import numpy as np 
x = np.arange(12).reshape(3,4)
print(x)
z = x[np.ix_([0,2],[1,3])]
print(z)

# %%
import numpy as np
arr = np.arange(10)
print(arr)
slice = arr[5:8]
print(slice)
print(arr)
arr[5:8]=7
print(slice)
print(arr)
slice[1]=87
print(slice)
print(arr)

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,11)
y = x**2
plt.plot(x,y)
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,linewidth =3)
plt.plot(x,y2,lw = 8)
plt.show()

# %%
x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, linewidth=3, color="c")
plt.plot(x, y2, lw=8, color="y")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, linewidth=8, color="#00ffff")
plt.plot(x, y2, lw=8, color=(255/255,0/255,0/255))
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,5,0.1)
plt.plot(x,x,"b--",x,x**2,"ro",x,x**3,"g+")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,10)
plt.plot(x,x, "--", marker="x")
plt.plot(x,x**2, "--", marker="o")
plt.plot(x,x**3, "--", marker="^" )
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
plt.rcParams["font.family"] = "PingFang TC"
plt.rcParams["font.size"] = 20
plt.rcParams['axes.unicode_minus'] = False

font_path = '/System/Library/Fonts/PingFang.ttc'
font_prop = fm.FontProperties(fname=font_path)

x = np.arange(1,11)
y = x**2
plt.plot(x,y,"--",marker="^")
plt.title("折線圖")
plt.xlabel("X 軸座標圖", size=10)
plt.ylabel("Y 軸", size=15, rotation=0)
plt.show()

# %%
# cd /usr/local/lib/python3.10/site-packages/matplotlib/mpl-data/fonts/ttf
# fc-list :lang=zh
import matplotlib
matplotlib.matplotlib_fname()

# %%
import matplotlib.font_manager
 
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
 
for i in a:
    print(i)

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,10)
plt.plot(x,x**3,"--",marker="^")
plt.axis([0,20,0,100])
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,10)
plt.plot(x,x*5,"--",marker="o")
plt.xlim(-10,10)
plt.ylim(0,80)
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

data = {"2010年":[3512,5241,1254],"2011年":[4000,4514,3590],"2012年":[5120,4120,5350]}
x = [1,2,3]
y1, y2, y3 = data["2010年"],data['2011年'],data['2012年']
labels =['Year 2010','Year 2011','Year 2012']
plt.xticks(x,labels)
plt.plot(x,y1,"g",x,y2,"r",x,y3,"b")
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

data = {"2010年":[3512,5241,1254],"2011年":[4000,4514,3590],"2012年":[5120,4120,5350]}
x = [1,2,3]
y1, y2, y3 = data["2010年"],data['2011年'],data['2012年']
labels =['Year 2010','Year 2011','Year 2012']
plt.xticks(x,labels)
plt.figure(figsize=(6,8), facecolor='#D1BBFF')
plt.plot(x,y1,"g",label='Product_A')
plt.plot(x,y2,"r",label='Product_A')
plt.plot(x,y3,"b",label='Product_A')
plt.legend(loc=5)
plt.grid()
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,500)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1,label="sin")
plt.plot(x,y2,label="cos")
plt.legend()
plt.grid()
plt.show()

# %%
x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(6,8), facecolor='#D1BBFF')
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")
plt.legend()
plt.grid()
plt.show()

# %%
import matplotlib.pyplot as plt 

y1 = x = [i for i in range(1,9)]
y2 = [i**2 for i in range(1,9)]

plt.figure(1)
plt.plot(x,y1,"r-*")
plt.plot("chatr 1")
plt.show()

plt.figure(2)
plt.plot(x,y2,"b-+")
plt.plot("chatr 2")
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
plt.rcParams['font.family'] = 'PingFang TC'
plt.rcParams['font.size'] = 20
font_path = '/System/Library/Fonts/PingFang.ttc'
fm.FontProperties(fname=font_path)
x = np.arange(1, 10)
plt.plot(x, x, "--", marker="x", label='一次方')
plt.plot(x, x**2, "--", marker="o", label='二次方')
plt.plot(x, x**3, "--", marker="^", label='三次方')
plt.title("折線圖", loc='left', color='#4621c2', fontstyle='normal')
plt.xlabel("X軸座標")
plt.ylabel("Y軸座標",rotation=90)
plt.axis([0,10,0,800])
plt.legend()
plt.grid()
plt.show()

# %%
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2,2,1, facecolor="g")
plt.subplot(2,2,2, facecolor='r')
plt.subplot(2,1,2)
plt.show()

# %%
import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2,1,1)
plt.subplot(2,2,3,facecolor='g')
plt.subplot(2,2,4,facecolor="r")
plt.show()

# %%
import matplotlib.pyplot as plt
x = [x for x in range(5)]
y = [y**2 for y in range(11,21)]
z = [z for z in range(10,0,-1)]
plt.figure()
plt.subplot(2,2,1, facecolor='#C4DDB1')
plt.plot(x)
plt.subplot(2,2,2,facecolor='#E6A8E6')
plt.plot(y)
plt.subplot(2,1,2,facecolor='#F3F599')
plt.plot(z)
plt.show()

# %%
import matplotlib.pyplot as plt
plt.figure()
plt.subplot2grid(shape=(3,3),loc=(0,0),rowspan=1,colspan=3,facecolor='r')
plt.subplot2grid(shape=(3,3),loc=(1,0),rowspan=1,colspan=2,facecolor='b')
plt.subplot2grid((3,3),(1,2),2,1,facecolor='g')
plt.subplot2grid((3,3),(2,0),facecolor='y')
plt.subplot2grid((3,3),(2,1),facecolor='w')
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
x = np.arange(1,10)
plt.plot(x,x**3,'--',marker='^')
plt.savefig("Output/123.jpg")
plt.show()

# %%
import matplotlib.pyplot as plt
name = ['Java', 'C++', 'Python', 'JavaScript', 'Objective-C']
student = [101, 87, 98, 67, 80]
plt.figure(1)
plt.bar(name, student, align='edge', color='#D55772')
plt.figure(2)
plt.bar(name,student)
plt.figure(3)
plt.bar(name, student, align='edge', color='#D55772')
plt.bar(name, student)
plt.show()

# %%
import matplotlib.pyplot as plt
name = ["Java", 'C++', 'Python', 'JavaScript', 'Objective-C']
student = [101, 87, 98, 67, 80]
plt.bar(name, student, width=1.0)
plt.show()

# %%
import matplotlib.pyplot as plt
name = ["Java", 'C++', 'Python', 'JavaScript', 'Objective-C']
student = [101, 87, 98, 67, 80]
plt.bar(name, student, hatch='o', color='#FFCC00')
plt.show()

# %%
import matplotlib.pyplot as plt
name = ["Java", 'C++', 'Python', 'JavaScript', 'Objective-C']
student = [101, 87, 98, 67, 80]
plt.barh(name,student)
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams['font.family'] = ['PingFang TC']
font_path = '/System/Library/Fonts/PingFang.ttc'
fm.FontProperties(fname=font_path)
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area)
plt.title('五月份國外旅遊調查表',fontsize=16)
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams['font.family'] = ['PingFang TC']
font_path = '/System/Library/Fonts/PingFang.ttc'
fm.FontProperties(fname=font_path)
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people, labels=area, autopct='%d%%')
plt.title('五月份國外旅遊調查表',fontsize=16)
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams['font.family'] = ['PingFang TC']
font_path = '/System/Library/Fonts/PingFang.ttc'
fm.FontProperties(fname=font_path)
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
exp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.1]
plt.pie(people, labels=area, autopct='%d%%', explode=exp)
plt.title('五月份國外旅遊調查表',fontsize=16)
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams['font.family'] = ['PingFang TC']
font_path = '/System/Library/Fonts/PingFang.ttc'
fm.FontProperties(fname=font_path)
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
exp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.3]
plt.pie(people, labels=area, autopct='%d%%', explode=exp, shadow=True)
plt.title('五月份國外旅遊調查表',fontsize=16)
plt.show()

# %%
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcParams['font.family'] = ['PingFang TC']
font_path = '/System/Library/Fonts/PingFang.ttc'
fm.FontProperties(fname=font_path)
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
color = ['aqua','g','pink','yellow','m','#0022ff']
plt.pie(people,labels=area, autopct='%d%%', colors=color)
plt.title('五月份國外旅遊調查表',fontsize=16)
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,21)
y = np.random.randint(1,10,20)
plt.scatter(x,y)
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np
x = color = np.arange(1,21)
y = np.random.randint(1,10,20)
plt.scatter(x,y, c=color, s=100)
plt.show()

# %%
import pandas as pd
ss = pd.Series([1,-3,5,7])
print(ss)
print('- - - - -')
print('- - - - -')
print(ss.values)
print(ss.index)

# %%
import pandas as pd
ss1 = pd.Series([4,7,-5,3], index=['a','b','c','d'])
print(ss1.index)
print(ss1['a'])
print('a' in ss1)
print( 7 in ss1)
print(7 in ss1.values)

# %%
import pandas as pd
list_ex = ["A",123,"B",4.56,"C",True]
list_to_Series=pd.Series(list_ex)
print(list_to_Series)
print('-'*10)
print(type(list_to_Series[0]))
print(type(list_to_Series[1]))
print(type(list_to_Series[2]))
print(type(list_to_Series[3]))
print(type(list_to_Series[4]))
print(type(list_to_Series[5]))
print('-'*10)

dic_ex={"A":123,"B":4.56,"C":True}
dic_to_Series=pd.Series(dic_ex)
print(dic_to_Series)
print('-'*10)
print(type(dic_to_Series["A"]))
print(type(dic_to_Series["B"]))
print(type(dic_to_Series["C"]))

# %%
import pandas as pd
X = [['Amy','F',80],['Bob','M',65],['Dave','M',46],['Eva','F',46]]
df1 = pd.DataFrame(X,columns=['Name','Gender','Mathgrade'])
print("-----顯示資料一--索引方式-----")
print(df1['Name'])
print(df1['Name'].values)
print(df1['Name'][1])
#print(df1['Name'][1].value)

# %%
import pandas as pd
df = pd.read_csv('Samples/csvsample.csv')
print(df.ndim)
print('---')
print(df.shape)
print('---')
print(df.dtypes)
print('---')
print(df.head(6))
print('---')
print(df.tail(6))
print('---')
print(df.info())
print('---')

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
print(df['Name'])
print(df['Name'][0:6])
print(df[['Name','Team']].head(10))

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
df.insert(1,column='Sport',value='Checked')
print(df.head())
# df = df.drop('Sport',axis = 1)
df.drop('Sport',axis = 1, inplace=True)
print(df.head())
print('---')
df = df.drop(0,axis = 0)
print(df.head())

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
df.insert(1,column='Sport',value='Checked')
print(df.head())
df.dropna(inplace=True)
print(df.head())

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
df.insert(1,column='Sport',value='Checked')
print(df.head())
df.fillna(10000,inplace=True)
print(df.head())

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
print(df.head(6))
print(df.sort_values('Age').head(6))
print(df.sort_values('Name',ascending=False).head(6))

# %%
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows',None)
df = pd.read_csv('Samples/nba.csv')
print(df['Age'].head(10) >= 25)
mask = (df['Age'] >= 25)
print(df[mask].head(8))
mask1 = df['Age'] < 29
print(df[mask1 & mask].head(8))
# print(df[mask][mask1].head(8))
# UserWarning: Boolean Series key will be reindexed to match DataFrame index.
mask2 = (df['Age'].between(20,28))
print(df[mask2].head(8))
mask3 = df['Age'].isin([25,28,32])
print(df[mask3].head(8))

# %%
import pandas as pd
col = ['Class','Name','Bday']
data = [['ClassA','小明','1995-08-01'],
['ClassB','小美','1995-10-02'],
['ClassC','小黃','1995-06-01'],
['ClassC','小陳','1993-11-03'],
['ClassA','小花','1996-01-02'],
['ClassB','小雨','1996-02-03']]
frame = pd.DataFrame(data,columns=col)
frame_class = frame.groupby('Class')
print(frame_class.groups)
print(frame_class.get_group('ClassA'))

# %%
import numpy as np
import pandas as pd
df = pd.DataFrame({
      'A': ['foo','bar','foo','bar','foo','bar','foo','foo'],
      'B': ['one','one','two','three','two','two','one','three'],
      'C': np.random.randn(8),
      'D': np.random.randn(8)
})
print(df)
print(df.groupby('A').sum())
# FutureWarning: The default value of numeric_only in DataFrameGroupBy.sum is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
print(df.groupby(['B','A']).sum())

# %%
import numpy as np 
import pandas as pd
df = pd.DataFrame({
      'key1':['A','B','A','C','B','D','C','D','A','C'],
      'data1': np.random.randn(10),
      'data2': np.random.randn(10)
})
print(df)
print()
sector = df.groupby('key1')
print(sector)
print()
print(type(sector))
print()
print(sector.size())
print(sector.get_group('A'))
print(sector.get_group('B'))

# %%
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(5,3),\
      index=list('ABCDE'),columns=list('XYZ'))
print(df)
print()
print(df.loc['A','X'])
print()
print(df.loc['B':'D',:])
print()
print(df.loc[:,'X':'Y'])
print()
print(df.loc['A':'C','X':'Y'])
print()
print(df.loc[['B','E'],['X','Z']])

# %%
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.rand(3,3),\
      index=list('xyz'),columns=list('XYZ'))
print(frame)
print()
print(frame.iloc[0,0])
print()
print(frame.iloc[0:2,:])
print()
print(frame.iloc[:,0:2])
print()
print(frame.iloc[0:2,0:2])
print()
print(frame.iloc[[0,2],[0,2]])

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
df.to_csv('Output/nba_2.csv')
df.to_csv('Output/nba_3.csv',index=0)
df.to_csv('Output/nba_4.csv',index=False, header=0)

# %%
import pandas as pd
df = pd.read_csv('Samples/nba.csv')
df.to_csv("Output/nba2.csv")
df0 = pd.read_csv('Output/nba2.csv')
print(df0.head(6))
df1 = pd.read_csv('Output/nba2.csv', index_col=0)
print(df1.head(6))
df2 = pd.read_csv('Output/nba2.csv', index_col=False, header=None)
print(df2.head(6))

# %%
import numpy as np
import pandas as pd
x1 = np.random.rand(100,1)
y1 = np.random.randn(100,1)
x2 = np.random.rand(100,4)
y2 = np.random.randn(100,4)
df1 = pd.DataFrame(x1,index=pd.date_range('3/1/22', periods=100),\
      columns=list('A'))
df2 = pd.DataFrame(y1,index=pd.date_range('3/1/22', periods=100),\
      columns=list('A'))
df3 = pd.DataFrame(x2,index=pd.date_range('3/1/22', periods=100),\
      columns=list('ABCD'))
df4 = pd.DataFrame(y2,index=pd.date_range('3/1/22', periods=100),\
      columns=list('ABCD'))
df1.plot()
df2.plot()
df3.plot()
df4.plot()

df1 = df1.cumsum()
df2 = df2.cumsum()
df3 = df3.cumsum()
df4 = df4.cumsum()
df1.plot()
df2.plot()
df3.plot()
df4.plot()

# %%
import numpy as np
import pandas as pd
x1 = np.random.randn(10000,1)
df1 = pd.DataFrame(x1,index=pd.date_range('3/1/22', periods=10000),\
      columns=list('A'))
df1.plot()

# %%
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(500,3), columns=list('xyz'),\
      index= pd.date_range('1/1/2022', periods=500))
df = df.cumsum()
df.plot(colormap='gray').set_ylabel('Value', fontsize=12)
df2 = pd.DataFrame(np.random.rand(5,3), columns=['a','b','c'])
df2.plot(kind='bar', fontsize=12,)
df2.plot(kind='bar', fontsize=12, stacked=True)

# %%
import sqlite3
con = sqlite3.connect('Output/test.sql')
sqlstr = 'CREATE TABLE IF NOT EXISTS table01 \
      ("num" INTEGER PRIMARY KEY NOT NULL, "tel" TEXT)'
con.execute(sqlstr)
sqlstr = 'INSERT INTO table01 VALUES(1, "02-1234567")'
con.execute(sqlstr)
sqlstr = '''INSERT INTO table01(num, tel)\
      VALUES(2,"03-2345678"),(3, "04-3456789")'''
con.execute(sqlstr)
con.commit()
con.close()

# %%
import sqlite3
conn = sqlite3.connect('Output/test.sqlite')
cursor = conn.execute('SELECT * FROM table01')
print(cursor)
print()

rows = cursor.fetchall()
print(rows)
print()

for row in rows:
      print('{:d}\t{:s}'.format(row[0],row[1]))
conn.close()

# %%
import sqlite3 
conn = sqlite3.connect('Output/test.sqlite')
cur = conn.execute('SELECT * FROM table01')
for row in cur:
      print(row)
# %%
import sqlite3
conn = sqlite3.connect('Output/test.sqlite')
cur = conn.execute('SELECT * FROM table01 where num=1')
row = cur.fetchone()
if row != None:
      print('{}\t{}'.format(row[0],row[1]))
conn.close()

# %%
import sqlite3
conn = sqlite3.connect('Output/test.db')
print('Opened database successfully')
c = conn.cursor()
c.execute("CREATE TABLE COMPANY \
      (`ID` INT PRIMARY KEY NOT NULL,\
      `NAME` TEXT NOT NULL,\
      `AGE` INT NOT NULL,\
      `ADDRESS` CHAR(50),\
      `SALARY` REAL)")
print("Table created successfully")
conn.commit()
conn.close()

# %%
import sqlite3
conn = sqlite3.connect('Output/test.db')
print('Opened database successfully')
c = conn.cursor()
c.execute("CREATE TABLE COMPANY \
      (`ID` INT PRIMARY KEY NOT NULL,\
      `NAME` TEXT NOT NULL,\
      `AGE` INT NOT NULL,\
      `ADDRESS` CHAR(50),\
      `SALARY` REAL)")
print("Table created successfully")
c.execute("INSERT INTO COMPANY (`ID`,`NAME`,`AGE`,`ADDRESS`,`SALARY`) \
      VALUES (1, 'Paul', 32, 'California', 20000.00), \
            (2, 'Allen', 25, 'Texas', 15000.00), \
            (3, 'Teddy', 23, 'Norway', 20000.00), \
            (4, 'Mark', 25, 'Rich-Mond', 65000.00)")
conn.commit()
print("Records created successfully")
conn.close()

# %%
import sqlite3
conn = sqlite3.connect('Output/test.db')
c = conn.cursor()
cursor = c.execute("SELECT `id`, `name`, `address`, `salary` from COMPANY")
for row in cursor:
      print('ID = ', row[0])
      print('NAME = ', row[1])
      print('ADDRESS = ', row[2])
      print('SALARY = ', row[3], "\n")
print('Operation done successfully')
conn.close 

# %%
import mysql.connector as mariadb
#conn_params={
#      'user': 'pytest',
#      'password': '1qazXSW@',
#      'host': '192.9.238.252',
#      'database': 'pytest'
#}
# http://192.9.238.252/phpMyAdmin/server_privileges.php?db=pytest&checkprivsdb=pytest&viewing_mode=db
con = mariadb.connect(
      user= 'pytest', # 輸入登入帳號
      host= '192.9.238.252', # 輸入MariaDB IP
      password= '2wsxCDE#', # 輸入登入密碼
      database= 'pytest' # 輸入
)
cursor= con.cursor()

sqlCreateTable = '''CREATE TABLE IF NOT EXISTS Countries \
      (`Name` VARCHAR(128) PRIMARY KEY NOT NULL,`Country_Code` TEXT, `Capital` TEXT)'''
cursor.execute(sqlCreateTable)

sqlInsert = "INSERT INTO Countries(`Name`, `Country_Code`, `Capital`) VALUES (?,?,?)" #("Japan","JPN","Tokyo"),("Taiwan", "TWN", "Taipei"),("Germany","GER","Berlin")'''  # ("Japan","JPN","Tokyo"),("Taiwan", "TWN", "Taipei"),("Germany","GER","Berlin")
countryData = ("Japan","JPN","Tokyo") 
cursor.execute(sqlInsert, countryData)
con.commit()

sqlSelectData = "SELECT `name`, `country_code`, `capital` FROM Countries"
cursor.execute(sqlSelectData)

row = cursor.fetchone()
print(row,sep=' ')

con.commit()
cursor.close()
con.close()

# %%
import sqlite3
book = 'P0002, Python, 500'
f = book.split(',')
conn = sqlite3.connect('Output/csvBooks.sqlite')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Books \
      (`ID` INT PRIMARY KEY NOT NULL,\
      `Title` TEXT NOT NULL,\
      `Price` REAL)")
sql = "INSERT INTO Books (`ID`, `Title`, `Price`) VALUES ('{0}','{1}',{2})"
sql = sql.format(f[0],f[1],f[2])
print(sql)
cursor = conn.execute(sql)
print(cursor.rowcount)
conn.commit()
conn.close()

# %%
import sqlite3
d = {
      'id': 'P0003',
      'title': 'Node.js程式設計',
      'price': 650
}
conn = sqlite3.connect("Output/jsonBooks.sqlite")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Books \
      (`ID` INT PRIMARY KEY NOT NULL,\
      `Title` TEXT NOT NULL,\
      `Price` REAL)")
sql = "INSERT INTO Books (`ID`, `Title`, `Price`) VALUES ('{0}','{1}',{2})"
sql = sql.format(d['id'],d['title'],d['price'])
print(sql)
cursor = conn.execute(sql)
print(cursor.rowcount)
conn.commit()
conn.close()

# %%
import sqlite3
import csv
with open('Output/全國5大超商資料集.csv','r',encoding= 'utf_8') as file:
      content = csv.reader(file)
      cvrtList = list(content)
conn = sqlite3.connect('Output/store.sqlite')
c = conn.cursor()
print('Opened database successfully','\n')
c.execute("CREATE TABLE IF NOT EXISTS Stores \
      (`Store_Name` TEXT, \
      `Branch_ID` PRIMARY KEY NOT NULL , \
      `Branch` TEXT, `Address` TEXT)")
print('Table created successfully','\n')
for rows in cvrtList[1:]:
      csvInsert = "INSERT INTO Stores(Store_Name, Branch_ID, Branch, Address) \
            VALUES('{0}', {1}, '{2}', '{3}')"
      sql = csvInsert.format(rows[1],rows[2],rows[3],rows[4])
      print(sql)
      c.execute(sql)
conn.commit()
conn.close()


# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
temperatures = np.array([29,28,34,31,25,29,32,31,24,33,25,31,26,30])
drink_sales = np.array([7.7,6.2,9.3,8.4,5.9,6.4,8.0,7.5,5.8,9.1,5.1,7.3,6.5,8.4])
x = pd.DataFrame(temperatures, columns=['Temperatures'])
y = pd.DataFrame(drink_sales, columns=['Drink_Sales'])
lm = LinearRegression()
lm.fit(x,y)
print('迴歸係數:', lm.coef_)
print('截距:',lm.intercept_)
new_temperatures = pd.DataFrame(np.array([26,30]), columns=['Temperatures'])
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)
plt.scatter(temperatures, drink_sales)
regression_sales = lm.predict(x)
plt.plot(temperatures, regression_sales, color='blue')
plt.plot(new_temperatures, predicted_sales, color='red', marker='o', markersize=10)
plt.show()

# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
waist_heights = np.array([[67,160],[68,165],[70,167],[65,170],[80,165],\
      [85,167],[78,178],[79,182],[95,175],[89,172]])
weights = np.array([50,60,65,65,70,75,80,85,90,81])
x = pd.DataFrame(waist_heights, columns=['Waist','Height'])
y = pd.DataFrame(weights,columns=['Weights'])
lm = LinearRegression()
lm.fit(x,y)
print('迴歸係數: ', lm.coef_)
print('截距: ', lm.intercept_)
new_waist_heights = pd.DataFrame(np.array([[66,164],[82,172]]))
predicted_weights = lm.predict(new_waist_heights)
print(predicted_weights)

# %%
from sklearn import datasets
# use of regressions
boston = datasets.load_boston()
diabetes = datasets.load_diabetes()
# use of catagorized
iris = datasets.load_iris()
digits = datasets.load_digits()

print(boston.keys())
print(diabetes.keys())
print(iris.keys())
print(digits.keys())
print(boston['target'])
print(boston.DESCR)
print(boston.values())

# %%
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
temperatures = np.array(
    [29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
drink_sales = np.array([7.7, 6.2, 9.3, 8.4, 5.9, 6.4,
                       8.0, 7.5, 5.8, 9.1, 5.1, 7.3, 6.5, 8.4])
x = pd.DataFrame(temperatures, columns=['Temperatures'])
y = pd.DataFrame(drink_sales, columns=['Drink_Sales'])
lm = LinearRegression()
lm.fit(x, y)
print('迴歸係數:', lm.coef_)
print('截距:', lm.intercept_)
new_temperatures = pd.DataFrame(np.array([26, 30]), columns=['Temperatures'])
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)
plt.scatter(temperatures, drink_sales)
regression_sales = lm.predict(x)
plt.plot(temperatures, regression_sales, color='blue')
plt.plot(new_temperatures, predicted_sales,
         color='red', marker='o', markersize=10)
plt.show()

# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
waist_heights = np.array([[67, 160], [68, 165], [70, 167], [65, 170], [80, 165],
                          [85, 167], [78, 178], [79, 182], [95, 175], [89, 172]])
weights = np.array([50, 60, 65, 65, 70, 75, 80, 85, 90, 81])
x = pd.DataFrame(waist_heights, columns=['Waist', 'Height'])
y = pd.DataFrame(weights, columns=['Weights'])
lm = LinearRegression()
lm.fit(x, y)
print('迴歸係數: ', lm.coef_)
print('截距: ', lm.intercept_)
new_waist_heights = pd.DataFrame(np.array([[66, 164], [82, 172]]))
predicted_weights = lm.predict(new_waist_heights)
print(predicted_weights)

# %%
from sklearn import datasets
# use of regressions
boston = datasets.load_boston()
diabetes = datasets.load_diabetes()
# use of catagorized
iris = datasets.load_iris()
digits = datasets.load_digits()

print(boston.keys())
print(diabetes.keys())
print(iris.keys())
print(digits.keys())
print(boston['target'])
print(boston.DESCR)
print(boston.values())

# %%
from sklearn import datasets
boston = datasets.load_boston()
print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

# %%
import pandas as pd
from sklearn import datasets
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
print(x.head())
target = pd.DataFrame(boston.target, columns=['MEDV'])
print(target.head())

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
lm = LinearRegression()
lm.fit(x,y)
print('迴歸係數: ',lm.coef_)
print('截距: ', lm.intercept_)
coef = pd.DataFrame(boston.feature_names, columns=['features'])
coef['estimatedCoefficients'] = lm.coef_
print(coef)
plt.scatter(x.RM,y)
plt.xlabel('Average number of rooms per dwelling(RM)')
plt.ylabel('Housing Price(MEDV)')
plt.title('Relationship between RM and Price')
plt.show()

# %%
# print multiple df testing
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
lm = LinearRegression()
lm.fit(x,y)
print('迴歸係數: ',lm.coef_)
print('截距: ', lm.intercept_)
a = boston.feature_names
coef = pd.DataFrame(boston.feature_names, columns=['features'])
print(coef)
coef['estimatedCoefficients'] = lm.coef_
print(coef)
for i in coef:
    plt.scatter(x[i],y)
    plt.xlabel('Average number of rooms per dwelling(RM)')
    plt.ylabel('Housing Price(MEDV)')
    plt.title('Relationship between RM and Price')
    plt.show()

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston = datasets.load_boston()

x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
lm = LinearRegression()
lm.fit(x,y)

predicted_price = lm.predict(x)
print(predicted_price[0:5])

plt.scatter(y, predicted_price)
plt.xlabel('Price')
plt.ylabel('Predicted Price')
plt.title('Price vs Predicted Price')
plt.show()


# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(xTrain,yTrain)
pred_test = lm.predict(xTest)
plt.scatter(yTest, pred_test)
plt.xlabel('Price')
plt.ylabel('Predicted Price')
plt.title('Price vs Predicted Price')
plt.show()

# %%
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split as tts
iris_data = load_iris()
data = iris_data.data
target =iris_data.target
x_train, x_test, y_train, y_test = tts(data, target, test_size=0.25)

# %%
import random
for i in range(5):
    print(random.randint(1,100))

# %%
import random
random.seed(101)
for i in range(5):
    print(random.randint(1,100))

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import numpy as np 
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(xTrain, yTrain)
pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)
MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
print('訓練資料的MSE: ', MSE_train)
print('測試資料的MSE: ', MSE_test)
print('訓練資料的R-Square: ', lm.score(xTrain, yTrain))
print('測試資料的R-Square: ', lm.score(xTest, yTest))


# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import numpy as np 
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']

xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(xTrain, yTrain)

pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)

plt.scatter(pred_train,yTrain-pred_train, c='b', s=40, alpha=0.5, label='Training Data')
plt.scatter(pred_test, yTest-pred_test, c='r', s=40, label='Test Data')
plt.title('Residual Plot')
plt.ylabel('Residual Value')
plt.legend()
plt.show()

# %%
from bokeh.plotting import figure, show
x = [0,1,2,3,4]
y = [0,1,4,9,16]
p = figure(plot_width=500, plot_height=500)
p.line(x,y)
show(p)

# %%
from bokeh.plotting import figure, show
x = [0,1,2,3,4]
y = [0,1,4,9,16]
p = figure(plot_width=500, plot_height=500)
p.line(x,x,line_color='blue',legend_label='linear', line_dash='dashed')
p.line(x,y,line_color='#FF4310', legend_label='quad', line_dash='solid')
show(p)

# %%
from bokeh.plotting import figure, show
x = [0,1,2,3,4]
y = [0,1,4,9,16]
p = figure(title='Sample Line Example',plot_width=500, plot_height=500)
p.diamond_dot(x,x,size=15, color='#ED8D21')
p.line(x,x,line_color='blue',legend_label='linear', line_dash='dashed', line_width=3, )
p.circle(x,y,size=15, color='#ED8D21')
p.line(x,y,line_color='#FF4310', legend_label='quad', line_dash='solid', line_width=3)
show(p)

# %%
from bokeh.io import output_file, show
from bokeh.plotting import figure

output_file("Output/bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

p = figure(x_range=fruits, height=250, title="Fruit counts")
           #toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9) 

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)

# %%
import bokeh.plotting import figure, show 
import numpy as np

x = np.arrange(10)
y = np.random.randint(1,10,10)
p = figure()
p.circle(x,y,size=15, colot )