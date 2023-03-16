# WWI Post Test - Study Guide

import time
import sys
import subprocess
import os

welcome = 'Welcome! Would you like to continue?'
finshedDefinitions = 'Now that you\'ve finished the defintion questions, we can move onto the QOD Questions for WWI.'
line = '------'
points = 0
reRetry = 'Would you like to retry to study more?'

questions = ['The definition of Militarism: ',
             'The definition of Alliance: ',
             'The definition of Imperialism: ',
             'The definition of Nationalism: ',
             'The definition of machine gun: ',
             'The definition of poison gas: ',
             'The definition of tanks: ',
             'The definition of U-Boat: ',
             'The definition of trench warfare: ',
             'The definition of Allied Powers: ',
             'The definition of Central Powers: ',
             'The definition of Lusitania: ',
             'The definition of Zimmerman Note: ',
             'The definition of Triple Alliance: ',
             'The definition of Triple Entente: ',
             'The definition of Treaty of Versailles: ',
             'The definition of Stalemate: ']
answers = ['European countries had undertaken a massive military buildup. This __________ was caused mostly by the desire to protect overseas colonies from other nations.',
           'a formal agreement between two or more nations entered into, to advance common interests or causes',
           'The act of taking over a smaller/weaker nation as a bigger/stronger nation, for political, economic, and social reasons.',
           'sense of pride and devotion to one\'s nation',
           'Other new weapons were far more effective. For example, rapid fire _______ ____ came into wide use during the war.',
           '______ ___ was one of the new weapons used in the war. Different types of ___ could blind, choke, or burn the victims.',
           '_____, armored vehicles that could cross rough battlefield terrain, were pioneered by the British.',
           '__________ used by Germans in WWI and II',
           'a form of combat in which soldiers dug ________, or deep ditches, to seek protection from enemy fire and to defend their positions',
           'the alliance formed between Britain, France, and Russia during WWI',
           'the alliance between Germany, Austria-Hungary, and the Ottoman Empire during WWI',
           'A passenger ship that sunk under the German policy of unrestricted warfare, killing some 1,200 people, including over 120 Americans.',
           'This was a secret message from German diplomat Arthur _________ to officials in Mexico in which Germany proposed that Mexico attack the United States.',
           'an alliance between Germany, Austria-Hungary, and Italy in the late 1800s',
           'an alliance between France, Russia, and Great Britain in the late 1800s',
           'a ______ that ended WWI and Germany had to pay +2 Billion for war damages to United states and others.',
           'a state where both sides are so evenly balanced that neither can breakthrough against the enemy.']

qodQuestions = ['Why were the Balkans considered a powder keg in the early 1900s?',
          'Which statement best describes Europe just before WWI?',
          'Just prior to WWI, the nations of Europe believed that the balance of power could best be maintained by',
          'What led to the assassination of Archduke Francis Ferdinand by a Serbia terrorist and started WWI?',
          '\'An ecstacy of fumbling, Fitting the clumsy helmet just in time; But someone still was yelling and stumbling and flound\'ring like a man in fire or in lime... Dim, through the misty panes and thick green light, As under a green sea, I saw him drowning.\'\nThe new technological advancement from WWI that Wilfred Owen is alluding to in his poem, "Dulce Et Decorum Est" is',
          'Which is an accurate statement based on the information in the graph?',
          'Which WWI military tactic resulted in a prolonged stalemate?',
          'What finally brought the United States into WWI, ending its policy of neutrality?']
qodAnswers1= ['The Ottoman Empire engaged in a war for control of the region.',
          'The competing interests of nationalist groups and foreign countries destabilized the region.',
          'The countries of the region sought to establish their own colonial empires.',
          'Religious differences led to conflicts within the newly independent nations.']
qodAnswers2= ['The formation of opposing alliance systems increased international distrust.',
          'European leaders resorted to a policy of appeasement to solve international disputes.',
          'The communist nations promoted violent revolution throughout Western Europe',
          'The isolationist policies of England and France prevented their entry into the hostilities']
qodAnswers3=['open agreements, openly arrived at.',
          'an international court',
          'increases in tariff barriers.',
          'a system of alliances.']
qodAnswers4=['A militant Serbian faction viewed Russia as a major political threat.',
          'The Seribans viewed the Austrians as foreign oppressors.',
          'Serbian nationalists were planning to join Russia.',
          'Germany saw the Archduke\'s planned visit as an outright declaration of war.']
qodAnswers5=['Poison gas',
          'The machine gun',
          'Trench warfare',
          'The airplane']
qodAnswers6=['In 1914, the five major European powers shown spent more on military programs than on any other program.',
          'In 1914, Austria-Hungary attempted to end the arms race in Europe.',
          'In 1914, Russia was the most militaristic of all the European nations shown.',
          'In 1914, Germany spent more money on its military than did the other European nations shown.']
qodAnswers7=['aerial bombardment',
          'submarine attacks',
          'tank fighting',
          'trench warfare']
