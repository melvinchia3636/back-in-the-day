print('SIMPLE CALCULATOR')
print('-----------------------------')
print('What you want to calcutate?')
calculation = list(input(''))

if '+' in calculation:
    print('Your answer is: ', int(calculation[0])+int(calculation[2]))
elif '-' in calculation:
    print('Your answer is: ', int(calculation[0])+int(calculation[2]))
elif '*' in calculation:
    print('Your answer is: ', int(calculation[0])+int(calculation[2]))
elif '/' in calculation:
    print('Your answer is: ', int(calculation[0])+int(calculation[2]))
else:
    print('INVALID')
