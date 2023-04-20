import chemparse as c

print('\nIMPORTANT: \n'
      'This program is case sensitive. Provide symbols as they appear on the periodic table. Some examples are, but'
      ' not limited to:'
      '\n\t- Element symbols with more than one letter must have only the first letter in uppercase (i.e. Cu).'
      '\n\t- If there are multiple atoms of an element, the amount must follow the symbol (i.e He3).\n')

element_list = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
                'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'Ge', 'As', 'Se',
                'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
                'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er',
                'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At',
                'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No',
                'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

equations = ('reactants', 'products')


def yes():
    for i in range(2):  # the function will only need to loop twice; once for reactants, once for products
        elements = input(f'Provide all {equations[i]}: ').replace(' ', '').replace(',', '').replace('+', '')
        elementsParse = c.parse_formula(elements)
        elementNames = list(elementsParse.keys())
        if all(item in element_list for item in elementNames) is False:
            print('Please try again.')
            continue
        else:
            pass

        for k in range(len(elementsParse)):
            elementNames = tuple(elementsParse.keys())
            elementAmount = tuple(elementsParse.values())
            print(f'Number of {elementNames[k]} atom(s) within the {equations[i]}: {int(elementAmount[k])}')


yes()
