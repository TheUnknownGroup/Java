# WWII Vocab
import time

questions = ['> 1) The defintion of Axis Powers: ',
             '> 2) The defintion of Allied Powers: ',
             '> 3) The defintion of Facism: ',
             '> 4) The defintion of Nazi Party: ',
             '> 5) The defintion of Totalitarianism: ',
             '> 6) The defintion of Appeasement: ',
             '> 7) The defintion of Nationalism: ',
             '> 8) The defintion of Communism: ',
             '> 9) The defintion of Bolsheviks: ',
             '> 10) The defintion of Vladimir Lenin: ',
             '> 11) The defintion of Refute: ',
             '> 12) The defintion of Opposition: ',
             '> 13) The defintion of Socialism: ',
             '> 14) The defintion of Vengence: ',
             '> 15) The defintion of Adolf Hitler: ',
             '> 16) The defintion of Woodrow Wilson: ',
             '> 17) The defintion of League of Nations: ',
             '> 18) The defintion of Isolationism: ',
             '> 19) The defintion of Treaty Of Versailles: ',
             '> 20) The defintion of Joseph Stalin: ',
             '> 21) The defintion of Winston Churchill: ']
definitions = ['the alliance of Germany, Italy, and Japan in WWII',
               'the alliance formed between Britain, France, and Russia during WWI',
               'a totalitarian system of government that focuses on the good of the state rather than on the good of the indiviual citizens',
               'National Socialist Party; facist political part of Adolf Hitler governed on totalitarian lines and advocating German racial superiority',
               'form of government in which the person or party in charge has absolute control over all aspects of life',
               'giving in to agressive demands in order to avoid war',
               'sense of pride and devotion to one\'s nation',
               'economic and political system in which government owns the means of production and controls economic planning',
               'Marxists whose goal was to seize state power and establish a dictatorship of the proletariat; Soviet Communists',
               'Russian revolutionary and found of Bolshevism; he rose to power in Russia following the Russian Revolution in 1917',
               'to prove wrong by argument or evidence : show to be false or erroneous',
               'an act of setting opposite or over against : the condition of being so set',
               'a political and economic system in which society, usually in the form of the government, owns the means of production',
               'punishment inflicted in retaliation for an injury or offense : Retribution',
               'Totalitarian dictator of Germany; his invasion of European countries led to WWI. He espoused notions of racial superiority and was responsible '
               'for the mass murder of millions of Jews and others in the Holocaust',
               'Twenty-eighth president of the United States; he proposed the League of Nations after WWI as a part of his Fourteen Points',
               'an internation body of nations formed after WWI to prevent future wars',
               'staying out of the affairs and wars of other nations; the position intially held by the US at the beginning of WWII',
               'treaty ending WWI; required Germany to pay huge war reparations and establish the League of Nations',
               'Totalitarian dictator of the Soviet Union through WWII and created a powerful Soviet sphere of influence in Eastern Europe after the war',
               'British prime minister; he opposed the polciy of appeasement and led Great Britian through WWII']
qodQuestions = ['> 1) Which factor contributed most to the success of the Bolshevik Revolution of 1917 in Russia?']
qodAnswers1 = ['a) The Russian people were discouraged with their losses in WWI.',
              'b) The Allied powers favored the revolution.',
              'c) The Czar was willing to abdicate.',
              'd) The appeal of Marxism to the Russian nobility.']

line = '------'
welcome = '> Welcome! Would you like to continue?'
tries = 'Would you like to retry to study more?'

