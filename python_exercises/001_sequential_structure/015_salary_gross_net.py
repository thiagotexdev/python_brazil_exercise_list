print('Gross Salary and Net Salary values Calculator')

salvalue = float(input('Enter the work value per hour: '))
salhours = float(input('Enter the worked hours in a month: '))

saltotal = salvalue * salhours

salincometax = (saltotal*11/100)
salinss = (saltotal*8/100)
salsyndicate = (saltotal*5/100)
salnet = saltotal - salincometax - salinss - salsyndicate

print(f'The gross salary in the period was: {saltotal}')
print(f'The value discounted for Income Tax was: {salincometax}')
print(f'The value discounted for National Institute of Social Security was: {salinss}')
print(f'The value discounted for syndicate was: {salsyndicate}')
print(f'The net salary in the period was: {salnet}')