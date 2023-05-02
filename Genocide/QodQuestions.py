import time

line = '------'

letters = ['a','A','b','B','c','C','d','D']
yeses = ['yes','Yes','y','sure']
qodQuestions = ['> 1) During World War I, Russia attacked the region on Turkey\'s northern border. The area was home to millions of Armenians, who were accused by the Turkish leaders of helping the Russians.\n\nHow did Turkish leaders respond to this perceived threat?','> 2) ']
qodAnswers = ['a) They agreed to grant citizenship to all Armenians in exchange for loyalty.','\n','b) They required all Armenians to take a loyalty oath and join the Turkish army.','\n','c) They signed a treaty with Russia that surrendered the region on Turkey\'s northern border.','\n','d)  They forcibly removed Armenians from the area, resulting in the death of about 600,000 Armenians.']

def ask_questions():
    global points
    points = 0
    print(qodQuestions[0])
    for s in qodAnswers[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters[6:8]:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[6]}'); time.sleep(1); print(line)


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