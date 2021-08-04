from Products_Functions import add_product, delete_product, update_products
from Orders_Functions import add_order, delete_order, update_orders, update_order_status
from Couriers_Functions import add_courier, update_couriers, delete_courier
from Useful_Functions import print_list
from input_output_CSV_VER import load_from_csv, product_csv_path, orders_csv_path, couriers_csv_path
products_list = load_from_csv(product_csv_path)
couriers_list = load_from_csv(couriers_csv_path)
orders_list = load_from_csv(orders_csv_path)

def main_menu():
    print("Main Menu: \n 1 for Product Menu \n 2 for Courier Menu \n 3 for Orders Menu \n 0 to end process")
    main_options = int(input("Enter Choice (1, 2, 3 or 0): \n "))
    if main_options == 1:
        return(product_menu())
    elif main_options == 2:
        return(courier_menu())
    elif main_options == 3:
        return(orders_menu())
    elif main_options == 0:
        print("Exiting....")
        exit()
    else:
        print("Inappropriate input detected")
        return(main_menu())

def product_menu():
    print("Product Menu: \n 0 to return to Main Menu \n 1 to see the list of products \n 2 to create a new product \n 3 to update an existing product \n 4 to delete a product")
    product_options = int(input("Enter Choice (0, 1, 2, 3 or 4)"))
    if product_options == 0:
        print("Loading main menu.....")
        return(main_menu())
    elif product_options == 1:
        print("Loading product list......")
        print_list(products_list)
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
    print("Courier Menu: \n 0 to return to Main Menu \n 1 to see the list of couriers \n 2 to create a new courier \n 3 to update an existing courier \n 4 to delete a courier")
    courier_options = int(input("Enter Choice (1, 2, 3, 4 or 0)"))
    if courier_options == 0:
        print("Loading main menu.....")
        return(main_menu())
    elif courier_options == 1:
        print("Loading courier list......")
        print_list(couriers_list)
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


def orders_menu():
    print("Orders Menu: \n 0 to return to Main Menu \n 1 to see the list of orders \n 2 to create a new order \n 3 to update an existing order status \n 4 to update an existing order \n 5 to delete an order.")
    order_options = int(input("Enter Choice (1, 2, 3, 4, 5 or 0)"))
    if order_options == 0:
        print("Loading main menu......")
        return(main_menu())
    elif order_options == 1:
        print("Loading orders list......")
        print_list(orders_list)
    elif order_options == 2:
        print("Begin adding order process......")
        return(add_order())
    elif order_options == 3:
        print("Begin updating order status process......")
        return(update_order_status())
    elif order_options == 4:
        print("Begin updating order process......")
        return(update_orders())
    elif order_options == 5:
        print("Begin order deletion process")
        return(delete_order())
    else:
        print("Inappropriate input detected")
        return(orders_menu())
main_menu()