def ask_questions():
    points = 0
    welcomeYesNo = input(welcome+'\n')
    if welcomeYesNo in ['Yes','yes','y','sure']:
        print('>> You will now go to the questions area since you have picked either \'Yes\' or \'yes\'.')
        time.sleep(1)
        print(line)
    else:
        print('>> You didn\'t pick either \'Yes\' or \'yes\'. Thank you for your time.')
        time.sleep(1)
        exit()
    ans1 = input(str(questions[0]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[5]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[2]).lstrip('[\'').rstrip('\']')+'\n')
    if ans1 == 'b':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was b) {definitions[0]}')
        time.sleep(1)
        print(line)
    ans2 = input(str(questions[1]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[5]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[6]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[1]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[20]).lstrip('[\'').rstrip('\']')+'\n')
    if ans2 == 'c':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was c) {definitions[1]}')
        time.sleep(1)
        print(line)
    ans3 = input(str(questions[2]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[6]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[7]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[2]).lstrip('[\'').rstrip('\']')+'\n')
    if ans3 == 'd':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was d) {definitions[2]}')
        time.sleep(1)
        print(line)
    ans4 = input(str(questions[3]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[3]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[9]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\n')
    if ans4 == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was a) {definitions[3]}')
        time.sleep(1)
        print(line)  
    ans5 = input(str(questions[4]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[11]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[8]).lstrip('[\'').rstrip('\']')+'\n')
    if ans5 == 'c':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\n\nWhoops, got that wrong. The Answer was c) {definitions[4]}')
        time.sleep(1)
        print(line)  
    ans6 = input(str(questions[5]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[17]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[5]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[20]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[2]).lstrip('[\'').rstrip('\']')+'\n')
    if ans6 == 'b':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was b) {definitions[5]}')
        time.sleep(1)
        print(line)  
    ans7 = input(str(questions[6]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[9]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[7]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[6]).lstrip('[\'').rstrip('\']')+'\n')
    if ans7 == 'd':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was d) {definitions[6]}')
        time.sleep(1)
        print(line)  
    ans8 = input(str(questions[7]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[7]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[18]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[19]).lstrip('[\'').rstrip('\']')+'\n')
    if ans8 == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was a) {definitions[7]}')
        time.sleep(1)
        print(line)  
    ans9 = input(str(questions[8]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[3]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[8]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[14]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[10]).lstrip('[\'').rstrip('\']')+'\n')
    if ans9 == 'b':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was b) {definitions[8]}')
        time.sleep(1)
        print(line)  
    ans10 = input(str(questions[9]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[9]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[1]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[14]).lstrip('[\'').rstrip('\']')+'\n')
    if ans10 == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was a) {definitions[9]}')
        time.sleep(1)
        print(line)  
    ans11 = input(str(questions[10]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[20]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[13]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[10]).lstrip('[\'').rstrip('\']')+'\n')
    if ans11 == 'd':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was d) {definitions[10]}')
        time.sleep(1)
        print(line)  
    ans12 = input(str(questions[11]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[11]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[9]).lstrip('[\'').rstrip('\']')+'\n')
    if ans12 == 'c':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was c) {definitions[11]}')
        time.sleep(1)
        print(line)  
    ans13 = input(str(questions[12]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[6]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[19]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\n')
    if ans13 == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was a) {definitions[12]}')
        time.sleep(1)
        print(line)  
    ans14 = input(str(questions[13]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[13]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[8]).lstrip('[\'').rstrip('\']')+'\n')
    if ans14 == 'c':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was c) {definitions[13]}')
        time.sleep(1)
        print(line)  
    ans15 = input(str(questions[14]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[5]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[14]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[6]).lstrip('[\'').rstrip('\']')+'\n')
    if ans15 == 'b':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was b) {definitions[14]}')
        time.sleep(1)
        print(line)  
    ans16 = input(str(questions[15]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[8]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[3]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\n')
    if ans16 == 'd':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was d) {definitions[15]}')
        time.sleep(1)
        print(line)  
    ans17 = input(str(questions[16]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[5]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[16]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[12]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\n')
    if ans17 == 'b':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was b) {definitions[16]}')
        time.sleep(1)
        print(line)  
    ans18 = input(str(questions[17]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[17]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[2]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[7]).lstrip('[\'').rstrip('\']')+'\n')
    if ans18 == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was a) {definitions[17]}')
        time.sleep(1)
        print(line)  
    ans19 = input(str(questions[18]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[18]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[10]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[2]).lstrip('[\'').rstrip('\']')+'\n')
    if ans19 == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was a) {definitions[18]}')
        time.sleep(1)
        print(line)  
    ans20 = input(str(questions[19]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[3]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[19]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[0]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[11]).lstrip('[\'').rstrip('\']')+'\n')
    if ans20 == 'b':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was b) {definitions[19]}')
        time.sleep(1)
        print(line)
    ans21 = input(str(questions[20]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(definitions[6]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(definitions[15]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(definitions[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(definitions[20]).lstrip('[\'').rstrip('\']')+'\n')
    if ans21 == 'd':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was d) {definitions[20]}')
        time.sleep(1)
        print(line)
    print(f'Since you have finished the definitions portion with {points} points, you will now continue to '
          'the QOD Questions. Loading may take a moment')
    time.sleep(5)
    ansQod = input(str(qodQuestions[0]).lstrip('[\'').rstrip('\']')+'\n'
                 +str(qodAnswers1[0]).lstrip('[\'').rstrip('\']')+'\n'
                 +str(qodAnswers1[1]).lstrip('[\'').rstrip('\']')+'\n'
                 +str(qodAnswers1[2]).lstrip('[\'').rstrip('\']')+'\n'
                 +str(qodAnswers1[3]).lstrip('[\'').rstrip('\']')+'\n')
    if ansQod == 'a':
        points += 1
        print('\nCorrect!')
        time.sleep(1)
        print(line)
    else:
        print(f'\nWhoops, got that wrong. The Answer was {qodAnswers1[0]}')
        time.sleep(1)
        print(line)
    print(f'You have: {points} out of 21')
    if points < 10:
        def retrys():
            retry = input('Would you like to retry?\n')
            if retry in ['Yes','yes','y','sure']:
                print('You will now restart at the beginning.')
                time.sleep(1)
                while points < 10:
                    ask_questions()
                    break
            else:
                print('Thanks for studying.')
                exit()
        retrys()
    elif points > 10:
        study = input('Would you like to continue studying?\n')
        if study in ['Yes','yes','y','sure']:
            print('You are now going to continue studying!')
            time.sleep(1)
            ask_questions()
        else:
            print('Thanks for studying!')
            exit()

ask_questions()