print('Bimester Calculator')

note_1 = float(input('Enter a first bimonthly note: '))
note_2 = float(input('Enter a second bimonthly note: '))
note_3 = float(input('Enter a third bimonthly note: '))
note_4 = float(input('Enter a fourth bimonthly note: '))

media = (note_1 + note_2 + note_3 + note_4) / 4

print(f'His bimonthly average was: {media}')

print(type(note_1))
print(type(note_2))
print(type(note_3))
print(type(note_4))

print(type(media))