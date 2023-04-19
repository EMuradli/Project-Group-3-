import chemparse

print('\nNOTICE: \n'
      '- This program is case sensitive. Provide symbols as they appear on the periodic table'
      ' (i.e. Cl must be written with a capital C and a lowercase l).\n')

skul = ('reactants', 'products')


def yes():
    for i in range(2):
        while True:
            try:
                amount = int(input(f'Amount of {skul[i]}: '))
            except ValueError:
                print('Please provide an integer.')
            else:
                break

        elements = input(f'Provide all {skul[i]}: ').replace(' ', '').replace(',', '').replace('+', '')

        for j in range(amount):
            elementsParse = chemparse.parse_formula(elements)
        for k in range(len(elementsParse)):
            elementNames = tuple(elementsParse.keys())
            elementAmount = tuple(elementsParse.values())
        print(f'The amount of {elementNames[k]} atoms in this compound are {elementAmount[k]}')


yes()
