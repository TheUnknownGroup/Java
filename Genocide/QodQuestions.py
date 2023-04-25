import time

line = '------'

letters = ['a','A','b','B','c','C','d','D']
yeses = ['yes','Yes','y','sure']
qodQuestions = ['1) During World War I, Russia attacked the region on Turkey\'s northern border. The area was home to millions of Armenians, who were accused by the Turkish leaders of helping the Russians.\n\nHow did Turkish leaders respond to this perceived threat?']
qodAnswers = ['a) They agreed to grant citizenship to all Armenians in exchange for loyalty.','\n','b) They required all Armenians to take a loyalty oath and join the Turkish army.','\n','c) They signed a treaty with Russia that surrendered the region on Turkey\'s northern border.','\n','d)  They forcibly removed Armenians from the area, resulting in the death of about 600,000 Armenians.']

def ask_questions():
    global points
    points = 0
    print(qodQuestions[0])
    for s in qodAnswers:
        print(s, end='')
    an1 = input('\n')
    if an1 in letters:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers}')


def welcome():
    welcome = input('Welcome! Would you like to continue?\n')
    if welcome in yeses:
        print('Alrighty, you\'re now going to continue to the questions area.'); time.sleep(1); print(line); ask_questions()
    else:
        print('Thanks for taking the time to open the quiz.'); time.sleep(1); exit()
welcome()