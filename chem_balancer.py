#this is an edited version of Wisang's code.

import chemparse

print("NOTICE: \nThis program is case sensitive.")


def element_balancer():
    reactants_list = []
    products_list = []

    num_reactants = int(input("How many reactants do you have?: "))
    for i in range(num_reactants):
        reactants = input("Enter the reactants: ")
        reactants_dict = chemparse.parse_formula(reactants)
        for i in range(len(reactants_dict.keys())):
            reactant_list_element = list(reactants_dict.keys())
            reactants_list.append(reactant_list_element[i])

    num_products = int(input("How many products do you have?: "))
    for i in range(num_products):
        products = input("Enter the products: ")
        products_dict = chemparse.parse_formula(products)
        for i in range(len(products_dict.keys())):
            product_list_element = list(products_dict.keys())
            products_list.append(product_list_element[i])

    return reactants_list, products_list


r_list, p_list = element_balancer()
print(r_list)
print(p_list)
sorted_r_list=sorted(r_list)
sorted_p_list=sorted(p_list)

def countOccurrence(a):
  k = {}
  for j in a:
    if j in k:
      k[j] +=1
    else:
      k[j] =1
  return k

print(countOccurrence(sorted_r_list))
print(countOccurrence(sorted_p_list))

if countOccurrence(sorted_r_list)==countOccurrence(sorted_p_list):
    print("this is balanced")
else:
    print("it is not balanced")
    matrix_list= countOccurrence(sorted_r_list + sorted_p_list)
    print(matrix_list)

# the things below i wasnt able to make it work. I was planning to create the rows based on the amount of elements
# present while the columns with the amount of molecules ie. CH4+O2=CO2+H2O has 3 rows and 4 columns.
# Also I tried to make the dictionary for the elements in alphabetical order cuz when the dic for reactants and
# products are printed they arent in order nor concatenated on both sides so i also made something to sort the list and
# count the total amount of each element

#     def createMatrix(rowCount, colCount, dataList):
#         mat = []
#         for i in range(rowCount):
#             rowList = []
#             for j in range(colCount):
#                 # you need to increment through dataList here, like this:
#                 rowList.append(dataList[rowCount * i + j])
#             mat.append(rowList)
#
#         return mat
#
#
#     def main():
#
#         mat = createMatrix(len(matrix_list), (len(r_list+p_list)), matrix_list)
#         print(mat)
#
#
# main()





