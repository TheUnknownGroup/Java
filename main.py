import time

welcome = 'Welcome! Would you like to continue?'

line = '------'
question1 = 'What is the element name for Fe?'
question2 = 'What are positive atoms?'
question3 = 'What are negative atoms?'
question4 = 'True or False: Binary is based off of 1s and 0s'

answers1 = 'a'
answers2 = 'c'
answers3 = 'd'
answers4 = 'a'
welcomeYes = 'Yes'

points = 0

print(welcome)
welcome2 = input()
if welcome2 == welcomeYes:
    print('You have picked \'Yes\', you will now go to the questions area.')
    time.sleep(2)
elif welcome2 == 'yes': 
    print('You have picked \'yes\', you will now go to the questions area.')
    time.sleep(2)
else:
    print('You didn\'t pick \'Yes\', thank you for taking the time to go to this test.')
    time.sleep(2)
    exit()
print(question1)
print('a) Iron')
print('b) Copper')
print('c) Oxygen')
print('d) Phosphorus')
answer = input()
if answer == answers1:
    points += 1
    print(f'\nCongrats, You got this correct! You have {points} point(s).')
else:
    print('Whoops, you got this one wrong.')
    print('The correct answer was a) Iron.')
time.sleep(2)
print(line)
print(question2)
print('a) Electrons')
print('b) Nuclei')
print('c) Protons')
print('d) Nucleus')
answer1 = input()
if answer1 == answers2:
    points += 1
    print(f'\nCongrats, You got this correct! You have {points} point(s)')
else:
    print('Whoops, you got this one wrong.')
    print('The correct answer was c) Protons.')
time.sleep(2)
print(line)
print(question3)
print('a) Protons')
print('b) Atoms')
print('c) Nuclei')
print('d) Electrons')
answer2 = input()
if answer2 == answers3:
    points += 1
    print(f'\nCongrats, You got this correct! You have {points} point(s)')
else:
    print('Whoops, you got this one wrong.')
    print('The correct answer was d) Electrons.')
time.sleep(2)
print(line)
print(question4)
print('a) True')
print('b) False')
answer3=input()
if answer3 == answers4:
    points += 1
    print(f'\nCongrats, You got this correct! You have {points} point(s)')
else:
    print('Whoops, you got this one wrong.')
    print('The correct answers was a) True')