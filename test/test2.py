import time
line = '------'
tip = 'Just write a or b.'

print('Please take this short quiz.')
print(tip)
time.sleep(1)
print(line)
print('You are tall.\na) True\nb) False')
bool1 = input()
if bool1 == 'a':
    is_tall = True
elif bool1 == 'b':
    is_tall = False
print('You are male.\na) True\nb) False')
bool2 = input()
if bool2 == 'a':
    is_male = True
elif bool2 == 'b':
    is_male = False
print('')
if is_male and is_tall:
    print('You are a tall male')
elif is_male and not(is_tall):
    print('You are a short male')
elif not(is_male) and is_tall:
    print('You are not a male, but tall.')
else:
    print('You are neither male or tall.')