qodAnswers8=['US investment in Allied nations, which amounted to $2 billion, and which would be lost if the Central Powers won the war.',
          'the German attack on the British passenger liner Lusitania, in which 128 Americans were killed',
          'the German attack on the French passenger ship Sussex, in which four Americans were killed',
          'discovery of the Zimmerman Note, in which Germany promised to give Mexico parts of the US if Mexico allied itself with Germany']

welcomeYes = input(welcome+'\n')
if welcomeYes == 'Yes' or 'yes':
    print('You have picked \'Yes\' or \'yes\', you will now go to the questions area.')
    time.sleep(1)
    print(line)
else:
    print('You didn\' pick \'Yes\' or \'yes\'. Thank you for your time.')
    exit()
print(str(questions[0]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[9]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[0]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[5]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[7]).lstrip('[\'').rstrip('\']'))
answer1 = input()
if answer1 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[1]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[1]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[2]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[9]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[15]).lstrip('[\'').rstrip('\']'))
answer2 = input()
if answer2 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[2]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[7]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[10]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[3]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[2]).lstrip('[\'').rstrip('\']'))
answer3 = input()
if answer3 == 'd':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[3]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[11]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[3]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[5]).lstrip('[\'').rstrip('\']'))
answer4 = input()
if answer4 == 'c':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[4]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[4]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[5]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[12]).lstrip('[\'').rstrip('\']'))
answer5 = input()
if answer5 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[5]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[15]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[0]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[5]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[2]).lstrip('[\'').rstrip('\']'))
answer6 = input()
if answer6 == 'c':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[6]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[13]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[6]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[9]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[15]).lstrip('[\'').rstrip('\']'))
answer7 = input()
if answer7 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[7]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[7]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[10]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[3]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[2]).lstrip('[\'').rstrip('\']'))
answer8 = input()
if answer8 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[8]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[14]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[7]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[12]).lstrip('[\'').rstrip('\']'))
answer9 = input()
if answer9 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[9]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[4]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[10]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[9]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[3]).lstrip('[\'').rstrip('\']'))
answer10 = input()
if answer10 == 'c':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[10]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[10]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[5]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[6]).lstrip('[\'').rstrip('\']'))
answer11 = input()
if answer11 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[11]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[11]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[4]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[5]).lstrip('[\'').rstrip('\']'))
answer12 = input()
if answer12 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[12]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[1]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[2]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[7]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[12]).lstrip('[\'').rstrip('\']'))
answer13 = input()
if answer13 == 'd':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[13]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[7]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[13]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[3]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[2]).lstrip('[\'').rstrip('\']'))
answer14 = input()
if answer14 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[14]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[4]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[14]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[4]).lstrip('[\'').rstrip('\']'))
answer15 = input()
if answer15 == 'c':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[15]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[15]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[8]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[5]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[8]).lstrip('[\'').rstrip('\']'))
answer16 = input()
if answer16 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(questions[16]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(answers[4]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(answers[16]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(answers[5]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(answers[9]).lstrip('[\'').rstrip('\']'))
answer17 = input()
if answer17 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(finshedDefinitions)
time.sleep(1)
print(str(qodQuestions[0]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers1[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers1[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers1[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers1[3]).lstrip('[\'').rstrip('\']'))
qodAnswer1 = input()
if qodAnswer1 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[1]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers2[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers2[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers2[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers2[3]).lstrip('[\'').rstrip('\']'))
qodAnswer2 = input()
if qodAnswer2 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[2]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers3[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers3[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers3[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers3[3]).lstrip('[\'').rstrip('\']'))
qodAnswer3 = input()
if qodAnswer3 == 'c':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[3]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers4[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers4[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers4[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers4[3]).lstrip('[\'').rstrip('\']'))
qodAnswer4 = input()
if qodAnswer4 == 'b':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[4]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers5[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers5[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers5[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers5[3]).lstrip('[\'').rstrip('\']'))
qodAnswer5 = input()
if qodAnswer5 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[5]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers6[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers6[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers6[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers6[3]).lstrip('[\'').rstrip('\']'))
qodAnswer6 = input()
if qodAnswer6 == 'd':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[6]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers7[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers7[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers7[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers7[3]).lstrip('[\'').rstrip('\']'))
qodAnswer7 = input()
if qodAnswer7 == 'd':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(str(qodQuestions[7]).lstrip('[\'').rstrip('\']')+'\n'+'a) '+str(qodAnswers8[0]).lstrip('[\'').rstrip('\']')+'\n'+'b) '+str(qodAnswers8[1]).lstrip('[\'').rstrip('\']')+'\n'+'c) '+str(qodAnswers8[2]).lstrip('[\'').rstrip('\']')+'\n'+'d) '+str(qodAnswers8[3]).lstrip('[\'').rstrip('\']'))
qodAnswer8 = input()
if qodAnswer8 == 'a':
    points += 1
    print('')
    print('Correct!')
    print(line)
else:
    print('Whoops, got that wrong.')
    print(line)
print(f'You have: {points} out of 25')
retry = input(reRetry)
if retry == 'Yes' or 'yes':
    print('You will now restart since you have picked \'Yes\' or \'yes\'.')
    time.sleep(1)
    subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
else:
    print('Thank you for answering the study guide.')
    exit()