#!/usr/bin/python


'''
dialogs.py
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
import gobject

import customgui

class DialogFactory:
    
    # Displays a dialog box to collect information in text format. A list of data labels
    # is the argument. The function returns a list of data collected in the same order
    # of labels. Returns False in case of insufficient data
    def get_info_dialog(self, data_labels = [], parent = None, title = 'Input'):
        rows = len(data_labels)
        
        layout = gtk.Table(rows, 2)
        entries = []

        for i in range(rows):
            entries.append(gtk.Entry())

        for i in range(rows):
            layout.attach(gtk.Label(data_labels[i]), 0,1,i, i+1 , gtk.EXPAND|gtk.FILL,
                            gtk.EXPAND|gtk.FILL)
            layout.attach(entries[i], 1, 2, i, i+1, gtk.EXPAND|gtk.FILL,
                            gtk.EXPAND|gtk.FILL)

        data_dialog = gtk.Dialog(title, parent, gtk.DIALOG_MODAL,
                                    (gtk.STOCK_CANCEL,gtk.RESPONSE_REJECT,
                                    gtk.STOCK_OK,gtk.RESPONSE_ACCEPT))
        data_dialog.vbox.pack_start(layout)
        data_dialog.show_all()
        response = data_dialog.run()

        # Return the input if response is 'OK'
        if response == gtk.RESPONSE_ACCEPT:
            data_input = []
            sufficiency = True
            for i in range(rows):
                data_input.append(entries[i].get_text())
                if data_input[i] == '':
                    sufficiency = False
            # check data sufficiency and display warning in case of insufficient data
            if (sufficiency == False):
                warn = gtk.MessageDialog(None,gtk.DIALOG_MODAL,gtk.MESSAGE_WARNING,
                                    gtk.BUTTONS_OK,'Insufficient data. Please try again')
                resp_warn = warn.run()
                if resp_warn == gtk.RESPONSE_OK:
                    warn.destroy()
                    data_dialog.destroy()
                    return False
            else:
                data_dialog.destroy()
                return data_input
        
        else:                       # Response is 'Cancel'
            data_dialog.destroy()
            return False


    # Function to allows user to select and delete an item from a group and returns the modified list
    # Arguments: List of items  to be operated on
    def delete_item(self, title = 'Remove item', parent = None,
                            input_data=[]):
        
        liststore = gtk.ListStore(gobject.TYPE_STRING)
        # Fill in the model
        for item in input_data:
            liststore.append([item])

        view = gtk.TreeView(liststore)
        tree_selection = view.get_selection()
        tree_selection.set_mode(gtk.SELECTION_SINGLE)

        column = gtk.TreeViewColumn()
        view.append_column(column)
        renderer = gtk.CellRendererText()
        column.pack_start(renderer, True)
        column.add_attribute(renderer, 'text', 0)
        

        # GUI to display the whole thing
        dialog = gtk.Dialog(title, parent, gtk.DIALOG_MODAL,(gtk.STOCK_OK,
                            gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
        dialog.vbox.pack_start(view)
        view.show()
        response = dialog.run()
        # get the selected value and return
        if response == gtk.RESPONSE_ACCEPT:
            model, pos = tree_selection.get_selected()
            dialog.destroy()
            item_to_remove = model.get(pos, 0)
            input_data.remove(item_to_remove[0])
            return input_data
        else:
            dialog.destroy()

    # Function to display a dialog with a list from which user can choose items
    def item_choose_dialog(self, title = 'Select item', parent = None, message = '',
                            left_title = None, right_title = None, item_list = []):
        dialog = gtk.Dialog(title, parent, gtk.DIALOG_MODAL, (gtk.STOCK_OK,
                            gtk.RESPONSE_ACCEPT, gtk.STOCK_CANCEL, gtk.RESPONSE_REJECT))
        item_selector = customgui.ItemSelector(item_list, message, left_title, right_title)
        dialog.set_default_size(400,300)
        dialog.vbox.pack_start(item_selector)
        item_selector.show()
        response = dialog.run()
        if response == gtk.RESPONSE_ACCEPT:
            dialog.destroy()
            return item_selector.get_selected_item_group()
        else:
            dialog.destroy()
            return False
if __name__ == '__main__':
    DialogFactory()
