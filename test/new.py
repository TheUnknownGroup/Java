import time

welcome = '> Welcome! Would you like to continue?'
line = '------'
questions = ['> 1) What is the element name for Fe?',
             '> 2) What are positive atoms?',
             '> 3) What are negative atoms?',
             '> 4) True or False: Binary is based off of 1s and 0s']
answers1 = ['a) Iron','\n','b) Copper','\n','c) Oxygen','\n','d) Phosphorus']
answers2 = ['a) Electrons','\n','b) Nuclei','\n','c) Protons','\n','d) Nucleus']
answers3 = ['a) Protons','\n','b) Atoms','\n','c) Nuclei','\n','d) Electrons']
answers4 = ['a) True','\n','b) False']
tries = '> Would you like to retry?'
study = '> Would you like to continue to study?'
def ask_questions():
    welcomeYes = input(line+'\n'+welcome+'\n')
    if welcomeYes in ['yes','Yes','y','sure']:
        print('>> You will now go to the questions area.')
        time.sleep(1)
    else:
        print('>> Thank you for taking the time to open this test.')
        time.sleep(1)
        exit()
    points = 0
    print(questions[0])
    for i in answers1:
        print(i, end='')
    ans1 = input('\n')
    if ans1 in ['a','A']:
        print(f'\nCorrect!\n{line}'); points+=1
        time.sleep(1)
    else:
        print(f'\nWhoops got that wrong. The answer was {answers1[0]}\n{line}')
        time.sleep(1)
    print(questions[1])
    for s in answers2:
        print(s, end='')
    ans2 = input('\n')
    if ans2 in ['c','C']:
        print(f'\nCorrect!\n{line}'); points+=1
        time.sleep(1)
    else:
        print(f'\nWhoops, got that wrong. The answer was {answers2[4]}\n{line}')
        time.sleep(1)
    print(questions[2])
    for d in answers3:
        print(d, end='')
    ans3 = input('\n')
    if ans3 in ['d','D']:
        print(f'\nCorrect!\n{line}'); points+=1
        time.sleep(1)
    else:
        print(f'\nWhoops, got that wrong. The answer was {answers3[6]}\n{line}')
        time.sleep(1)
    print(questions[3])
    for c in answers4:
        print(c, end='')
    ans4 = input('\n')
    if ans4 in ['a','A']:
        print(f'\nCorrect!\n{line}'); points+=1
        time.sleep(1)
    else:
        print(f'\nWhoops, got that wrong. The answer was {answers4[0]}\n{line}')
        time.sleep(1)
    print(f'>> You have now completed the questions area with {points} points out of 4.\n{line}')
    if points < 2:
        def retrys():
            retry = input(tries+'\n')
            if retry in ['yes','Yes','y','sure']:
                print('>> You will now restart from the beginning.')
                time.sleep(1)
                ask_questions()
            else:
                print('>> Thanks for studying!')
                time.sleep(1)
                exit()
        retrys()
    elif points == 2:
        studys = input(study+'\n')
        if studys in ['yes','Yes','y','sure']:
            print('>> You will now continue studying.')
            time.sleep(1)
            ask_questions()
        else:
            print('>> Thanks for studying!')
            time.sleep(1)
            exit()
    elif points > 2:
        studys = input(study+'\n')
        if studys in ['yes','Yes','y','sure']:
            print('>> You will now continue studying.')
            time.sleep(1)
            ask_questions()
        else:
            print('>> Thanks for studying!')
            time.sleep(1)
            exit()

ask_questions()