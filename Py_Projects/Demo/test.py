# %%
import requests
dayList = []
for week in range(1, 5):
    print('Week %d:' % (week))
    for days in range(1, 4):
        i = float(input('Day %d:' % (days)))
        dayList.append(i)
print('Average:', '%.2f' %(sum(dayList)/12))
print('Highest:', max(dayList))
print('Lowest:', min(dayList))
# %%
import requests
url = 'https://www.codejudger.com/target/5201.html'
context = requests.get(url)
context_list = context.
#word = str(input('請輸入欲搜尋的字串 : '))
print(context_list)
#context_list = context.split(' ')

# %%
count = 0
for row in context_list:
    if row == word:
        count += 1
if count == 0:
    print(word, '搜尋失敗')
    print('出現 0 次')
else:
    print(word, '搜尋成功')
    print('出現 %d 次'%count)

# %%
