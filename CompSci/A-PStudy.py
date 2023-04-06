import time

line = '------'

studyQuestions = ['> 1) What is a program?',
                  '> 2) What is a programming language?',
                  '> 3) What is a webpage?',
                  '> 4) What is a website?',
                  '> 5) What are mobile applications?',
                  '> 6) What is a front-end language?',
                  '> 7) What is a back-end language?',
                  '> 8) What is binary?',
                  '> 9) What is machine code?',
                  '> 10) What is compiling?',
                  '> 11) What is a bit?',
                  '> 12) What is a byte?',
                  '> 13) What is pseudocode?',
                  '> 14) What is a flowchart?',
                  '> 15) What is computational thinking?',
                  '> 16) What is decomposition (compscience terms)?',
                  '> 17) What is pattern recognition?',
                  '> 18) What is abstraction (compscience terms)?',
                  '> 19) What is algorithm design?']
studyAns = ['a) a way to convert the program code into machine code for the computer to be able to read','\n','b) an algorithm that has been translated into code for a computer','\n','c) plain language description of the steps of an algorithm','\n','d) documents that can be displayed in a web browser',
            'a) identify what different problems have in common','\n','b) creating a solution','\n','c) a combo of numbers, letters, symbols, and formatting to tell a computer what to do','\n','d) binary that is able to be processed and read by the computer',
            'a) documents that can be displayed in a web browser','\n','b) a diagram that outlines the steps in a process','\n','c) (short for binary digit): one digit (either 1 or 0)','\n','d) ',
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
            'a) ','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) ',
            'a) ','\n','b) ','\n','c) ','\n','d) ']
ranges = ['7:14','14:21','21:28','28:35','35:42','42:49','49:56','56:63','63:70','70:77','77:84','84:91','91:98','98:105','105:112','112:119','119:126','126:133']

def ask_questions():
    points = 0
    print(studyQuestions[0])
    for s in studyAns[0:7]:
        print(s, end='')
    an1 = input('\n')
    if an1 in ['b','B']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[2]}'); time.sleep(1); print(line)
    print(studyQuestions[1])
    for s in studyAns[7:14]:
        print(s, end='')
    an2 = input('\n')
    if an2 in ['c','C']:
        print('Correct!\n'); time.sleep(1); print(line); points += 1
    else:
        print(f'Whoops, got that wrong. The answer was {studyAns[11]}'); time.sleep(1); print(line)
welcome = input('Welcome! Would you like to continue?\n')
if welcome in ['yes','Yes','y','sure']:
    print('Alrighty, you\'re now going to continue to the questions area.'); time.sleep(1); print(line); ask_questions()