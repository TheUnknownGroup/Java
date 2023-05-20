import time

def ask_grading():
    global gradingscale
    gradingscale = int(input('Are you looking to grade one sem., or both?\nType 1 (for 1 sem.) or Type 2 (for both).\n'))
ask_grading()



if gradingscale == 1:
    q1 = float(input('Quarter 1 Grade: ')); q2 = float(input('Quarter 2 Grade: ')); s1 = q1+q2; s1grade = s1/2; eoygrade = s1grade
elif gradingscale == 2:
    q1 = float(input('Quarter 1 Grade: ')); q2 = float(input('Quarter 2 Grade: ')); q3 = float(input('Quarter 3 Grade: ')); q4 = float(input('Quarter 4 Grade: ')); time.sleep(0.5); quarters = q1+q2+q3+q4; eoygrade = quarters/4
else:
    print('You have entered a number that is not of the different types (1 or 2) please try again.'); time.sleep(1); ask_grading()

print('Calculating...\n'); time.sleep(3)

print('Done!\n'); time.sleep(1); print(f'EOYGrade: {eoygrade}%')