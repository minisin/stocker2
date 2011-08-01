#!/usr/bin/python

import csv
import datetime

class Portfolio:
    def __init__(self):
        self.buy_trns = []  # List of all buy trans(date,stock,trn_type, qty, price)
        self.sell_trns = [] # List of all sell trans(date,stock,trn_type, qty, price)

    '''
    Function to read the transactin file and create  lists of tuples
    containing the buys and sells separately. Returns data in the format
    (transaction_date,stock,transaction_type,quantity); returns 0 in case
    of error, 1 in case of successful read
    '''
    def read_transactions(self, transaction_file = None):
        try:
            f = open(transaction_file, 'rb')
        except IOError:
            print 'Error: Could not open file'
            return 0
        csv_read = csv.reader(f)
        len = 1
        for row in csv_read:
            if len != 1:                #avoid reading header columns
                date_string = row[0].split('-')
                trn_date = datetime.date(int(date_string[0]),
                        int(date_string[1]),int(date_string[2]))
                if row[2] == 'B':
                    self.buy_trns.append((trn_date,row[1],row[2],row[3], row[4]))
                elif row[2] == 'S':
                    self.sell_trns.append((trn_date,row[1],row[2],row[3], row[4]))
            len = len + 1
        return 1


    '''
    Function to calculate the capital gains and generate data in tabular form
    '''
    def get_capgain(self, stock_code):
        # do a sort of both buy and sell data before taking up this
        # separate code required here
        for sale in self.sell_trns:
            if sale[1] == stock_code:
                sale_date = sale[0]
                sale_quantity = sale[3]
                sale_price = sale[4]
                print sale_date, sale_quantity, sale_price

            else:
                return False


    def display_buys(self):
        for row in self.buy_trns:
            print row

    def display_sells(self):
        for row in self.sell_trns:
            print row
