#!/usr/bin/env python3
import requests
import json
import PyZenity
import regex


r = requests.get('http://api.ttr-invasions.com/json/invasionlist/')
invkeys = r.json()
invlist=[]
for i in invkeys:
    invlist.append([i['invasion_cog'],i['invasion_district'],i['invasion_remaining']])
chosen_invasion = PyZenity.List(['Invasions','District','Time Left'],data=invlist, title='TTR Invasion Timer', width=500, height=220)
chosen_string = ''.join(chosen_invasion)
for key in invkeys:
    if key['invasion_cog'] == chosen_string:
        print(key['invasion_remaining'])
