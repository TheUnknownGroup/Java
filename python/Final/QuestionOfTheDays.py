import time

letters = ['a','A','b','B','c','C','d','D']

line = '------'
yeses = ['yes','Yes','y','sure']

qod = ['> 1) A biography is an example of this type of source?','> 2) A historian is also which of these people?']
qod_a = ['a) First Source','\n','b) Primary Source','\n','c) Secondary Source','\n','d) Third Source',
         'a) Detective','\n','b) ','\n','c) Police Officer','\n','d) ']

global welcome3
welcome3 = 'Welcome! Would you like to continue?'

def ask_questions():
    global points
    points = 0
    print(qod[0])
    for s in qod_a[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters[4:6]:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qod_a[4]}'); time.sleep(1); print(line)
    print(qod[1])
    for s in qod_a[7:14]:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters[2:4]:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qod_a[9]}'); time.sleep(1); print(line)


def try_again():
    times = 1
    welcome(times)


def welcome(times):
    welcome2 = input(f'{welcome3}\n')
    if welcome2 in yeses:
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