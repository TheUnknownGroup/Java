import time

questions = ['> 1) What is the War Guilt clause?',
             '> 2) What was Nazism?',
             '> 3) What is Communism?',
             '> 4) Who were the Bolsheviks?',
             '> 5) What was the League of Nations?',
             '> 6) What is Isolationism?',
             '> 7) What is Disarmament?',
             '> 8) What was 14 Points?',
             '> 9) What is Reparations?',
             '> 10) What is the Treaty of Brest-Litovsk?']
answers = ['\'The Allied and Associated Governments affirm, and Germany accepts the responsibility of Germany and her allies for causing all the loss and damage\'',
           'the political principles of the National Socialist German Workers\' Party',
           'economic and political system in which government owns the means of production and controls economic planning',
           'Marxists whose goal was to seize state power and establish a dictatorship of the proletariat; Soviet Communists',
           'an internation body of nations formed after WWI to prevent future wars',
           'staying out of the affairs and wars of other nations; the position intially held by the US at the beginning of WWII',
           'the reduction or withdrawal of military forces and weapons',
           'The Fourteen Points was a statement of principles for peace that was to be used for peace negotiations in order to end World War I.',
           'Germany had to pay over $33 Billion in Reparations or fines.',
           'The Treaty of Brest-Litovsk was a separate peace treaty signed on 3 March 1918 between Russia and the Central Powers, that ended Russia\'s participation in World War I.']

line = '------'
welcome = 'Welcome! Would you like to continue?'
tries = 'Would you like to study more?'

def ask_questions():
    points = 0
    welcomeYes = input(welcome+'\n')
    if welcomeYesNo in ['Yes','yes','y','sure']:
        print('>> You will now go to the questions area since you have picked either \'Yes\' or \'yes\'.')
        time.sleep(1)
        print(line)
    else:
        print('>> You didn\'t pick either \'Yes\' or \'yes\'. Thank you for your time.')
        time.sleep(1)
        exit()
    ans1 = input(str(questions[0]).lstrip('[\'').rstrip('\']')
                +str(answers[6]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[5]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[10]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[0]).lstrip('[\'').rstrip('\']')+'\nd) ')
    if ans1 in ['d','D']:
        points += 1
        print(f'\nCorrect!\n{line}')
        time.sleep(1)
    else:
        print(f'\nWhoops, got that wrong. The Answer was {answers[0]}\n{line}')
        time.sleep(1)
    ans2 = input(str(questions[1]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[9]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[1]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[3]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[5]).lstrip('[\'').rstrip('\']'))
    if ans2 in ['a','A']:
        points += 1
        print(f'\nCorrect!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[1]}\n{line}')
        time.sleep(1)
    ans3 = input(str(questions[2]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[5]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[2]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[3]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[0]).lstrip('[\'').rstrip('\']'))
    if ans3 in ['b','B']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[2]}\n{line}')
        time.sleep(1)
    ans4 = input(str(questions[3]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[7]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[5]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[3]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[8]).lstrip('[\'').rstrip('\']'))
    if ans4 in ['c','C']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The answer was {answers[3]}\n{line}')
        time.sleep(1)
    ans5 = input(str(questions[4]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[6]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[9]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[2]).lstrip('[\'').rstrip('\']'))
    if ans5 in ['b','B']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The answer was {answers[4]}\n{line}')
        time.sleep(1)
    ans6 = input(str(questions[5]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[2]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[7]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[5]).lstrip('[\'').rstrip('\']'))
    if ans6 in ['d','D']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[5]}\n{line}')
        time.sleep(1)
    ans7 = input(str(questions[6]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[6]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[1]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[7]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[2]).lstrip('[\'').rstrip('\']'))
    if ans7 in ['a','A']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[6]}\n{line}')
        time.sleep(1)
    ans8 = input(str(questions[7]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[7]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[1]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[3]).lstrip('[\'').rstrip('\']')+'\nd)'
                +str(answers[9]).lstrip('[\'').rstrip('\']'))
    if ans8 in ['a','A']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[7]}\n{line}')
    ans9 = input(str(questions[8]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[1]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[8]).lstrip('[\'').rstrip('\']')+'\nd)'
                +str(answers[2]).lstrip('[\'').rstrip('\']'))
    if ans9 in ['c','C']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[8]}\n{line}')
    ans10 = input(str(questions[9]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[8]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[2]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[5]).lstrip('[\'').rstrip('\']')+'\nd)'
                +str(answers[9]).lstrip('[\'').rstrip('\']'))
    if ans10 in ['d','D']:
        points += 1
        print(f'Correct!\n{line}')
        time.sleep(1)
    else:
        print(f'Whoops, got that wrong. The Answer was {answers[9]}\n{line}')
    print(f'You have finished this studying session with {points} out of 10')
    if points < 5:
        def retry():
            tries = input('Would you like to retry?\n')
            if tries in ['Yes','yes','y','sure']:
                print('You will now restart the quiz.')
                time.sleep(1)
                ask_questions()
    elif points > 5:
        reYes = input('Since you have gotten more then 5 points')
        if reYes in ['Yes','yes','y','sure']:
            