import time

line = '------'

studyQuestions = ['> 1) What is an algorithm',
                  '> 2) What is a program?',
                  '> 3) What is a programming language?',
                  '> 4) What is a webpage?',
                  '> 5) What is a website?',
                  '> 6) What are mobile applications?',
                  '> 7) What is a front-end language?',
                  '> 8) What is a back-end language?',
                  '> 9) What is binary?',
                  '> 10) What is machine code?',
                  '> 11) What is compiling?',
                  '> 12) What is a bit?',
                  '> 13) What is a byte?',
                  '> 14) What is pseudocode?',
                  '> 15) What is a flowchart?',
                  '> 16) What is computational thinking?',
                  '> 17) What is decomposition (compscience terms)?',
                  '> 18) What is pattern recognition?',
                  '> 19) What is abstraction (compscience terms)?',
                  '> 20) What is algorithm design?']
studyAns = ['a) each letter or number is represented by 1s and 0s','\n','b) 8 bits or digits','\n','c) a list of steps or instructions about how to complete a task','\n','d) the thought process for creating solutions that can be carried out by a computer',
            'a) a way to convert the program code into machine code for the computer to be able to read','\n','b) an algorithm that has been translated into code for a computer','\n','c) plain language description of the steps of an algorithm','\n','d) documents that can be displayed in a web browser',
            'a) identify what different problems have in common','\n','b) creating a solution','\n','c) a combo of numbers, letters, symbols, and formatting to tell a computer what to do','\n','d) binary that is able to be processed and read by the computer',
            'a) documents that can be displayed in a web browser','\n','b) a diagram that outlines the steps in a process','\n','c) (short for binary digit): one digit (either 1 or 0)','\n','d) plain description of the steps of an algorithm',
            'a) programming languages used to organize information and connect it to the front end','\n','b) a way to convert the program code into machine code for the computer to be able to read','\n','c) creating a solution with simple steps','\n','d) a collection of web pages',
            'a) types of software designed to run on mobile applications','\n','b) separating details that matter from details that are not important','\n','c) each letter or number is represented by 1s and 0s','\n','d) an algorithm that has been translated into code for a computer',
            'a) creating a solution','\n','b) programming languages used to make the part of a website that are seen on the screen','\n','c) ','\n','d) ',
            'a) ','\n','b) programming languages used to organize information and connect it to the front end','\n','c) ','\n','d) ',
            'a) each letter or number is represented by 1s and 0s','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) code that can be read and/or displayed by the computer',
            'a) ','\n','b) ','\n','c) a way to convert the program code into machine code for the computer to be able to read','\n','d) ',
            'a) ','\n','b) (short for binary digit): one digit (either 1 or 0)','\n','c) ','\n','d) ',
            'a) 8 bits or digits','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) plain description of the steps of an algorithm',
            'a) ','\n','b) ','\n','c) a diagram that displays the steps of a process','\n','d) ',
            'a) ','\n','b) the thought process for creating solutions that can be carried out by a computer','\n','c) ','\n','d) ',
            'a) breaking a problem down into simple parts','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) identify what problems have in common','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) separating details that matter from details that are not important',
            'a) ','\n','b) creating a solution with simple steps','\n','c) ','\n','d) ']
global points
points = 0
def ask_questions():
    print(studyQuestions[0])
    for s in studyAns[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[4]}\n'); time.sleep(1); print(line)
    print(studyQuestions[1])
    for s in studyAns[7:14]:
        print(s, end='')
    an2 = input('\n')
    if an2 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[9]}\n'); time.sleep(1); print(line)
    print(studyQuestions[2])
    for s in studyAns[14:21]:
        print(s, end='')
    an3 = input('\n')
    if an3 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[18]}\n'); time.sleep(1); print(line)
    print(studyQuestions[3])
    for s in studyAns[21:28]:
        print(s, end='')
    an4 = input('\n')
    if an4 in ['a','A']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[21]}\n'); time.sleep(1); print(line)
    print(studyQuestions[4])
    for s in studyAns[28:35]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[34]}\n'); time.sleep(1); print(line)
    print(studyQuestions[5])
    for s in studyAns[35:42]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['a','A']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[35]}\n'); time.sleep(1); print(line)
    print(studyQuestions[6])
    for s in studyAns[42:49]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[44]}\n'); time.sleep(1); print(line)
    print(studyQuestions[7])
    for s in studyAns[49:56]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[51]}\n'); time.sleep(1); print(line)
    print(studyQuestions[8])
    for s in studyAns[56:63]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['a','A']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[56]}\n'); time.sleep(1); print(line)
    print(studyQuestions[9])
    for s in studyAns[63:70]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[69]}\n'); time.sleep(1); print(line)
    print(studyQuestions[10])
    for s in studyAns[70:77]:
     print(s, end='')
    an5 = input('\n')
    if an5 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[74]}\n'); time.sleep(1); print(line)
    print(studyQuestions[11])
    for s in studyAns[77:84]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[79]}\n'); time.sleep(1); print(line)
    print(studyQuestions[12])
    for s in studyAns[84:91]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['a','A']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[84]}\n'); time.sleep(1); print(line)
    print(studyQuestions[13])
    for s in studyAns[91:98]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[97]}\n'); time.sleep(1); print(line)
    print(studyQuestions[14])
    for s in studyAns[98:105]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[102]}\n'); time.sleep(1); print(line)
    print(studyQuestions[15])
    for s in studyAns[105:112]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[107]}\n'); time.sleep(1); print(line)
    print(studyQuestions[16])
    for s in studyAns[112:119]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['a','A']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[112]}\n'); time.sleep(1); print(line)
    print(studyQuestions[17])
    for s in studyAns[119:126]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
         print(f'Whoops, got that wrong. The answer was {studyAns[123]}\n'); time.sleep(1); print(line)
    print(studyQuestions[18])
    for s in studyAns[126:133]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['d','D']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[132]}\n'); time.sleep(1); print(line)
    print(studyQuestions[19])
    for s in studyAns[133:140]:
        print(s, end='')
    an5 = input('\n')
    if an5 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[135]}\n'); time.sleep(1); print(line)
    print(f'You have this many points: {points} out of 20')
    if points < 10:
        trys = input('Would you like to retry?\n')
        if trys in ['yes','Yes','y','sure']:
            print('Then, lets get retrying!'); time.sleep(2); print(''); welcome()
        else:
            print('Well, you got a good amount of points, yes. But I think you can do better!'); time.sleep(1); exit()
    elif points == 10:
            print(f'YAY! You got 10 out of 20!! You made it past the underachievers.')
            trys = input('Would you like to continue studying?\n')
            if trys in ['yes','Yes','y','sure']:
                print('Then, lets get studying!'); time.sleep(2); print(''); welcome()
            else:
                print('Well, you got a great amount of points, yes. But I think that doing some more could do you good.'); time.sleep(1); exit()
    elif points > 10:
        print(f'YAY! You got {points} out of 20!! You made it past the underachievers.')
        trys = input('Would you like to continue studying?\n')
        if trys in ['yes','Yes','y','sure']:
            print('Then, lets get studying!'); time.sleep(2); print(''); welcome()
        else:
            print('Well, you got a great amount of points, yes. But I think that doing some more could do you good.'); time.sleep(1); exit()


def welcome():
        welcome = input('Welcome! Would you like to continue?\n')
        if welcome in ['yes','Yes','y','sure']:
            print('Alrighty, you\'re now going to continue to the questions area.'); time.sleep(1); print(line); ask_questions()
        else:
            print('Thanks for taking the time to open the quiz.'); time.sleep(1); exit()
welcome()