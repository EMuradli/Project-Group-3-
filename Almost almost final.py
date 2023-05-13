import re
from fractions import Fraction as frac
from math import gcd
import chemparse as c

ListOfElements = []
MatrixOfElements = []
print("As an example, here is what your input should look like: P4O10 + H2O -> H3PO4")
equation = input('Provide the equation. This is case sensitive').replace(' ', '').replace(',', '')
reactants, products = equation.split("->")
reactants = reactants.replace(' ', '').split("+")
products = products.replace(' ', '').split("+")
print(reactants)
print(products)


def augmentMatrix(element, index, count, side):
    if index == len(MatrixOfElements):
        MatrixOfElements.append([])
        for x in ListOfElements:
            MatrixOfElements[index].append(0)
    if element not in ListOfElements:
        ListOfElements.append(element)
        for i in range(len(MatrixOfElements)):
            MatrixOfElements[i].append(0)
    column = ListOfElements.index(element)
    MatrixOfElements[index][column] += count * side


def retrieveElements(segment, index, multiplier, side):
    elementsAndNumbers = re.split('([A-Z][a-z]?)', segment)
    i = 0
    while (i < len(elementsAndNumbers) - 1):  # last element always blank
        i += 1
        if (len(elementsAndNumbers[i]) > 0):
            if (elementsAndNumbers[i + 1].isdigit()):
                count = int(elementsAndNumbers[i + 1]) * multiplier
                augmentMatrix(elementsAndNumbers[i], index, count, side)
                i += 1
            else:
                augmentMatrix(elementsAndNumbers[i], index, multiplier, side)


def seperateElements(compound, index, side):
    segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
    for segment in segments:
        if segment.startswith('('):
            segment = re.split('\)([0-9]*)', segment)
            elementsParse = c.parse_formula(segment)
            multiplier = int(elementsParse.values())
            # multiplier = int(segment[1])
            segment = segment[0][1:]
        else:
            multiplier = 1

        retrieveElements(segment, index, multiplier, side)
        print(segment)


for i in range(len(reactants)):
    seperateElements(reactants[i], i, 1)
for i in range(len(products)):
    seperateElements(products[i], i + len(reactants), -1)

tempMatrix = MatrixOfElements
A = [list(x) for x in zip(*tempMatrix)]

def largest_row_pivot(A, k):
    i_max = k
    for i in range(k + 1, len(A)):
        if abs(A[i][k]) > abs(A[i - 1][k]):
            i_max = i
    return i_max


def elimination_phase(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n)):
        i_max = largest_row_pivot(A, k)
        if A[i_max][k] == 0:
            break
        A[k], A[i_max] = A[i_max], A[k]  # Operation 1: swap
        for i in range(k + 1, m):
            c = A[i][k] / A[k][k]  # Operation 3: linear
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - c * A[k][j]
            A[i][k] = 0


def backward_substitution_phase(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n) - 1, 0, -1):  # [min(m, n), 1]
        if A[k][k] == 0:
            continue
        for i in range(k - 1, -1, -1):  # [k - 1, 0]
            c = A[i][k] / A[k][k]
            for j in range(i, n):
                A[i][j] = A[i][j] - c * A[k][j]  # Operation 3: linear
    for i in range(min(m, n)):
        if A[i][i] == 0:
            continue
        for j in range(n - 1, i - 1, -1):  # [n - 1, i]
            A[i][j] = A[i][j] / A[i][i]  # Operation 2: scale


def gaussian_elimination():
    elimination_phase(A)
    backward_substitution_phase(A)


lst1 = []
lst2 = []

if __name__ == "__main__":
    gaussian_elimination()
    matrixArray = A
    for i, row in enumerate(matrixArray):
        if i == len(matrixArray) - 1 and matrixArray[i][-1] == 0:
            continue
        elif matrixArray[i][i] == 0:
            continue
        else:
            thirdVal = float(row[-1])
            thirdVal *= -1
            lst2.append(thirdVal)
            thirdVal = frac(thirdVal).limit_denominator()
            lst1.append(thirdVal.denominator)

lcm = 1
for i in lst1:
    lcm = lcm*i//gcd(lcm, i)
# print(lcm)

freeVar = lcm
lst3 = []

for i in range(len(lst2)):
    res = lst2[i] * freeVar
    lst3.append(int(res))

lst3.append(freeVar)
print(lst3)
# print(type(lst3))
balanced = ''
for i in range(len(reactants)):
    balanced += str(lst3[i]) + reactants[i]
    # print(balanced)
    # print(type(balanced))
    if i < len(reactants) - 1:
        balanced += ' + '
balanced += ' -> '
for i in range(len(products)):
    balanced += str(lst3[i + len(reactants)]) + products[i]
    if i < len(products) - 1:
        balanced += ' + '
print(balanced)
# for i in range(len(reactants)):
#     z1 = f'{lst3[i]}{reactants[i]}'
#     if i < len(reactants) - 1:
#         z1 = f'{lst3[i]}{reactants[i]} + {lst3[i+1]}{reactants[i+1]}'
#         g1 = f'{z1}'
#     else:
#         g1 = f'{z1}'
#
# for i in range(len(products)):
#     z2 = f'{lst3[i + len(reactants)]}{products[i]}'
#     if i < len(products) - 1:
#         z2 = f'{lst3[i + len(reactants)]}{products[i]} + {lst3[i+1]}{products[i+1]}'
#         g2 = f' -> {z2}'
#     else:
#         g2 = f' -> {z2}'
#
# print(g1 + g2)

# Na3PO4 + KOH
# NaOH + K3PO4