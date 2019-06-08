import sqlite3

conn = sqlite3.connect('Transactions.db')

c = conn.cursor()
#
# conn.execute("""CREATE TABLE Transactions(
#                     transactionDate text,
#                     transactionItem text,
#                     transactionQuantity integer,
#                     transactionAmount Real,
#                     transactionType text,
#                     transactionTotal Real
#
#
#                       )""")

# ......START OF DATABASE FUNCTIONS.......
def new_Transaction (Date, item, Quantity, amount, Type,Total):
    with conn:
        c.execute("INSERT INTO Transactions VALUES "
                  "(:transactionDate, :transactionItem,"
                  " :transactionQuantity,:transactionAmount,"
                  ":transactionType,:transactionTotal)"
                  ,{'transactionDate':Date, 'transactionItem':item,
                    'transactionQuantity':Quantity,'transactionAmount'
                    :amount,'transactionType':Type,'transactionTotal':Total})
#...........................

def find_item_by_name(name):

    c.execute("SELECT * FROM Transactions WHERE transactionItem =:transactionItem", {'transactionItem': name})
    search = c.fetchone()
def summary_total():
    c.execute("SELECT * FROM Transactions WHERE transactionTotal = transactionTotal")
    last_trans = float
    search = c.fetchall()
    # ..... TO MAKE SURE TOTAL IS ONLY CALCULATED ONCE .........
    for trans in search[0:]:
        print(trans)
        last = trans[5:]
        for n in last:
            last_trans = n
            break
    return last_trans
#
# find_item_by_name('initial Total')
# l = summary_total()
# print(l)


