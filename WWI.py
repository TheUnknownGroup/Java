# WWI Post Test
import time
import random

welcome = 'This is the WWI Post Test - Study Guide'
questions = 'You will now go to the questions area.'
question1 = 'The definition of Militarism.'
question2 = 'The definition of Alliances'
question3 = 'The definition of Imperialism'
question4 = 'The definition of Nationalism'
points = 0

print(welcome)
print(questions)
time.sleep(1)
print(question1+'\na) European countries had undertaken a massive military buildup. This militarism was caused mostly by the desire to protect overseas colonies from other nations.\nb) a formal agreement between two or more nations entered into to advance common interests or causes\nc) The quest to build empires in the late 1800s and early 1900s had created much rivalry and ill will among the nations of Europe.\nd) sense of pride and devotion to one\'s nation')
answer1 = input()
if answer1 == 'a':
    points += 1
    print('Correct')
    time.sleep(1)
else:
    print('Wrong')
print(question2+'\na) European countries had undertaken a massive military buildup. This militarism was caused mostly by the desire to protect overseas colonies from other nations.\nb) a formal agreement between two or more nations entered into to advance common interests or causes\nc) The quest to build empires in the late 1800s and early 1900s had created much rivalry and ill will among the nations of Europe.\nd) sense of pride and devotion to one\'s nation')
answer2 = input()
if answer2 == 'b':
    points += 1
    print('Correct')
    time.sleep(1)
else:
    print('Wrong')
print(question3+'\na) European countries had undertaken a massive military buildup. This militarism was caused mostly by the desire to protect overseas colonies from other nations.\nb) a formal agreement between two or more nations entered into to advance common interests or causes\nc) The quest to build empires in the late 1800s and early 1900s had created much rivalry and ill will among the nations of Europe.\nd) sense of pride and devotion to one\'s nation')
answer3 = input()
if answer3 == 'c':
    points += 1
    print('Correct')
    time.sleep(1)
else:
    print('Wrong')
print(question4+'\na) European countries had undertaken a massive military buildup. This militarism was caused mostly by the desire to protect overseas colonies from other nations.\nb) a formal agreement between two or more nations entered into to advance common interests or causes\nc) The quest to build empires in the late 1800s and early 1900s had created much rivalry and ill will among the nations of Europe.\nd) sense of pride and devotion to one\'s nation')
answer4 = input()
if answer4 == 'd':
    points += 1
    print('Correct')
    time.sleep(1)
else:
    print('Wrong')


