import time

points = 0
welcome = 'Welcome! Please give us a series of questions.'
line = '------'
answers = 'Alright, now time for the answers.'
print(welcome)
time.sleep(1)
question1 = input('1. ')
question2 = input('2. ')
question3 = input('3. ')
print(answers)
time.sleep(1)
answers1 = input('1. ')
answers2 = input('2. ')
answers3 = input('3. ')

print('Thank you for the questions! Would you like to continue?')
continueYes = input()
if continueYes == 'Yes':
    print('You have picked \'Yes\'. You will now answer your questions.\n')
    time.sleep(1)
elif continueYes == 'yes':
    print('You have picked \'yes\'. You will now answer your questions.\n')
    time.sleep(1)
else:
    print('You didn\'t pick \'Yes\' or \'yes\'. Thank you for answering our first question.')
    exit()
print('This is the questions area.')
print(line)
print(question1)
answer1 = input()
if answer1 == answers1:
    points += 1
else:
    print('Whoops, you got this wrong.')
print(question2)
answer2 = input()
if answer2 == answers2:
    points += 1
else:
    print('Whoops, you got this wrong.')
print(question3)
answer3 = input()
if answer3 == answers3:
    points += 1
else:
    print('Whoops, you got this wrong.')
print('You are at the end of the questions.')
time.sleep(3)
print(f'You have {points} for points which is: {points} out of 3')
exit()