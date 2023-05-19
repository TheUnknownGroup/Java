import time

q1 = int(input('Quarter 1 Grade: ')); q2 = int(input('Quarter 2 Grade: ')); q3 = int(input('Quarter 3 Grade: ')); q4 = int(input('Quarter 4 Grade: '))
time.sleep(0.5)
print('Calculating...\n'); time.sleep(3)

quarters = q1+q2+q3+q4

eoygrade = quarters/4

print('Done!\n'); time.sleep(1); print(f'EOYGrade: {eoygrade}%')