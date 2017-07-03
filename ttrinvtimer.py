#!/usr/bin/env python3
import requests
from multiprocessing import Queue
import json
from get_sec import get_sec
import regex
import time
import sys
import gi
import html
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Pango

# Get list of invasions and import it
r = requests.get('http://api.ttr-invasions.com/json/invasionlist/')
invkeys = r.json()

# Initialize and populate the list for the columns
invlist=[]
for i in invkeys:
    invlist.append((html.unescape(i['invasion_cog']),i['invasion_district'],i['invasion_remaining']))

# Function for the countdown (Credit to dust)
def countdown(t):
    hours, newt = divmod(t, 3600)
    mins, secs = divmod(newt, 60)
    timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
    t -= 1
    return(timeformat)

# The initial invasion selection window
class InvasionSelector(Gtk.Window):

    # Initialize the window
    def __init__(self):
        Gtk.Window.__init__(self, title='TTR Invasion Timer')
        self.set_border_width(10)
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        # Initialize the window element
        self.invasion_liststore = Gtk.ListStore(str, str, str)
        for invasions in invlist:
            self.invasion_liststore.append(list(invasions))

        # Associate each column
        self.treeview = Gtk.TreeView(self.invasion_liststore)
        for i, column_title in enumerate(['Cog', 'District', 'Time Remaining']):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)
            column.set_sort_column_id(i)

        # Initialize the buttons
        self.buttons = list()
        cancelbut = Gtk.Button.new_from_stock(Gtk.STOCK_CANCEL)
        self.buttons.append(cancelbut)
        cancelbut.connect('clicked', Gtk.main_quit)
        okbutton = Gtk.Button.new_from_stock(Gtk.STOCK_OK)
        self.buttons.append(okbutton)
        okbutton.connect('clicked', self.ok_clicked)

        # Attatch the list and the buttons to the window
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach_next_to(self.scrollable_treelist, None, Gtk.PositionType.TOP, 6, 6)
        self.grid.attach(self.buttons[0], 4, 0, 1, 1)
        for i, button in enumerate(self.buttons[1:]):
            self.grid.attach_next_to(button, self.buttons[i], Gtk.PositionType.RIGHT, 1, 1)
        self.grid.set_row_spacing(10)
        self.grid.set_column_spacing(8)
        self.scrollable_treelist.add(self.treeview)

        self.show_all()

    def ok_clicked(self, button):
        model, treeiter = self.treeview.get_selection().get_selected()
        if treeiter != None:
            timeleft = model[treeiter][2]
#            if timeleft != 'Calculating..' or 'Ending soon..':
            self.destroy()
            starttimer(timeleft)
#            else:
#                return

# Function to parse the invasion selected and convert the time to seconds to be used in the countdown function
def starttimer(time):
    if time != 'Calculating..':
        time_split = ':'.join(regex.split(' H | M | s', time)[:-1])
    else:
        return
    time_seconds = get_sec(time_split)

    # Start the countdown dialog, and pass the time with it in time_seconds so we don't need a global
    win = InvasionTimer()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    win.startclocktimer(time_seconds)

# The countdown timer window
class InvasionTimer(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='TTR Invasion Timer')

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.label = Gtk.Label()
        self.label.modify_font(Pango.FontDescription('Impress BT 90'))
        self.box.pack_start(self.label, True, True, 0)

        self.set_keep_above(True)
        self.set_default_size(620, 260)

    # Displays Timer
    def displayclock(self):
        datetimenow = countdown(self.t)
        self.t -= 1
        self.label.set_label(datetimenow)
        return True

    # Initialize Timer
    def startclocktimer(self, time):
        GObject.timeout_add(1000, self.displayclock)
        self.t = time


box = InvasionSelector()
box.connect('delete-event', Gtk.main_quit)
box.show_all()
Gtk.main()

