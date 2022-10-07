# %%
import numpy as np
times=0
cardList = {'cards':[{'A': 1}, {'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6},
            {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 11}, {'Q': 12}, {'K': 13}]}
answer = 11  # np.random.randint(13)
while True:
    guess = '2' #input(print('猜猜看撲克牌數字是多少?'))
    times += 1
    print(cardList)
    if guess.upper() in cardList['cards'][answer].keys():
        print(f'恭喜你！猜{times}次就對了～')
        break
    elif guess.upper() in cardList['cards'][-1].keys():
        del cardList['cards'][-1]
        print('猜錯囉，你的數字太大，介於%s~%s，請重新輸入' \
            %(str(cardList['cards'][0].keys()).strip("dict_keys([''])"),\
                str(cardList['cards'][-1].keys()).strip("dict_keys([''])")))
    elif guess.upper() in cardList['cards'][0].keys():
        del cardList['cards'][0]
        print('猜錯囉，你的數字太小，介於%s~%s，請重新輸入' \
            % (str(cardList['cards'][0].keys()).strip("dict_keys([''])"),\
                str(cardList['cards'][-1].keys()).strip("dict_keys([''])")))
    elif guess < answer:
        for i in cardList[guess:-1]:
            del cardList['cards'][i]
    else:
        break
#        if guess > 0:
#            print(guess)#'猜錯囉，你的數字太小，介於%s~%s，請重新輸入'\
#                  #% (guess, str(cardList['cards'][-1].keys()).strip("dict_keys([''])")))
#        elif True: #int(str(cardList['cards'][guess].values).strip("dict_values([''])")) < answer+1:
#            print('猜錯囉，你的數字太大，介於%s~%s，請重新輸入'
#                  % (guess, str(cardList['cards'][-1].keys()).strip("dict_keys([''])")))
#        else:
#            print('撲克牌只有A~10,J,Q,K 請重新輸入')
#    continue   
    
 # %%
cardDictstr = {'cards': [{'A': '1'}, {'2': '2'}, {'3': '3'}, {'4': '4'}, {'5': '5'}, {'6': '6'},
            {'7': '7'}, {'8': '8'}, {'9': '9'}, {'10': '10'}, {'J': '11'}, {'Q': '12'}, {'K': '13'}]}
cardDictint = {'cards': [{'A': 1}, {'2': 2}, {'3': 3}, {'4': 4}, {'5': 5}, {'6': 6},
            {'7': 7}, {'8': 8}, {'9': 9}, {'10': 10}, {'J': 11}, {'Q': 12}, {'K': 13}]}
#cardList = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J': 11, 'Q': 12, 'K': 13}
#g = input()
print(cardDictint)
guess = 'K'
#del cardDict['cards'][-1]
for i in range(1,14):
    print('number: ', i)
    print('1: ', cardDictint['cards'][0].keys())
    print('2: ', cardDictint['cards'][-1].keys()) 
    print('3: ', cardDictint['cards'][i-1].values())
    print('4: ',('12' == cardDictint['cards'][i-1].values()))    
    print(int(str(cardDictint['cards'][guess].keys()).strip("dict_keys([''])")))
    print(cardDictint['cards'][guess].values())
print(cardDictint)
#if g not in cardList:
#    print('not in')
#else:
#    print('in')
# %%
a = '1'
a.upper()
print(a)
print(type(a))
# %%
