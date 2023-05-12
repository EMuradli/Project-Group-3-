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
        else:
            multiplier = 1
        findElements(segment, index, multiplier, side)


for i in range(len(reactants)):
    compoundDecipher(reactants[i], i, 1)
for i in range(len(products)):
    compoundDecipher(products[i], i + len(reactants), -1)

tempMatrix = elementMatrix
A = [list(x) for x in zip(*tempMatrix)]
b = ([0] * len(elementList))
c = list(b)


def pivot_row(A, k):
    i_max = k
    for i in range(k + 1, len(A)):
        if abs(A[i][k]) > abs(A[i - 1][k]):
            i_max = i
    return i_max


def forward_elimination(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n)):
        i_max = pivot_row(A, k)
        if A[i_max][k] == 0:
            break
        A[k], A[i_max] = A[i_max], A[k]  # Operation 1: swap
        for i in range(k + 1, m):
            c = A[i][k] / A[k][k]  # Operation 3: linear
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - c * A[k][j]
            A[i][k] = 0


def backward_substitution(A):
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
    forward_elimination(A)
    backward_substitution(A)
    for r in A:
        for s in range(len(r)):
            r[s] = str(frac(str(r[s])).limit_denominator())
        print(r)


if __name__ == "__main__":
    gaussian_elimination()
