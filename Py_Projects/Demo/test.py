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
#%%台北市與松山區一起的折線圖
#匯入套件
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
##################################################################################
#設定畫布相關設定（中文

plt.rcParams["font.family"] = ["PingFang TC", 'PingFang HK', 'Songti SC']
plt.rcParams["font.size"] = 20
plt.rcParams['axes.unicode_minus'] = False

font_path = '/System/Library/Fonts/PingFang.ttc'
font_prop = fm.FontProperties(fname=font_path)

sns.color_palette("bright") #預設的調色盤
# sns.palplot(current_palette)
##################################################################################

#讀取檔案名稱
taipei_data=pd.read_csv("~/Downloads/taipei_data.csv", encoding='utf_8')
#所需的欄位#header=None ~欄位名稱變01234索引 ;header=1~欄位名稱就是變第二列變成欄位標頭ＥＸ：文山區

plt.title("疫情前後台北市與松山區平均房價變化") #圖的標題
###############################################################################
#x軸
x_quarter=taipei_data["year_quar"]
plt.xlabel("107年第一季～111年第三季")    # x軸的名稱
plt.xticks(rotation=45)
# plt.xticks(x_quarter)
###############################################################################
#y1軸台北的值
y1_unitprice_tai=taipei_data["taipei_unit_price"]
y1_unit_prices=[]
for i in y1_unitprice_tai:
    y1_unit_price=round(i/10000,2)
    y1_unit_prices.append(y1_unit_price)
plt.ylabel("每一季的平均單價(萬元/坪)")     # y軸的名稱
#y2軸台北的值
y2_unitprice_song=taipei_data["song_unit_price"]
y2_unit_prices_song=[]
for i in y2_unitprice_song:
    y2_unit_price=round(i/10000,2)
    y2_unit_prices_song.append(y2_unit_price)

plt.ylim(40,100)  #將y軸起始值做設定
# plt.yticks(y_taipei_unit_price,rotation=90)
##############################################################################

sns.set(style="white")  #白色網格背景
sns.despine(top=True,right=True) #移除上方跟右方的框線
plt.plot(x_quarter,y1_unit_prices,marker="o",lw=2.8,label='台北市平均房價')
plt.plot(x_quarter,y2_unit_prices_song,marker="o",lw=2.8,label='松山區平均房價')

# plt.bar(y_taipei_unit_price,rotation=45)
#設定圖利
plt.legend()
plt.savefig("taipei_and_songshan_price.png",bbox_inches='tight',dpi=400)
plt.show()
# %%
