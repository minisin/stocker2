#!/usr/bin/python

'''
customgui.py
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
# This widget allows visual selection of individual item from a list of items and returns the list of selected items

import gtk
import gobject

class ItemSelector(gtk.Table):
    def __init__(self, group = [], message = '', left_title = None,
                 right_title = None):
        gtk.Table.__init__(self, 5,3)
        #convert non-strings in the list to strings
        self.item_group = []
        for item in group:
            self.item_group.append(str(item))
        self.deleted_group = []
        self.left_title = left_title
        self.right_title = right_title
        self.user_message = message
        self.create_selector(self.item_group) 

    # Set the list of input items
    def set_item_group(self, group = []):
        self.item_group = []
        for item in group:
            self.item_group.append(str(item))
        self.liststore1.clear()
        for item in self.item_group:
            self.liststore1.append([str(item)])

    def create_selector(self, group):

        # Create the message area and display the message
        message_label = gtk.Label(self.user_message)

        # create left pane content
        # add list index as another column in the treemodel for item reference,
        # but do not display it
        self.liststore1 = gtk.ListStore(gobject.TYPE_STRING)
        for item in self.item_group:
            self.liststore1.append([item])
        leftview = gtk.TreeView(self.liststore1)
        leftview.set_headers_visible(False)
        self.left_selector = leftview.get_selection()
        self.left_selector.set_mode(gtk.SELECTION_SINGLE)
        column1 = gtk.TreeViewColumn()
        leftview.append_column(column1)
        renderer1 = gtk.CellRendererText()
        column1.pack_start(renderer1, True)
        column1.add_attribute(renderer1, 'text', 0)
        scroll_1 = gtk.ScrolledWindow()
        scroll_1.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll_1.add(leftview)
        frame1 = gtk.Frame(self.left_title)
        frame1.add(scroll_1)
        
        # create control buttons
        move_right_button = gtk.Button(label = '>>')
        move_right_button.connect('clicked', lambda c: self.move_item_right())
        move_left_button = gtk.Button(label = '<<')
        move_left_button.connect('clicked', lambda c: self.move_item_left())

        # create right pane content
        self.liststore2 = gtk.ListStore(gobject.TYPE_STRING)
        rightview = gtk.TreeView(self.liststore2)
        rightview.set_headers_visible(False)
        self.right_selector = rightview.get_selection()
        self.right_selector.set_mode(gtk.SELECTION_SINGLE)
        column2 = gtk.TreeViewColumn()
        rightview.append_column(column2)
        renderer2 = gtk.CellRendererText()
        column2.pack_start(renderer2, True)
        column2.add_attribute(renderer2, 'text', 0)
        scroll_2 = gtk.ScrolledWindow()
        scroll_2.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll_2.add(rightview)
        frame2 = gtk.Frame(self.right_title)
        frame2.add(scroll_2)

        # Add components to layout and display them
        self.attach(message_label, 0,3,0,1, gtk.EXPAND|gtk.FILL,
                        gtk.EXPAND|gtk.FILL)
        message_label.show()
        self.attach(frame1, 0,1,1,5, gtk.EXPAND|gtk.FILL,
                        gtk.EXPAND|gtk.FILL, 5, 5)
        self.attach(move_right_button, 1,2,2,3, gtk.SHRINK, gtk.SHRINK,5,5)
        self.attach(move_left_button, 1,2,3,4, gtk.SHRINK, gtk.SHRINK,5,5)
        self.attach(frame2, 2,3,1,5, gtk.EXPAND|gtk.FILL,
                        gtk.EXPAND|gtk.FILL,5,5)

    # Callback funcion for move_right button
    def move_item_right(self):
        model, pos = self.left_selector.get_selected()
        if pos != None:
            selected_item = (model.get_value(pos, 0))

            self.deleted_group.append(selected_item)
            self.liststore2.clear()
            for item in self.deleted_group:
                self.liststore2.append([item])

            self.item_group.remove(selected_item)
            self.liststore1.clear()
            for item in self.item_group:
                self.liststore1.append([item])

    # Callback function for move_left button
    def move_item_left(self):
        model, pos = self.right_selector.get_selected()
        if pos != None:
            selected_item = model.get_value(pos, 0)

            self.deleted_group.remove(selected_item)
            self.liststore2.clear()
            for item in self.deleted_group:
                self.liststore2.append([item])

            self.item_group.append(selected_item)
            self.liststore1.clear()
            for item in self.item_group:
                self.liststore1.append([item])

    # Function to fetch the modified list
    def get_selected_item_group(self):
        return self.deleted_group

    # Function to show all the components
    def show(self):
        self.show_all()
