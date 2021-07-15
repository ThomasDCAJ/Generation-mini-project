 while True:
            data = input("Enter an item for your list: ")
            repeat = input("Would you like to enter another item? (y or n)")
            self.name.append(data)
            if repeat.lower() == 'n':
                break
            elif repeat.lower() =='y':
                continue
            else:
                print("Improper input, Try Again! ")
                continue
        print(name)

x = Name()