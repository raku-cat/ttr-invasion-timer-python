#!/usr/bin/env python3
import requests
import json
import PyZenity
import regex
import time
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, Pango

r = requests.get('http://api.ttr-invasions.com/json/invasionlist/')
invkeys = r.json()
invlist=[]
for i in invkeys:
    invlist.append([i['invasion_cog'],i['invasion_district'],i['invasion_remaining']])
chosen_invasion = PyZenity.List(['Invasions','District','Time Left'],data=invlist, title='TTR Invasion Timer', width=500, height=220, select_col='1,2')
try:
    chosen_cog, chosen_dist = chosen_invasion
except TypeError:
    sys.exit(0)

for key in invkeys:
    if key['invasion_cog'] == chosen_cog:
        if key['invasion_district'] == chosen_dist:
            chosen_time = key['invasion_remaining']
#print(chosen_time)
#if chosen_time == 'Calculating'
time_split = ':'.join(regex.split(' H | M | s', chosen_time)[:-1])
#print(time_split)
def get_sec(time_str):
    try:
        h, m, s = time_str.split(':')
    except ValueError:
        try:
            m, s = time_str.split(':')
            h = '0'
        except ValueError:
            s = time_str
            h = '0'
            m = '0'
    return int(h) * 3600 + int(m) * 60 + int(s)

time_seconds = get_sec(time_split)

def countdown(t):
    hours, newt = divmod(t, 3600)
    mins, secs = divmod(newt, 60)
    timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
    t -= 1
    return(timeformat)

class MainWindow(Gtk.Window):
    t = time_seconds
    def __init__(self):
        Gtk.Window.__init__(self, title="TTR Invasion Timer")

        self.box = Gtk.Box(spacing=6)
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
    def startclocktimer(self):
        GObject.timeout_add(1000, self.displayclock)


win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
win.startclocktimer()
Gtk.main()
