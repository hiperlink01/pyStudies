#-*- coding: UTF-8 -*-

exp = input('Type your mathematical expression to see if it is valid: ')
if exp.index(')') < exp.index('('):
    print('Your expression is not valid.')
else:
    print('Your expression is valid') if exp.count(')') == exp.count('(') \
    else print('Your expression is not valid.')