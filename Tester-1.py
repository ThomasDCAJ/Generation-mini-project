import json
product_path = '/Users/Thomas/Documents/Generation-mini-project/Product-list.json'

def load_products():
    with open('/Users/Thomas/Documents/Generation-mini-project/Product-list.json', 'r') as infile:
        global product_list
        product_list = json.load(infile)
        return(product_list)

product_list = load_products()

def update_products():
    for product in product_list:
        index = product_list.index(product)
        print("{} : {}".format(product, index))
    print("Which product would you like to update? ")
    chosen_prod = int(input("Enter the product ID: "))
    print("What is the new name of the product? ")
    new_name = input("New Name: ")
    product_list[chosen_prod] = new_name
    print(product_list)
    with open('/Users/Thomas/Documents/Generation-mini-project/Product-list.json', 'w') as outfile:
        json.dump(product_list, outfile)

update_products()
