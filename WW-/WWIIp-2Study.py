import time

line = '------'

questions = ['> 1) Who were the axis powers?',
             '> 2) Who were the allied powers?',
             '> 3) What was fascism?',
             '> 4) What was the Nazi Party?',
             '> 5) What was Totalitarianism?',
             '> 6) What is appeasement?',
             '> 7) What was the Holocaust?',
             '> 8) What is Communism?',
             '> 9) Who was Vladimir Lenin?',
             '> 10) Who was Adolf Hitler?',
             '> 11) Who was Joseph Stalin?',
             '> 12) Who was Benito Mussolini?']
answers = ['']

qodQuestions = ['> 1) During World War I, communists seized power in Russia and created a totalitarian state. How were these developments similar to post-World War I developments in other European nations?',
                '> 2) One impact of the worldwide economic depression that occurred between World War I and World War II was the:',
                '> 3) How did the death and destruction during World War I shape the postwar policies of France, England and the United States as they were confronted with German aggression in the 1930s?',
                '> 4) What did the British and French do at the Munich Conference in 1938 to avoid war?',
                '> 5) Who said this quote: "a date that will live in infamy", and what did it mean?']
qodAnswers = ['a) Nearly all European nations adopted communist forms of government after World War I.','\n','b) Communists also seized power in Great Britain and France after World War I.','\n','c) The formation of the League of Nations can be seen as a similar consolidation of power under one totalitarian governing body.','\n','d) Germany and Italy also embraced totalitarian dictatorships in response to economic, political and social problems arising out of World War I.','a) decline of totalitarian leaders whose militaristic policies led to more costly wars.','\n','b) rise of totalitarian leaders worldwide who promised their citizens a return to stability through strong leadership and militaristic expansion.','\n','c) rise of totalitarian leaders worldwide whose message of isolationism and appeasement indicated a lack of concern for foreign affairs.','\n','d) failure of militaristic states like Germany, Italy and Japan to effectively build and mobilize large standing armies.','a) These leaders were eager to make full use of the wide variety of new, extremely deadly weapons introduced in World War I.','\n','b) These leaders agreed to avoid the use of the wide variety of new, extremely deadly weapons introduced in World War I should fighting start again','\n','c) These leaders were reluctant to enter another major war, so they gave in to many of Hitler\'s demands.','\n','d) These leaders were sure that, should another major war start, this time Germany would be quickly and easily defeated.','a) They persuaded Austria to give in to German occupation.','\n','b) They persuaded Belgium to allow the occupation of Luxembourg.','\n','c) They persuaded the Soviet Union to allow Germany to occupy Poland.','\n','d) They persuaded the Czechs to surrender the Sudetenland','a) Winston Churchill — Requesting U.S. military and economic aid','\n','b) Dwight D. Eisenhower — Announcing the D-Day invasion of France','\n','c) Joseph Stalin — Proclaiming Russia’s decisive victory at Stalingrad','\n','d) Franklin D. Roosevelt — Asking Congress to declare war on Japan']
global points 
points = 0
def ask_questions():
    print(qodQuestions[0])
    for s in qodAnswers[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[6]}\n'); time.sleep(1); print(line)
    print(qodQuestions[1])
    for s in qodAnswers[7:14]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[9]}\n'); time.sleep(1); print(line)
    print(qodQuestions[2])
    for s in qodAnswers[14:21]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[18]}\n'); time.sleep(1); print(line)
    print(qodQuestions[3])
    for s in qodAnswers[21:28]: 
        print(s, end='')
    an1 = input('\n')
    if an1 in ['d','D)']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[27]}\n'); time.sleep(1); print(line)
    print(qodQuestions[4])
    for s in qodAnswers[28:35]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {qodAnswers[34]}\n'); time.sleep(1); print(line)
    
    if points >= 1:
        print(f'You got {points} points!')
    elif points == 1:
        print('You got 1 point')
    elif points <= 1:
        print(f'You got {points} points :( ')
        

welcome = input('Welcome! Would you like to continue?\n')
if welcome in ['yes','Yes','y','sure']:
    print('Alrighty then, lets continue to questions area!'); time.sleep(1); ask_questions()
else:
    print('Thanks for taking the time to open the quiz!'); time.sleep(1); exit()