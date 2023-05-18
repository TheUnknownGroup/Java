import time

letters = ['']

line = '------'
yeses = ['yes','Yes','y','sure']

qod = ['']
qod_a = ['']

welcome = 'Welcome! Would you like to continue?'

def ask_questions():
    global points
    points = 0
    print(qod[0])
    for s in qod_a:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qod_a}'); time.sleep(1); print(line)


def try_again():
    times = 1
    welcome(times)


def welcome(times):
    welcome = input('Welcome! Would you like to continue?\n')
    if welcome in yeses:
        print('Alrighty, then lets get started!'); times = 1; time.sleep(1); print(line); ask_questions()
    else:
        while times != 1:
            print('Please put words like: yes, Yes, y, sure'); time.sleep(1); print(line); try_again()
            times += 1
            if times == 1:
                print('I\'m guessing you really were trying to get out huh?\nWell I guess theres nothing I can do about that.'); time.sleep(1); exit()
                break
            else:
                continue


def start():
    global times
    times = 0; welcome(times); return times
start()