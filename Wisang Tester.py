import re
from fractions import Fraction as frac
elementList = []
elementMatrix = []
print("please input your reactants, this is case sensitive")
print("your input should look like: H2O+Ag3(Fe3O)4")
reactants = input("Reactants: ")
print("please input your products, this is case sensitive")
products = input("Products: ")
reactants = reactants.replace(' ', '').split("+")
products = products.replace(' ', '').split("+")
print(reactants)
print(products)


def addToMatrix(element, index, count, side):
    if index == len(elementMatrix):
        elementMatrix.append([])
        for x in elementList:
            elementMatrix[index].append(0)
    if element not in elementList:
        elementList.append(element)
        for i in range(len(elementMatrix)):
            elementMatrix[i].append(0)
    column = elementList.index(element)
    elementMatrix[index][column] += count * side


def findElements(segment, index, multiplier, side):
    elementsAndNumbers = re.split('([A-Z][a-z]?)', segment)
    i = 0
    while (i < len(elementsAndNumbers) - 1):  # last element always blank
        i += 1
        if (len(elementsAndNumbers[i]) > 0):
            if (elementsAndNumbers[i + 1].isdigit()):
                count = int(elementsAndNumbers[i + 1]) * multiplier
                addToMatrix(elementsAndNumbers[i], index, count, side)
                i += 1
            else:
                addToMatrix(elementsAndNumbers[i], index, multiplier, side)


def compoundDecipher(compound, index, side):
    segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
    for segment in segments:
        if segment.startswith('('):
            segment = re.split('\)([0-9]*)', segment)
            multiplier = int(segment[1])
            segment = segment[0][1:]
            # print(segment, multiplier)
        else:
            multiplier = 1
            # print(segment)
        findElements(segment, index, multiplier, side)


for i in range(len(reactants)):
    compoundDecipher(reactants[i], i, 1)
for i in range(len(products)):
    compoundDecipher(products[i], i + len(reactants), -1)

tempMatrix = elementMatrix
A = [list(x) for x in zip(*tempMatrix)]
# print(A)
b = ([0] * len(elementList))
c = list(b)
# print(elementMatrix)
# print(elementList)
# print(A)
# print(b)
# print(c)

# sol = A + [c]
#
# print(sol)

def gaussian_elimination(A, c):

    n = len(A)

    Ac = [A[i] + [c[i]] for i in range(n)]
    print(Ac)
    for i in range(n):
        # Find row with largest pivot
        max_row = i
        for j in range(i + 1, n):
            if abs(Ac[j][i]) > abs(Ac[max_row][i]):
                max_row = j
        # Swap current row with row containing largest pivot
        Ac[i], Ac[max_row] = Ac[max_row], Ac[i]
        # Eliminate entries below pivot
        for j in range(i + 1, n):
            factor = Ac[j][i] / Ac[i][i]
            for k in range(i + 1, n + 1):
                Ac[j][k] -= factor * Ac[i][k]
            Ac[j][i] = 0

    # Back substitution phase
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = Ac[i][n]
        for j in range(i + 1, n):
            x[i] -= Ac[i][j] * x[j]
        x[i] /= Ac[i][i]

    # Turning decimals into fractions if needed
    sol = {}
    for k in range(len(x)):
        xStr = str(x[k])
        xStrFrac = frac(xStr).limit_denominator()
        sol[f"x{k+1}"] = str(xStrFrac)

    return sol

sol = gaussian_elimination(A, c)


print(A)
print(b)
print(elementList)
print(elementMatrix)
print(len(elementMatrix))
print(len(elementList))
print(sol)