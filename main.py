import json, os

filedir = os.path.dirname(os.path.realpath('__file__'))
datapath = './Data/Product-list.json'
courierpath = './Data/Courier-list.json'
product_path = os.path.join(filedir, datapath)
couriers_path = os.path.join(filedir, courierpath)

def dump_prod():
    with open(product_path, 'w') as outfile:
        json.dump(product_list, outfile)

def dump_cour():
    with open(couriers_path, 'w') as outfile:
        json.dump(courier_list, outfile)


def load_products():
    with open(product_path, 'r') as infile:
        global product_list
        product_list = json.load(infile)
        return(product_list)

def load_couriers():
    with open(couriers_path, 'r') as infile:
        global product_list
        courier_list = json.load(infile)
        return(courier_list)

product_list = load_products()
courier_list = load_couriers()

def main_menu():
    print("Main Menu-- Enter; 1 for Product Menu, 2 for Courier Menu, 0 to end process")
    main_options = input("Enter Choice (1 or 0)")
    if main_options == '1':
        return(product_menu())
    elif main_options == '2':
        return(courier_menu())
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


def courier_menu():
    print("Courier Menu-- Enter; 0 to return to Main Menu, 1 to see the list of couriers, 2 to create a new courier, 3 to update an existing courier or 4 to delete a courier")
    courier_options = int(input("Enter Choice (0, 1, 2, 3 or 4)"))
    if courier_options == 0:
        print("Loading main menu.....")
        return(main_menu())
    elif courier_options == 1:
        print("Loading courier list......")
        return(load_couriers())
    elif courier_options == 2:
        print("Begin adding courier process...")
        return(add_courier())
    elif courier_options == 3:
        print("Begin updating process......")
        return(update_couriers())
    elif courier_options == 4:
        print("Begin courier deletion process")
        return(delete_courier())
    else:
        print("Inappropriate input detected")
        return(courier_menu())

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
        dump_prod()

def add_courier():
    print("What is the name of the courier you want to add? ")
    name = input("Name: ")
    courier_list.append(name)
    print("Would you like to add another courier? ")
    again = input("Yes (y) or No (n): ")
    if again.lower() == 'y':
        add_courier()
    elif again.lower() == 'n':
        print("Saving new courier.....")
        print(courier_list)
        dump_cour()


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
    dump_prod()

def update_couriers():
    for courier in courier_list:
        index = courier_list.index(courier)
        print("{} : {}".format(courier, index))
    print("Which courier would you like to update? ")
    chosen_cour = int(input("Enter the courier ID: "))
    print("What is the new name of the courier? ")
    new_name = input("New Name: ")
    courier_list[chosen_cour] = new_name
    print(courier_list)
    dump_cour()


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
        dump_prod()
    elif confirm.lower() == 'n':
        print("Cancelling.... ")
        exit()

def delete_courier():
    for courier in courier_list:
        index = courier_list.index(courier)
        print("{} : {}".format(courier, index))
    print("Which courier would you like to delete? ")
    chosen_cour = int(input("Enter the Courier ID: "))
    print("you are requesting to delete {} : {}".format(chosen_cour, courier_list[chosen_cour]))
    confirm = input("please confirm (y or n): ")
    if confirm.lower() == 'y':
        print("Deleting....")
        del courier_list[chosen_cour]
        print(courier_list)
        dump_cour()
    elif confirm.lower() == 'n':
        print("Cancelling.... ")
        exit()

main_menu()
