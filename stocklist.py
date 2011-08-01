#!/usr/bin/python

'''
stocklist.py
Copyright (C) 2011 Pradeep Balan Pillai

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
'''

import pickle

class StockList:
    def __init__(self):
        pass

    # Function initiates a stock list in case the list is empty
    def initiate_stock_list(self):
        f = open('stock_list', 'wb')
        pickle.dump({}, f)
        f.close()

    # Add a stock to the list; 
    # argument must be a dictionary in a tuple in the form (stock_code, display name)
    def append_stock(self, stock):
        pickled_list = {}
        # Get the existing list; initiate the list if it is empty
        try:
            file1 = open('stock_list','rb')
            pickled_list = pickle.load(file1)
            file1.close()
        except EOFError:
            file1.close()
            self.initiate_stock_list()
        # update the existing list by adding new data
        file2 = open('stock_list','wb')
        pickled_list[stock[0]] = stock[1]
        pickle.dump(pickled_list, file2)
        file2.close()

    # Delete stocks from the list. The key of dictionary entry corresponding to the stock
    # to be deleted must be passed as an argument
    def delete_stocks(self, stock_keys = []):
        try:
            f = open('stock_list', 'rb')
            pickled_list = pickle.load(f)
            f.close()
            for key in stock_keys:
                del pickled_list[key]
            
            f = open('stock_list', 'wb')
            pickle.dump(pickled_list, f)
            f.close()
            return True
        except EOFError:
            f.close()
            return False

    # Return a list of stocks from the pickled file
    def get_stocklist(self):
        try:
            file = open('stock_list','rb')
            stocklist = pickle.load(file)
            file.close()
        except EOFError:
            return {'Error':'No data available'}
        return stocklist

    # Function validated the individual stock code for correctness.
    # Stock code in string format shall be passed as an argument.
    def validate_stock(self, stock_code):
        pass

