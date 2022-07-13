gender = str(input('Enter a letter represent your gender (M = Masculine , F= Feminine , O = Other ): '))
print(f'The letter informed was: {gender} ')


if(gender == 'M'):
    print('The gender informed was masculine ')
elif(gender == 'F'):
    print('The gender informed was feminine' )
elif(gender == 'O'):
    print('The gender informed was other' )
else:
    print('The gender informed is invalid ')

print(type(gender))
