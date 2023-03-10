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

# Answer Choices
answerChoice = {'1','2','3','4'}
answerChoice1={}
answerChoice2={}
answerChoiceTrue={}

points = 0

print(welcome)
welcome2 = input()
if welcome2 == welcomeYes:
    print('You have picked \'Yes\', you will now go to the questions area.')
    time.sleep(2)
else:
    print('You didn\'t choose yes, you can have a great rest of your day!')
    time.sleep(2)
    exit()
print(question1)
print(answerChoice)
print('b) Copper')
print('c) Oxygen')
print('d) Phosphorus')
answer = input()
if answer == answers1:
    points += 1
    print(f'\nCongrats, You got this correct! You have {points} point(s).')
else:
    print('Whoops, you got this one wrong.')
    print(f'\nThe correct answer was a) Iron.')

print(line)
print(question2)
print('a) Electrons')
print('b) Nuclei')
print('c) Protons')
print('d) Nucleus')
answer1 = input()
if answer == answers2:
    points += 1
    print(f'\nCongrats, You got this correct! You have {points} point(s)')
else:
    print('Whoops, you got this one wrong.')
    print(f'\nThe correct answer was c) Protons.')

print(line)
print(question3)