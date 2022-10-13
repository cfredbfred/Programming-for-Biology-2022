#!/usr/bin/env python3

import sys

fav_things = {'book' : 'Jitterbug Perfume', 'song' : 'Tom Petty - I wont back down', 'tree' : 'Cedar'}

'''
print(fav_things['book'])

fav_thing = 'book'

print(fav_things[fav_thing])
'''

fav_thing = sys.argv[1]


fav_things[fav_thing] = sys.argv[2]
print(fav_things[fav_thing])

for key in fav_things:
    print(f'{key}\t{fav_things[key]}')
    