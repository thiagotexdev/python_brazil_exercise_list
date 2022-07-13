print('Two Integer Numbers And One Float Number Calculator')

print(' ------------------------------ ')
num1 = int(input('Enter a first number: '))
print(type(num1))

print(' ------------------------------ ')
num2 = int(input('Enter a second number: '))
print(type(num2))

print(' ------------------------------ ')
num3 = float(input('Enter a third number: '))
print(type(num3))

result1 = (num1 * 2) + (num2 /2)

print('----- Calculate sum of double of first number and a half of second number -----')
print(f'The result of sum is: {result1}')

result2 = (num1 * 3) + num3

print(' ------------------------------ ')
print(f'The result of the sum of the triple of the first number and the third number is: {result2} ')

result3 = num3 ** 3

print(' ------------------------------ ')
print(f'The result of exponentiaton of third number is: {result3}')