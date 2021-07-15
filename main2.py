import json, os

filepath = os.path.abspath(os.path.realpath('__file__'))
filedir = os.path.split(filepath)[0]
print(filedir)
file_name = '/Data/Product-list.json'
data = os.path.join(filedir, '/Data/Product-list.json')
print('hello', data)

def dump():
    with open('/Users/Thomas/Documents/Generation-mini-project/Product-list.json', 'w') as outfile:
        json.dump(product_list, outfile)


def load_products():
    with open('/Users/Thomas/Documents/Generation-mini-project/Product-list.json', 'r') as infile:
        global product_list
        product_list = json.load(infile)
        return(product_list)

product_list = load_products()

def main_menu():
    print("Main Menu-- Enter; 1 for Product Menu, 0 to end process")
    main_options = input("Enter Choice (1 or 0)")
    if main_options == '1':
        return(product_menu())
    elif main_options == '0':
        print("Exiting....")
        exit()
    else:
        print("Inappropriate input detected")
        return(main_menu())


def product_menu():
    print("Product Menu-- Enter; 0 to return to Main Menu, 1 to see the list of products, 2 to create a new product, 3 to update an existing product or 4 to delete a product")
    product_options = int(input("Enter Choice (0, 1, 2, 3 or 4)"))
    if product_options == 0:
        print("Loading main menu.....")
        return(main_menu())
    elif product_options == 1:
        print("Loading product list......")
        return(load_products())
    elif product_options == 2:
        print("Begin adding product process...")
        return(add_product())
    elif product_options == 3:
        print("Begin updating process......")
        return(update_products())
    elif product_options == 4:
        print("Begin product deletion process")
        return(delete_product())
    else:
        print("Inappropriate input detected")
        return(product_menu())


def add_product():
    print("What is the name of the product you want to add? ")
    name = input("Name: ")
    product_list.append(name)
    print("Would you like to add another product? ")
    again = input("Yes (y) or No (n): ")
    if again.lower() == 'y':
        add_product()
    elif again.lower() == 'n':
        print("Saving new product.....")
        print(product_list)
        dump()

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
    dump()


def delete_product():
    for product in product_list:
        index = product_list.index(product)
        print("{} : {}".format(product, index))
    print("Which product would you like to delete? ")
    chosen_prod = int(input("Enter the Product ID: "))
    print("you are requesting to delete {} : {}".format(chosen_prod, product_list[chosen_prod]))
    confirm = input("please confirm (y or n): ")
    if confirm.lower() == 'y':
        print("Deleting....")
        del product_list[chosen_prod]
        print(product_list)
        dump()
    elif confirm.lower() == 'n':
        print("Cancelling.... ")
        exit()

###main_menu()
