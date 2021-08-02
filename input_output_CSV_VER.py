import  os, csv

filedir = os.path.dirname(os.path.realpath('__file__'))
productcsvpath = './Data/Product-list.csv'
couriercsvpath = './Data/Courier-list.csv'
ordercsvpath = './Data/Orders-list.csv'
product_csv_path = os.path.join(filedir, productcsvpath)
couriers_csv_path = os.path.join(filedir, couriercsvpath)
orders_csv_path = os.path.join(filedir, ordercsvpath)

'''def load_cour_csv():
    with open(couriers_csv_path, 'r') as infile:
        csvreader = csv.reader(infile)
        contents = list()
        for item in csvreader:
            contents.append(item)
        return contents

couriers_list = load_cour_csv()
print(couriers_list)


def dump_cour_csv():
    with open(couriers_csv_path, 'w') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(couriers_list)'''

def load_from_csv(path):
    contents = []
    with open(path, 'r') as infile:
        reader = csv.DictReader(infile, delimiter = ',')
        for row in reader:
            item = dict(row)
            contents.append(item)
        return contents




def dump_to_csv(path, list):
    with open(path, "w") as outfile:
        fieldnames = ['name', 'price']
        csvwriter = csv.DictWriter(outfile, fieldnames = fieldnames)
        csvwriter.writeheader()
        for item in list:
            csvwriter.writerow(item)



def load_ords_csv():
    contents = []
    with open(orders_csv_path, 'r') as infile:
        reader = csv.DictReader(infile, delimiter = ',')
        for row in reader:
            item = dict(row)
            contents.append(item)
        return contents

orders_list = load_ords_csv()


def dump_ords_csv():
    with open(orders_csv_path, "w") as outfile:
        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        csvwriter = csv.DictWriter(outfile, fieldnames = fieldnames)
        csvwriter.writeheader()
        for item in orders_list:
            csvwriter.writerow(item)
