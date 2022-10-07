# TODO
# -b+(((b**2)-(4*a*c))**0.5)/(2*a)
def compute():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    proof = (b**2)-(4*a*c)
    if proof < 0:
        print('Your equation has no root.')
    elif proof == 0:
        print('%s'%(-b/(2*a)))
    else:
        print(f'{(-b+proof**0.5)/(2*a)}, {(-b-proof**0.5)/(2*a)}')
compute()
"""
Your equation has no root.
"""