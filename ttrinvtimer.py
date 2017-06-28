#!/usr/bin/env python3
import requests
import json
import PyZenity
import regex
import time
import sys

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

def countdown(t):
    while t:
        hours, newt = divmod(t, 3600)
        mins, secs = divmod(newt, 60)
        timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

time_seconds = get_sec(time_split)
#print(time_split)
#print(time_seconds)
countdown(time_seconds)