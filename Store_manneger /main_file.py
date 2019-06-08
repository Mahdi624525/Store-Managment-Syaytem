import dataBaseFunctions as dataF
import transaction
import Functions as fun
User_input = str
def main_menu():
    while True :
        print("\n.....Welcome To Store Manager Assistant......\n")
        print("...Choose one of the following...")
        print("\t[I]- Inventory\n\t[C]- Cashiering")
        print("\t[T]- Transactions Summary\n\t[E]- Exit")
        User_input = input("\t>>").upper()

# ........ picking the Page .........

        if User_input == "I":
            check_inventory()
        elif User_input == 'C':
            fun.Cashiring()
        elif User_input == 'T':
            print("......DEMO TO BE UPDATED.........")
            summery = transaction.summary_total()
            print("[A]- TRANSACTIONS TOTAL")
            print("[M]- MAIN MENU")
            u_input = input(">>>").upper()
            if u_input == "A":
                print(f'TOTAL REVENUE IS: ${summery}')
        elif User_input == 'M':
            main_menu()
        else: print('Please Enter a valid Option')

# ........... Finished ...........

def check_inventory():

    print(".....INVENTORY MANAGE SYSTEM......")
    print("...Choose one of the following...")
    print("\t[A]- Add a New item\n\t[B]- Find an item")
    print("\t[C]- Remove an item\n\t[I]- Update Item's Quantity\n\t"
          "[M]- Main Menu\n\t[E]- Exit")
    User_input = input("\t>>").upper()
    if User_input == "A":
        dataF.new_item()
        check_inventory()
    elif User_input == 'B':
        dataF.find_item_by_name()
    elif User_input == 'C':
        print(".........REMOVE AN ITEM.........")
        u_input = input("ENTER ITEM'S NAME :\n>>>").upper()
        dataF.remove_item(u_input)
        User_input = input("[M] - Main Menu").upper()
    elif User_input == 'M':
            main_menu()
    elif User_input == 'I':
            dataF.update_item_quantity()
    elif User_input == 'E':
        exit()
    else:
        print('Please Enter a valid Option')

main_menu()
