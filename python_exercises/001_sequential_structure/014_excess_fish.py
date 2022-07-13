print('Calculate Excess Weight of Fishing')

fishweight = float(input('Enter a weight of fish greater than 50 kg: '))
weightlimit = 50

print(f'The weight limit is: {weightlimit} kg')

finevalue = 4.00
print(f'The value of fine is: R$ {finevalue}')

excessfine = (fishweight - weightlimit) * finevalue

print(f'The amount of fine payable is: R$ {excessfine} ')