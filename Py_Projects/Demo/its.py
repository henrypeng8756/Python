# %%
def incresScore(score,bonus,points):
    if bonus == True:
        points = points * 3
    score = score * points
    return score
points = 8
score = 12
newScore = incresScore(score, True, points)
print(newScore)

# %%
import datetime
now = datetime.datetime.now()
#now2 = datetime()
#now3 = datetime.date()
today = now.strftime('%A')
today2 = now.strftime('%B')
today3 = now.strftime('%W')
today4 = now.strftime('%Y')
weekday = now.weekday()

# %%

