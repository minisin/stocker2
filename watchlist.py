#!/usr/bin/python

'''
watchlist.py
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


import gtk
import pickle


class Watchlist:
    def __init__(self):
        self.tickers = []

	# Load the tickers from pickled list of stocks 
    def load_tickers(self):
        ticker_file = open('ticker_list', 'rb')
        if(ticker_file.readlines() == []):  # Check whether the file contains data
            ticker_file.close()             # else add data before initiating
            self.add_stock()
            ticker_file = open('ticker_list','rb')
            self.tickers = pickle.load(ticker_file)
        else:
            ticker_file = open('ticker_list','rb')
            self.tickers = pickle.load(ticker_file)
        ticker_file.close()

    
    # Add stocks to watchlist. Argument should be pair of display_name:stock_code dictionary
    def add_stocks(self, stocks = {}):
        pickled_stocks = {}
        f = open('watch_list', 'rb')    # Load existing watchlist add new stocks and write 
        try:
            pickled_stocks = pickle.load(f)
            f.close()
            for key in stocks.keys():
                pickled_stocks[key] = stocks[key]
            f = open('watch_list', 'wb')
            pickle.dump(pickled_stocks, f)
            f.close()
        except EOFError:
            f.close()
            return 0 


        

