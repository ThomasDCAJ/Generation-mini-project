def enumerate_list(items_list):
    choice = int(input("Which order would you like to update? (Enter order_id): "))
    key_idx = {}
    for item in items_list:
        if item[0] == str(choice):
            chosen = item
            print(chosen)
            for id, value in enumerate(chosen.keys()):
                key_idx[id] = value
    return(key_idx, choice)