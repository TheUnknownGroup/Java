import time
line = '------'

questions = ['What is your Username?\n',
             'What is your Password?\n']
username = 'ddr4lover'
password = 'ddr5lover#5'

welcome = 'Welcome! Please Log In with the correct credentials.'
cor = 'incorrect'
inc = 'correct'

def login():
    print(welcome); time.sleep(0.5)
    for s in questions[0]:
        print(s, end='')
    ans1 = input('')
    for s in questions[1]:
        print(s, end='')
    ans2 = input('')
    time.sleep(1)
    if ans1 == username:
        ans1 = 'correct'
    elif ans1 != username:
        ans1 = 'incorrect'
    elif ans2 == passwod:
        ans1 = 'correct'
    elif ans2 != password:
        ans2 = 'incorrect'
    elif ans1 and ans2 == 'incorrect':
        print('Incorrect password & username. Please Try Again.')
    elif ans1 and ans2 == 'correct':
        print('Logging In')
login()