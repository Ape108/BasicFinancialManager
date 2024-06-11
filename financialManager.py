
import csv
import gspread
import time

MONTH = '2024-06'

file = fr"C:\Users\Balmy\Python Projects\FinancialManager\usbank_{MONTH}.csv"

transactions = []

def usbankFin(file):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[2]
            amount = float(row[4])
            transaction = ((date, name, amount))
            print(transaction)
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = usbankFin(file)

for row in rows:
    if row[1][:len("DEBIT PURCHASE -VISA")] == "DEBIT PURCHASE -VISA":
        wks.insert_row([row[0], row[1][len("DEBIT PURCHASE -VISA")+1:], row[2]], 8)
        time.sleep(2)
    else:
        wks.insert_row([row[0], row[1], row[2]], 8)
        time.sleep(2)


