#for Big-O operation
import random
import time
import matplotlib.pyplot as plt
import re
from fractions import Fraction as frac
from math import gcd
import chemparse as chem

MAX_LEN = 200

def count_common_elements_nested_loops(l1, l2):
    common_elements = []
    count = 0
    for v in l1:
        for w in l2:
            if w == v:
                common_elements.append(w)
                count += 1
    return count

print('\nIMPORTANT: This program is case sensitive, thus:'
      '\n- Elements and compounds must be provided correctly (i.e. C, Cu, O2, CH4). '
      '\n- An unbalanced equation as must be provided as follows: H2 + O2 -> H2O'
      '\n- If there is a factored compound, simplify (i.e. (NH4)2 should be N2H8).'
      '\n- The program will recognise random letters and words as elements; ensure '
      'they are written correctly to avoid confusion.'
      '\nOtherwise, the program may yield incorrect results or malfunction.\n')

ListOfElements = []
MatrixOfElements = []
equation = input('Provide the equation: ').replace(' ', '').replace(',', '')
reactants, products = equation.split("->")
reactants = reactants.replace(' ', '').split("+")
products = products.replace(' ', '').split("+")

start1=time.time()
def augment_matrix(element, index, count, side):
    if index == len(MatrixOfElements):
        MatrixOfElements.append([])
        for _ in ListOfElements:
            MatrixOfElements[index].append(0)
    if element not in ListOfElements:
        ListOfElements.append(element)
        for i in range(len(MatrixOfElements)):
            MatrixOfElements[i].append(0)
    column = ListOfElements.index(element)
    MatrixOfElements[index][column] += count * side


def retrieve_elements(segment, index, multiplier, side):
    elementsAndNumbers = re.split('([A-Z][a-z]?)', segment)
    i = 0
    while i < len(elementsAndNumbers) - 1:  # last element always blank
        i += 1
        if len(elementsAndNumbers[i]) > 0:
            if elementsAndNumbers[i + 1].isdigit():
                count = int(elementsAndNumbers[i + 1]) * multiplier
                augment_matrix(elementsAndNumbers[i], index, count, side)
                i += 1
            else:
                augment_matrix(elementsAndNumbers[i], index, multiplier, side)


def separate_elements(compound, index, side):
    segments = re.split('(\([A-Za-z0-9]*\)[0-9]*)', compound)
    for segment in segments:
        if segment.startswith('('):
            segment = re.split('\)([0-9]*)', segment)
            elementsParse = chem.parse_formula(segment)
            multiplier = int(elementsParse.values())
            segment = segment[0][1:]
        else:
            multiplier = 1
        retrieve_elements(segment, index, multiplier, side)


for i in range(len(reactants)):
    separate_elements(reactants[i], i, 1)
for i in range(len(products)):
    separate_elements(products[i], i + len(reactants), -1)

tempMatrix = MatrixOfElements
A = [list(x) for x in zip(*tempMatrix)]


def largest_row_pivot(A, k):
    max_row = k
    for i in range(k + 1, len(A)):
        if abs(A[i][k]) > abs(A[i - 1][k]):
            max_row = i
    return max_row


def elimination_phase(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n)):
        max_row = largest_row_pivot(A, k)
        if A[max_row][k] == 0:
            break
        A[k], A[max_row] = A[max_row], A[k]
        for i in range(k + 1, m):
            c = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - c * A[k][j]
            A[i][k] = 0


def backward_substitution_phase(A):
    m, n = len(A), len(A[0])
    for k in range(min(m, n) - 1, 0, -1):
        if A[k][k] == 0:
            continue
        for i in range(k - 1, -1, -1):
            c = A[i][k] / A[k][k]
            for j in range(i, n):
                A[i][j] = A[i][j] - c * A[k][j]
    for i in range(min(m, n)):
        if A[i][i] == 0:
            continue
        for j in range(n - 1, i - 1, -1):
            A[i][j] = A[i][j] / A[i][i]


def gaussian_elimination():
    elimination_phase(A)
    backward_substitution_phase(A)


val3Floats = []
val3Fracs = []

gaussian_elimination()

matrixArray = A
for i, row in enumerate(matrixArray):
    if i == len(matrixArray) - 1 and matrixArray[i][-1] == 0:
        continue
    elif matrixArray[i][i] == 0:
        continue
    else:
        val3 = float(row[-1])
        val3 *= -1
        val3Floats.append(val3)
        val3 = frac(val3).limit_denominator()
        val3Fracs.append(val3.denominator)

lcm = 1
for i in val3Fracs:
    lcm = lcm*i//gcd(lcm, i)

freeVar = lcm
varRes = []

for i in range(len(val3Floats)):
    res = val3Floats[i] * freeVar
    varRes.append(int(res))

varRes.append(freeVar)

balanced = ''
for i in range(len(reactants)):
    balanced += str(varRes[i]) + reactants[i]
    if i < len(reactants) - 1:
        balanced += ' + '
balanced += ' -> '

for i in range(len(products)):
    balanced += str(varRes[i + len(reactants)]) + products[i]
    if i < len(products) - 1:
        balanced += ' + '
print(balanced)

end1=time.time()
runtime1=end1-start1
print("elapsed Time: {:.16f} seconds".format(runtime1))
if __name__ == "__main__":

    # Initialise results containers
    lengths_nested = []
    times_nested = []
    lengths_comp = []
    times_comp = []
    lengths_hash_table = []
    times_hash_table = []
    lengths_sets = []
    times_sets = []

    for length in range(0, MAX_LEN, 10):
        # Generate random lists
        l1 = [random.randint(0, 99) for _ in range(length)]
        l2 = [random.randint(0, 99) for _ in range(length)]

        # Time execution for nested lists version
        start = time.perf_counter()
        count_common_elements_nested_loops(l1, l2)
        end = time.perf_counter()

        # Store results
        lengths_nested.append(length)
        times_nested.append(end - start)

    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Common List Elements Algorithm - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_nested, times_nested, label="count_common_elements_nested_loops()")
    plt.legend()
    plt.tight_layout()
    plt.show()


