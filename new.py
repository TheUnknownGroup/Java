import time

line = '------'

start = 'Welcome, choose the following:'

list = ['-a', '-b', '-c', '-d', '-e']


def new2():
    inp = input(f'{line}\nYour choice: ')
    thanks = f'Thanks for choosing {inp}'
    if inp is ['a', 'b', 'c', 'd', 'e']:
        print(thanks)
    elif inp not in ['a', 'b', 'c', 'd', 'e']:
        print('Please choose: a, b, c, d, e'); time.sleep(1); new()


def new():
    print(start + '\n'+ line); time.sleep(0.35)
    for s in list:
        print(s, end='' + '\n')
    new2()
new()