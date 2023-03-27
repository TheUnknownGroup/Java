import time

line = '------'
playerName = ['What is Player 1s name?', 'What is Player 2s name?', 'What is Player 3s name?', 'What is Player 4s name?']
come = ', COME ON DOWN!!!!'

def retry():
    retryYes = input('Hello! I was told you wanted to retry this game?\n')
    if retryYes in ['yes','Yes','y','sure']:
        print('Well you\'re in good luck then. You\'ve come to the right place. You will now restart your game.'); time.sleep(5); print(line)
        ask_questions()
def priceIsRight2(s,s1):
    print('Welcome to the Price is Right, everyone!\nFor the first item...'); time.sleep(2); print(line)
    money0 = int(input(f'What is your guess {s}?\n'))
    money4 = int(input(f'What is your guess {s1}?\n'))
    if money0 > 1500 or money4 > 1500:
        print('WHOAAA, You went wayyy to far.')
        if abs(1000 - money0) < abs(1000 - money4):
            print(f'{s} CONGRATS! You beat {s1}!')
        else:
            print(f'{s1} CONGRATS! You beat {s}!')
    elif money0 >= 1000:
        print(f'{s} CONGRATS! You won this prize!!')
    elif money4 >= 1000:
        print(f'{s1} CONGRATS! You won this prize')
    elif money0 < 500 or money4 < 500:
        print('Nope, Too low.')
        if abs(1000 - money0) < abs(1000 - money4):
            print(f'{s} CONGRATS! You beat {s1}!')
        else:
            print(f'{s1} CONGRATS! You beat {s}!')
    elif money0 <= 1000:
        print(f'{s} CONGRATS! You won this prize')
    elif money4 <= 1000:
        print(f'{s1} CONGRATS! You won this prize')
    trys = input('Do you want to retry?\n')
    if trys in ['yes','Yes','y','sure']:
        print('You will go to the restart area.')
        retry()
    else:
        print('Welp, Thanks for playing!')
        exit()
def priceIsRight4(so,so1,so2,so3):
    print('Welcome to the Price is Right, everyone!\nFor the first item...'); time.sleep(2); print(line)
    money = int(input(f'What is your guess {so}?\n'))
    money1 = int(input(f'What is your guess {so1}?\n'))
    money2 = int(input(f'What is your guess {so2}?\n'))
    money3 = int(input(f'What is your guess {so3}?\n'))
    if money > 1500 or money1 > 1500:
        print('WHOAAA, You went wayyy to far.'); time.sleep(1)
        if abs(1000 - money) < abs(1000 - money1):
            print(f'{so} CONGRATS! You beat {so1}!')
        else:
            print(f'{so1} CONGRATS! You beat {so}!')
    elif money2 > 1500 or money3 > 1500:
        print('WHOAAA, You went wayyy to far.')
        if abs(1000 - money) < abs(1000 - money1):
            print(f'{so2} CONGRATS! You beat {so3}!')
        else:
            print(f'{so3} CONGRATS! You beat {so2}!')
    elif money >= 1000:
        print(f'{so} CONGRATS! You won this prize!!')
    elif money1 >= 1000:
        print(f'{so1} CONGRATS! You won this prize!!')
    elif money2 >= 1000:
        print(f'{so2} CONGRATS! You won this prize!!')
    elif money3 >= 1000:
        print(f'{so3} CONGRATS! You won this prize!!')
    elif money < 500 or money1 < 500:
        print('Nope, Too low.')
        if abs(1000 - money) > abs(1000 - money1):
            print(f'{so} CONGRATS! You beat {so1}!')
        else:
            print(f'{so1} CONGRATS! You beat {so}!')
    elif money2 < 500 or money3 < 500:
        print('Nope, Too low.')
        if abs(1000 - money) > abs(1000 - money1):
            print(f'{so2} CONGRATS! You beat {so3}!')
        else:
            print(f'{so3} CONGRATS! You beat {so2}!')
    elif money <= 1000:
        print(f'{so} CONGRATS! You won this prize')
    elif money1 <= 1000:
        print(f'{so1} CONGRATS! You won this prize')
    elif money2 <= 1000:
        print(f'{so2} CONGRATS! You won this prize')
    elif money3 <= 1000:
        print(f'{so3} CONGRATS! You won this prize')
    trys = input('Do you want to retry?\n')
    if trys in ['yes','Yes','y','sure']:
        print('You will go to the restart area.')
        retry()
    else:
        print('Welp, Thanks for playing!')
        exit()
def count():
    counts = input('Would you like to add more people or just keep it at that number?\n')
    if counts in ['add more','Add more','Add More','add More','add','more','people','yes','Yes','y','sure']:
        print(f'You will now go back to the beginning to then add more people.\n{line}')
        time.sleep(1)
        ask_questions()
def price_is_rightCalling4(so,so1,so2,so3):
    print(so+come); time.sleep(5)
    print(so1+come); time.sleep(5)
    print(so2+come); time.sleep(5)
    print(so3+come); time.sleep(2)
    print('You are the first four contestants on the PRICE. IS. RIGHT!!')
    return so,so1,so2,so3
def price_is_rightCalling2(s,s1):
    print(s+come); time.sleep(5)
    print(s1+come); time.sleep(2)
    print('You are the first two contestants on the PRICE. IS. RIGHT!!')
    return s,s1
def name2():
    s = input(str(playerName[0]).lstrip('[\'').rstrip('\']')+'\n')
    s1 = input(str(playerName[1]).lstrip('[\'').rstrip('\']')+'\n')
    print(f'Welcome Player {s} and Player {s1}. You will now go to the game.'); time.sleep(3); print(line)
    return s,s1
def name4():
    global so
    so = input(str(playerName[0]).lstrip('[\'').rstrip('\']')+'\n')
    global so1
    so1 = input(str(playerName[1]).lstrip('[\'').rstrip('\']')+'\n')
    global so2
    so2 = input(str(playerName[2]).lstrip('[\'').rstrip('\']')+'\n')
    global so3
    so3 = input(str(playerName[3]).lstrip('[\'').rstrip('\']')+'\n')
    print(f'Welcome Players {so}, {so1}, {so2}, {so3}. You will now go to the game.'); time.sleep(3); print(line)
    return so,so1,so2,so3
def ask_questions():
    global players
    players = int(input('How many players are we beginning with?\n'))
    if players < 2:
        print(f'Sorry not possible with less than 2 people.\n{line}'); time.sleep(1)
        count()
    elif players == 2:
        print(f'You will now begin the Price is Right with 2 players.\n{line}'); time.sleep(1)
        s,s1 = name2()
        price_is_rightCalling2(s,s1)
        priceIsRight2(s,s1)
    elif players == 3:
        print(f'Sorry not possible with 3 people.\n{line}'); time.sleep(1)
        count()
    elif players == 4:
        print(f'You will now begin the Price is Right with 2 or more players.\n{line}'); time.sleep(1)
        so,so1,so2,so3 = name4()
        price_is_rightCalling4(so,so1,so2,so3)
        priceIsRight4(so,so1,so2,so3)
    return players

ask_questions()