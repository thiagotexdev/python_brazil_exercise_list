print('Ideal weight person calculator per gender')

perheight = float(input('''Enter the person's height: '''))

idealweight_male = (72.7 * perheight) - 58
idealweight_female = (62.1 * perheight) - 44.7

print('The ideal weight of person is:')
print(f' {idealweight_male} for man')
print(f' {idealweight_female} for woman')
