#!/usr/bin/python

'''
portfolio.py
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

import gobject
import gtk
import guiutils

class Portfolio:
    
    def __init__(self, profile = None):
        self.drawGUI()


    # Dialog to receive transaction input
    def add_transaction(self):
        dialog = gtk.Dialog('Add Transaction', None, gtk.DIALOG_MODAL,
                            (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_ADD,
                                gtk.RESPONSE_ACCEPT))
        dialog.set_position(gtk.WIN_POS_CENTER)
        table = gtk.Table(6,2)

        name_label = gtk.Label('Name')
        name_label.set_alignment(0.90,0.5)
        code_label = gtk.Label('Stock code')
        code_label.set_alignment(0.90,0.5)
        action_label = gtk.Label('Action')
        action_label.set_alignment(0.90,0.5)
        date_label = gtk.Label('Date')
        date_label.set_alignment(0.90,0.5)
        quantity_label = gtk.Label('Quantity')
        quantity_label.set_alignment(0.90,0.5)
        price_label = gtk.Label('Price')
        price_label.set_alignment(0.90,0.5)

        table.attach(name_label, 0,1,0,1)
        table.attach(code_label, 0,1, 1, 2,gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(action_label, 0,1, 2, 3,gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(date_label, 0,1, 3, 4,gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(quantity_label, 0,1, 4, 5,gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(price_label, 0,1, 5, 6,gtk.EXPAND|gtk.FILL, gtk.SHRINK)

        name_entry = gtk.Entry()
        code_entry = gtk.Entry()
        date_selector = guiutils.DateEntry()
        quantity_entry = gtk.Entry()
        price_entry = gtk.Entry()

        combolist = gtk.ListStore(gobject.TYPE_STRING)
        for item in ['Buy', 'Sell']:
            combolist.append([item])
        action_combobox = gtk.ComboBoxEntry(combolist)

        table.attach(name_entry, 1,2,0,1, gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(code_entry, 1,2,1,2, gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(action_combobox, 1,2,2,3, gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(date_selector, 1,2,3,4, gtk.SHRINK)
        table.attach(quantity_entry, 1,2,4,5, gtk.EXPAND|gtk.FILL, gtk.SHRINK)
        table.attach(price_entry, 1,2,5,6, gtk.EXPAND|gtk.FILL, gtk.SHRINK)

        dialog.vbox.pack_start(table)
        dialog.show_all()
        resp = dialog.run()

        if resp == gtk.RESPONSE_CANCEL:
            dialog.destroy()

    # Funcion to generate the GUI
    def drawGUI(self):
        self.win = gtk.Window()
        self.win.set_title('Portfolio')
        self.win.set_default_size(400,200)
        self.win.set_position(gtk.WIN_POS_CENTER)
        self.win.connect('destroy', gtk.main_quit)


        # Set toolbar and toolbuttons
        toolbar = gtk.Toolbar()

        add_toolbutton = gtk.ToolButton(gtk.STOCK_ADD)
        add_toolbutton.set_tooltip_text('Add transaction')
        add_toolbutton.connect('clicked', lambda a: self.add_transaction())

        delete_toolbutton = gtk.ToolButton(gtk.STOCK_DELETE)
        delete_toolbutton.set_tooltip_text('Delete transaction')

        import_toolbutton = gtk.ToolButton(gtk.STOCK_GO_DOWN)
        import_toolbutton.set_label('Import')
        import_toolbutton.set_tooltip_text('Import transaction')

        refresh_toolbutton = gtk.ToolButton(gtk.STOCK_REFRESH)
        refresh_toolbutton.set_tooltip_text('Update portfolio')

        toolbar.insert(refresh_toolbutton, 0)
        toolbar.insert(import_toolbutton, 0)
        toolbar.insert(delete_toolbutton, 0)
        toolbar.insert(add_toolbutton, 0)

        # Create a Liststore object for portfolio table and attach it to Treeview
        self.store = gtk.ListStore(str,str,str,str,str)
        treeview = gtk.TreeView(self.store)
        


        layout = gtk.Table(2, 1)
        layout.attach(toolbar, 0,1,0,1, gtk.FILL|gtk.EXPAND, gtk.SHRINK)

        self.win.add(layout)

        self.win.show_all()
        gtk.main()

if __name__ == '__main__':
    Portfolio()

