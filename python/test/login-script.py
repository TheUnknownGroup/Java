import time
import webbrowser as web
line = '------'

count1 = 0
count2 = 0

i1 = 1
i2 = 0

questions = ['1) What is your Username?\n',
             '2) What is your Password?\n']
username = 'ddr4lover'
password = 'ddr5lover#5'

welcome = 'Welcome! Please login with the correct credentials.'

def red(ans1, ans2):

    if ans1 == i1:
        count1 += 1
    elif ans1 == i2:
        count2 += 1
    elif ans2 == i1:
        count1 += 1
    elif ans2 == i2:
        count2 += 1
        
    time.sleep(1)
    
    if count1 == 1:
        print('Incorrect password or username. Please try again.'); start()
    elif count1 == 2:
        print('Incorrect password & username. Please Try Again.'); start()
    elif count2 == 2:
        print('Logging in...'); time.sleep(0.5); web.open("https://theunknowngroup.github.io"); exit()


def names(ans1, ans2):
    time.sleep(0.5)
    
    if ans1 == username:
        print(f'Your username {ans1} is correct!'); time.sleep(0.5)
        ans1 = i2
    elif ans1 != username:
        print(f'Your username {ans1} is incorrect.'); time.sleep(0.5)
        ans1 = i1
        
    if ans2 == password:
        print(f'Your password {ans2} is correct!'); time.sleep(0.5)
        ans1 = i2
    elif ans2 != password:
        print(f'Your password {ans2} is incorrect.'); time.sleep(0.5)
        ans1 = i1
    
    red(ans1, ans2); return ans1 and ans2


def login():
    print(welcome); time.sleep(1.25)
    for s in questions[0]:
        print(s, end='')
    ans1 = input('')
    for s in questions[1]:
        print(s, end='')
    ans2 = input(''); time.sleep(1)
    
    names(ans1, ans2); return ans1 and ans2


def start():
    global ans1; global ans2; login()
start()