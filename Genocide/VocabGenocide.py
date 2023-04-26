import time

line = '------'

letters = ['a','A','b','B','c','C','d','D']
yeses = ['yes','Yes','y','sure','yea','yeah','Yeah','Yea']
questions = ['> 1) ','> 2) ','> 3) ','> 4) ','> 5) ','> 6) ','> 7) ','> 8) ','> 9) ','> 10) ','> 11) ','> 12) ','> 13) ']
answers = ['a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ',
           'a) ','\n','b) ','\n','c) ','\n','d) ']
def ask_questions():
    print(questions[0])
    for s in answers[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters[0:2]:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {answers}\n'); time.sleep(1); print(line)
    print(questions[1])
    for s in answers[7:14]:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {answers}\n'); time.sleep(1); print(line)


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