import time
line = '------'

questions = ['What is your Username?\n',
             'What is your Password?\n']
username = 'ddr4lover'
password = 'ddr5lover#5'

welcome = 'Welcome! Please Log In with the correct credentials.'

def login():
    print(welcome); time.sleep(0.5)
    for s in questions[0]:
        print(s, end='')
    ans1 = input('')
    for s in questions[1]:
        print(s, end='')

login()