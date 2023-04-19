import chemparse
print("NOTICE: \nThis program is case sensitive.")
def element_balancer():
    reactants_list=[]
    products_list = []
    
    num_reactants = int(input("How many reactants do you have?: "))
    for i in range(num_reactants):
        reactants=input("Enter the reactants: ")
        reactants_dict=chemparse.parse_formula(reactants)
        for i in range(len(reactants_dict.keys())):
         reactant_list_element = list(reactants_dict.keys())
         reactants_list.append(reactant_list_element[i])

    num_products = int(input("How many products do you have?: "))
    for i in range(num_products):
        products=input("Enter the products: ")
        products_dict = chemparse.parse_formula(products)
        for i in range(len(products_dict.keys())):
            product_list_element=list(products_dict.keys())
            products_list.append(product_list_element[i])
    


    return reactants_list,products_list
r_list,p_list = element_balancer()
print(r_list)
print(p_list)


