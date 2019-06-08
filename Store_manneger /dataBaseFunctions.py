import sqlite3
User_input = str
# Creating / Open:

conn =sqlite3.connect('storeDataBase.db')

c = conn.cursor()
#
# conn.execute("""CREATE TABLE storeDataBase(
#                     itemName text,
#                     itemPrice Real,
#                     itemQuantity integer
#                       )""")
#
# ......START OF DATABASE FUNCTIONS.......

def new_item():
    print("........................................")
    Name = input("Type in item's Name :\n").upper()
    Price = float(input("Type in item's price :\n"))
    Quantity = int(input("Type in item's Quantity in Stock :\n"))
    print("\n")
    print(".......ITEM WAS ADDED........\n\n")
    with conn:
        c.execute("INSERT INTO storeDataBase VALUES (:itemName, :itemPrice, :itemQuantity)",
                  {'itemName':Name, 'itemPrice':Price ,'itemQuantity':Quantity})

# ......................................

def find_item_by_name():
    itemName = str
    try:
        print("........................................")
        itemName = input("Type in item's Name to Search :\n[E]- EXIT\n>>").upper()
        print("........................................\n")
        c.execute("SELECT * FROM storeDataBase WHERE itemName=:itemName", {'itemName': itemName})
        search = c.fetchone()
        for info in search[0:1]:
            print(f'Item: {info}')
        for info in search[1:2]:
            print(f'Price: ${info}')
        for info in search[2:3]:
            print(f'Quantity: {info}\n\n')
        User_input = input("[M]- Main Menu\n[F]- Find Another Item\n[E]- Exit").upper()

        # ....... User Options ........

        if User_input == "M":
            print("Fixing")
            # main_menu()
        elif User_input == "F":
            find_item_by_name()
        if itemName == 'E':
            exit()
    except:
        print("........ITEM WAS NOT FOUND TRY AGAIN.........")
        find_item_by_name()

# ......................................

def update_item_quantity():
    print(".........Updating Quantity...........\n")
    name = input("Type in item's Name to update :\n").upper()
    quantity = input("Enter new Quantity in Stock\n")
    print(".........Quantity UPDATED..........")
    with conn:
        c.execute("""UPDATE storeDataBase SET itemQuantity = :newQuantity
                    WHERE itemName =:itemName""",
                  {'itemName': name, 'newQuantity':quantity})

# ......................................

def remove_item(user_input):
    itemName = user_input
    try:
        c.execute("SELECT * FROM storeDataBase WHERE itemName=:itemName", {'itemName': itemName})
        search = c.fetchone()
        for info in search[0:1]:
            print(f'Item: {info}')
        for info in search[1:2]:
            print(f'Price: ${info}')
        for info in search[2:3]:
            print(f'Quantity: {info}\n\n')
        U_input = input("[D]- DELETE").upper()
        if U_input == 'D':
            print(".........REMOVING AN ITEM...........\n")
            with conn:
                c.execute("DELETE from storeDataBase WHERE itemName = :itemName",
                      {'itemName':itemName})
                print(".........ITEM WAS SUCCESSFULLY REMOVED..........")
    except:
        print(".........ITEM WAS NOT FOUND TRY AGAIN..........")
        remove_item()

# # ..................END OF DATABASE FUNCTIONS ....................


conn.commit()

def ubdate_all_quantity():
    c.execute("SELECT * FROM storeDataBase WHERE itemQuantity = itemQuantity")
    search = c.fetchall()
    print(search)
# ubdate_all_quantity()