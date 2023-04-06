import time

line = '------'

qodQuestions = ['> 1) During World War I, communists seized power in Russia and created a totalitarian state. How were these developments similar to post-World War I developments in other European nations?',
                '> 2) One impact of the worldwide economic depression that occurred between World War I and World War II was the:']
qodAnswers = ['a) Nearly all European nations adopted communist forms of government after World War I.','\n',
              'b) Communists also seized power in Great Britain and France after World War I.','\n',
              'c) The formation of the League of Nations can be seen as a similar consolidation of power under one totalitarian governing body.','\n',
              'd) Germany and Italy also embraced totalitarian dictatorships in response to economic, political and social problems arising out of World War I.']
qodAns1 = ['a) decline of totalitarian leaders whose militaristic policies led to more costly wars.','\n',
           'b) rise of totalitarian leaders worldwide who promised their citizens a return to stability through strong leadership and militaristic expansion.','\n',
           'c) rise of totalitarian leaders worldwide whose message of isolationism and appeasement indicated a lack of concern for foreign affairs.','\n',
           'd) failure of militaristic states like Germany, Italy and Japan to effectively build and mobilize large standing armies.']
def ask_questions():
    points = 0
    print(qodQuestions[0])
    for s in qodAnswers:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[6]}\n'); time.sleep(1); print(line)
    print(f'You have this many points: {points} out of 1')
    print(qodQuestions[1])
    for s in qodAns1:
        print(s, end='')
    an2 = input('\n')
    if an2 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAns1[0]}\n'); time.sleep(1); print(line)
welcome = input('Welcome! Would you like to continue?\n')
if welcome in ['yes','Yes','y','sure']:
    print('Alrighty then, lets continue to questions area!'); time.sleep(1); ask_questions()
else:
    print('Thanks for taking the time to open the quiz!'); time.sleep(1); exit()