import time

line = '------'

qodQuestions = ['> 1) During World War I, communists seized power in Russia and created a totalitarian state. How were these developments similar to post-World War I developments in other European nations?',
                '> 2) One impact of the worldwide economic depression that occurred between World War I and World War II was the:',
                '> 3) How did the death and destruction during World War I shape the postwar policies of France, England and the United States as they were confronted with German aggression in the 1930s?']
qodAnswers = ['a) Nearly all European nations adopted communist forms of government after World War I.','\n','b) Communists also seized power in Great Britain and France after World War I.','\n','c) The formation of the League of Nations can be seen as a similar consolidation of power under one totalitarian governing body.','\n','d) Germany and Italy also embraced totalitarian dictatorships in response to economic, political and social problems arising out of World War I.']
qodAns1 = ['a) decline of totalitarian leaders whose militaristic policies led to more costly wars.','\n','b) rise of totalitarian leaders worldwide who promised their citizens a return to stability through strong leadership and militaristic expansion.','\n','c) rise of totalitarian leaders worldwide whose message of isolationism and appeasement indicated a lack of concern for foreign affairs.','\n','d) failure of militaristic states like Germany, Italy and Japan to effectively build and mobilize large standing armies.']
qodAns2 = ['a) These leaders were eager to make full use of the wide variety of new, extremely deadly weapons introduced in World War I.','\n','b) These leaders agreed to avoid the use of the wide variety of new, extremely deadly weapons introduced in World War I should fighting start again','\n','c) These leaders were reluctant to enter another major war, so they gave in to many of Hitler\'s demands.','\n','d) These leaders were sure that, should another major war start, this time Germany would be quickly and easily defeated.']
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
    print(qodQuestions[1])
    for s in qodAns1:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAns1[0]}\n'); time.sleep(1); print(line)
    print(qodQuestions[2])
    for s in qodAns2:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAns2[2]}\n'); time.sleep(1); print(line)
welcome = input('Welcome! Would you like to continue?\n')
if welcome in ['yes','Yes','y','sure']:
    print('Alrighty then, lets continue to questions area!'); time.sleep(1); ask_questions()
else:
    print('Thanks for taking the time to open the quiz!'); time.sleep(1); exit()