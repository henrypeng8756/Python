num = eval(input())
if num >= 10 and num <= 15:
    print((str.upper(hex(num))).lstrip('0X'))
else:
    print(num)
# TODO