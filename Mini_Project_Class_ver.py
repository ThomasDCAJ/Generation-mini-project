import json, os

filedir = os.path.dirname(os.path.realpath('__file__'))
datapath = './Data/Product-list.json'
courierpath = './Data/Courier-list.json'
product_path = os.path.join(filedir, datapath)
couriers_path = os.path.join(filedir, courierpath)


class Dataset:
    New_List = []
    Lists = ['Product', 'Courier']
    def __init__(self):
        self.name = input("What is the name of your dataset? ")
        self.Lists.append(self.name)
        while True:
            data = input("Enter an item for your list: ")
            repeat = input("Would you like to enter another item? (y or n)")
            self.New_List.append(data)
            if repeat.lower() == 'n':
                break
            elif repeat.lower() == 'y':
                continue
            else:
                print("Improper input, Try Again! ")
                continue
        print(self.New_List)
        new_path = './Data/' + str(self.name.capitalize()) + "-list.json"
        self.new_path = os.path.join(filedir, new_path)
        print("New path created @ {}".format(self.new_path))
        new_file = open(self.new_path, 'w')
        new_file.close()


    def Save_List(self):
        with open(self.new_path, 'w') as outfile:
            json.dump(self.New_List, outfile)


    def View_List(self):
        for lst in self.Lists:
            lst_idx = self.Lists.index(lst)
            print("ID {} : Name {}".format(lst_idx, lst))
        while True:
            choice_list = int(input("Which List would you like to view (Enter ID) : "))
            if choice_list > len(self.Lists) or choice_list < 0:
                continue
            else:
                break
        chosen_list = self.Lists[choice_list]
        chosen_list_path = './Data/' + str(chosen_list.capitalize()) + "-list.json"
        with open(chosen_list_path, 'r') as infile:
            contents = list(infile)
            print(contents)




x = Dataset.View_List()
