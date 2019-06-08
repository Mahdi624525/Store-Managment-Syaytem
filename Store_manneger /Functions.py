
import sqlite3
import transaction

item = str
user_input = str
def Cashiring():
    # ........ Main Menu .......#
    print("\t.....CASHIERING......")
    print("...Choose one of the following...")
    print("\t[S]- Sell an item\n\t[R]- Refund an item")
    print("\t[M]- Main Menu\n\t[E]- Exit")
    User_input = input("\t>>").upper()
    if User_input == "S":
        sell_item()
    elif User_input == 'R':
        refund_item()
    elif User_input == 'M':
        print("")
    elif User_input == 'E':
        exit()
    else:
        print('Please Enter a valid Option')
        Cashiring()
def update_sold_item_quantity(updated_item, ubdated_quantity):
    conn = sqlite3.connect('storeDataBase.db')
    c = conn.cursor()
    with conn:
        c.execute("""UPDATE storeDataBase SET itemQuantity =:newQuantity
                    WHERE itemName =:itemName""",
                  {'itemName': updated_item, 'newQuantity': ubdated_quantity})
        print(".................................................")
        print(".................................................")
        print(" .....TRANSACTION WAS SUCCESSFULLY PROCESSED.....")
def find_item_for_cashiering(itemName):
    conn = sqlite3.connect('storeDataBase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM storeDataBase WHERE itemName=:itemName", {'itemName': itemName})
    search = c.fetchone()
    for i in range(1):
        for info in search[0:1]:
            print(f'Item: {info}')
        for info in search[1:2]:
            print(f'Price: ${info}')
        for info in search[2:3]:
            print("")
    return search


# .............................................................................#
def sell_item():

    try:
        item_name = input(" Type in item's Name:\n>>").upper()
        passed_item = find_item_for_cashiering(item_name)
        price = (passed_item[1])
        current_quantify = (passed_item[2])
        sold_quantity = int(input("How Many :\n\n"))
        # ........... Current quantity shall always be more than 0 .......
        if current_quantify == 1 :
                print(".....ITEM IS OUT OF STOCK.....")
                sell_item()
        elif sold_quantity > current_quantify :
            print(".....Not Enough Supply In Stock Try a Smaller amount.....")
            sell_item()
        elif sold_quantity < current_quantify :
            print('...........PROCESSING.............\n')
            transaction_total = sold_quantity * price
            print(f'Total amount Due: ${transaction_total}\n')
            print('...............................')
            user_input = input("[C]- Cash Out\n[T] - Cancel transaction\n>>").upper()
            if user_input == 'C':
                transactionType = "PURCHASE"
                current_total = transaction.summary_total()
                updated_total = transaction_total + current_total
                updated_quantity = current_quantify - sold_quantity
                update_sold_item_quantity(item_name.upper(),updated_quantity)
                transaction.new_Transaction('05/27/2019',item_name.upper(),sold_quantity,transaction_total,transactionType,updated_total)
            elif user_input == "T":
                print(".....................TRANSACTION CANCELLED............................")
                print(".................................................")
                print(".................................................")
    except:
        print(".....ITEM IS WAS NOT FOUND TRY AGAIN.....")
        print(".........................................")
        print(".........................................")
        sell_item()

# .................................. REFUND FUNCTION ...........................................#


def refund_item():
    try:
        item_name = input(" Type in Refunded item's Name:\n>>").upper()
        passed_item = find_item_for_cashiering(item_name)
        price = (passed_item[1])
        current_quantity  = (passed_item[2])
        refunded_quantity = int(input("How Many :\n\n"))

        print('...........PROCESSING.............\n')
        transaction_total = refunded_quantity * price * -1
        print(f'Total amount Refunded: ${transaction_total}\n')
        print('...............................')
        user_input = input("[R]- Refund\n[C] - Cancel transaction\n>>").upper()
        if user_input == 'R':

            transactionType = "(-REFUND-)"
            current_total = transaction.summary_total()
            updated_total = current_total + transaction_total
            updated_quantity = refunded_quantity + current_quantity
            update_sold_item_quantity(item_name,updated_quantity)
            transaction.new_Transaction('05/27/2019',item_name.upper(),refunded_quantity,transaction_total,
                                        transactionType,updated_total)
        elif user_input == "C":
            print(".....................TRANSACTION CANCELLED............................")
            print(".................................................")
            print(".................................................")

    except:
        print(".....ITEM IS WAS NOT FOUND TRY AGAIN.....")
        print(".........................................")
        print(".........................................")
        refund_item()

    # ..................  FINISH'S HERE   .......................... #
