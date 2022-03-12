import random

num = random.randint(0,1000)

run=True

while(run):
    try:
        userinput = int(input('guess a number: '))
        if userinput==num:
            print('YOU WIN!!!')
            run=False
        elif userinput<=num:
            print('need a LARGER number')
        elif userinput>=num:
            print('need a SMALLER number')
    except:
        print('PLEASE ENTER A NUMBER!!!')
