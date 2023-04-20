import chemparse as chem
def element_balancer():
    react_list = []
    prod_list = []
    reactant_num = int(input("How many reactants do you have? "))
    for i in range(reactant_num):
        reactants = react_list.append(chem.parse_formula(input("Enter the reactants: ")))
    product_num = int(input("How many products do you have? "))
    for i in range(product_num):
        products = prod_list.append(chem.parse_formula(input("Enter the products: ")))
    return react_list,prod_list
react_list,prod_list = element_balancer()
print(react_list)
print(prod_list)