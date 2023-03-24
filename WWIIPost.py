import time

questions = ['> 1) What was the Axis Powers?',
             '> 2) What was the Allied Powers?',
             '> 3) What was the War Guilt clause?',
             '> 4) What was Nazism?'
             '> 5) What is Facism?',
             '> 6) What is the Nazi Party?',
             '> 7) What is Totalitarianism?',
             '> 8) What is Appeasement?',
             '> 9) What is Nationalism?',
             '> 10) What is Communism?',
             '> 11) Who were Bolsheviks?',
             '> 12) Who was Vladimir Lenin?',
             '> 13) What is Refute?',
             '> 14) What is Opposition?',
             '> 15) What is Socialism?',
             '> 16) What is Vengence?',
             '> 17) Who was Adolf Hitler?',
             '> 18) Who was Woodrow Wilson?',
             '> 19) What was the League of Nations?',
             '> 20) What is Isolationism?',
             '> 21) What is the Treaty Of Versailles?',
             '> 22) Who was Joseph Stalin?',
             '> 23) Who was Winston Churchill?',
             '> 24) What is Disarmament?',
             '> 25) What were the 14 Points (Created by Woodrow Wilson for the \'peace without victory\')?',
             '> 26) What is Reparations?',
             '> 27) What is the Treaty of Brest-Litovsk?']
answers = ['the alliance of Germany, Italy, and Japan in WWII',
           'the alliance formed between Britian, France, and Russia during WWI',
           '\'The Allied and Associated Governments affirm, and Germany accepts the responsibility of Germany and her allies for causing all the loss and damage\'',
           'the political principles of the National Socialist German Workers\' Party',
           'a totalitarian system of government that focuses on the good of the state rather than on the good of the individual citizens',
           'National Socialist Party; facist political part of Adolf Hitler governed on totalitarisn lines and advocating German racial superiority',
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
           'British prime minister; he opposed the polciy of appeasement and led Great Britian through WWII',
           'the reduction or withdrawal of military forces and weapons',
           'The Fourteen Points was a statement of principles for peace that was to be used for peace negotiations in order to end World War I.',
           'Germany had to pay over $33 Billion in Reparations or fines.',
           'The Treaty of Brest-Litovsk was a separate peace treaty signed on 3 March 1918 between Russia and the Central Powers, that ended Russia\'s participation in World War I.']
qodQuestions = ['> 1) Which factor contributed most to the success of the Bolshevik Revolution of 1917 in Russia?',
                '> 2) What treaty forced Germny to accept blame for WWI?',
                '> 3) Which part of the Treaty of Versailles was was most damaging to the German economy?',
                '> 4) Which major nation did not join the League of Nations?']
qodAnswers1 = ['a) The Russian people were discouraged with their losses in WWI.',
              'b) The Allied powers favored the revolution.',
              'c) The Czar was willing to abdicate.',
              'd) The appeal of Marxism to the Russian nobility.']
qodAnswers2 = ['a) Treaty of London',
               'b) Treaty of Munich',
               'c) Treaty of Versailles',
               'd) Treaty of Rome']
qodAnswers3 = ['a) Germany lost its colonies',
               'b) the German emporer was to be put on trial',
               'c) the Germans had to pay the Allies large sums of money',
               'd) Germans were not allowed to have a large army and navy']
qodAnswers4 = ['a) France',
               'b) Britain',
               'c) Italy',
               'd) US']

line = '------'
welcome = '> Welcome! Would you like to continue?'
tries = 'Would you like to retry to study more?'

def ask_questions():
    welcomeYes = input(welcome+'\n')
    if welcomeYes in ['Yes','yes','y','sure']:
        print(f'>> You will now go to the questions area.\n{line}')
        time.sleep(1)
    else:
        print('Thanks for using your time to open this.')
        time.sleep(1)
        exit()
    ans1 = input(str(questions[0]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans2 = input(str(questions[1]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans3 = input(str(questions[2]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans4 = input(str(questions[3]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans5 = input(str(questions[4]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans6 = input(str(questions[5]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans7 = input(str(questions[6]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans8 = input(str(questions[7]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans9 = input(str(questions[8]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans10 = input(str(questions[9]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans11 = input(str(questions[10]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans12 = input(str(questions[11]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans13 = input(str(questions[12]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans14 = input(str(questions[13]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans15 = input(str(questions[14]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans16 = input(str(questions[15]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans17 = input(str(questions[16]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans18 = input(str(questions[17]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans19 = input(str(questions[18]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans20 = input(str(questions[19]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans21 = input(str(questions[20]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans22 = input(str(questions[21]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans23 = input(str(questions[22]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans24 = input(str(questions[23]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans25 = input(str(questions[24]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))
    ans26 = input(str(questions[25]).lstrip('[\'').rstrip('\']')+'\na) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nb) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nc) '
                +str(answers[4]).lstrip('[\'').rstrip('\']')+'\nd) '
                +str(answers[4]).lstrip('[\'').rstrip('\']'))