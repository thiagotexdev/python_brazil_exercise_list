number_1 = input('Enter a first number: ')
print(f'The number informed was: {number_1} ')
number_2 = input('Enter a second number: ')
print(f'The number informed was: {number_2} ')

if(number_1 > number_2):
    print(f'The higher number informed was: {number_1} ')
elif(number_1 == number_2):
    print('The number informed is equal !! ')
else:
    print(f'The higher number informed was: {number_2} ')

print(type(number_1))
print(type(number_2))