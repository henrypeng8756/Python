#TODO
dayList = []
for weeks in range(1,5):
    print(f'Week {weeks}:')
    for days in range(1,4):
        daytemp = eval(input(f'Day {days}:'))
        dayList.append(daytemp)
print('Average: %.2f'%(sum(dayList)/12))
print(f'Highest: {max(dayList)}')
print(f'Lowest: {min(dayList)}')

"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""