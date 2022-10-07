word = 'Please Spell 好 in English: ' 
answer = input(word)
while answer.upper() != 'GOOD':
      if answer.upper() == 'FUCK':
            print('I am done with this SHIT!')
            break
            print('FUCK OFF')
      answer = input('Wrong,\n%s' % word)
else:
      print('Correct!')

# %%
a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|%5d%5d|'%(a,b))
print('|%5d%5d|'%(c,d))
print('|%-5d%-5d|'%(a,b))
print('|%-5d%-5d|'%(c,d))

# %%
text = '''save the text to output
1. A
2. B
3.C'''
print(text,file=open('../Output/datatest.txt','w'))

# %%
