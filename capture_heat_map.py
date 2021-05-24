import plotly.express as px
import chm_function

#!Python3
# Fetches chess games, tallies captures to coordinates, renders a simple ascii capture map.

import re, os, requests, sys
import chm_function as chm

user = ''

if len(sys.argv) > 1:
    user = ' '.join(sys.argv[1:])
else:
    user = input('Enter lichess username:')


response = chm.getGamesFromLichess(user)


if response.status_code == 200:
    chm.write_games(response, user)
else:
    print(str(response.status_code) + " account not found. Try again.")
    exit()


g = open(user + '.pgn', 'r')
games = g.read()

# gets a list of captures from games
captures = chm.captureFinder(games)

g.close()


# Shortened variable name to simplify the displayboard 
x = chm.captureCounter(captures)


# There must be a more elegant way to display this data
displayBoard = f'''
8  {x['a8']} {x['b8']} {x['c8']} {x['d8']} {x['e8']} {x['f8']} {x['g8']} {x['h8']}
7  {x['a7']} {x['b7']} {x['c7']} {x['d7']} {x['e7']} {x['f7']} {x['g7']} {x['h7']}
6  {x['a6']} {x['b6']} {x['c6']} {x['d6']} {x['e6']} {x['f6']} {x['g6']} {x['h6']}
5  {x['a5']} {x['b5']} {x['c5']} {x['d5']} {x['e5']} {x['f5']} {x['g5']} {x['h5']}
4  {x['a4']} {x['b4']} {x['c4']} {x['d4']} {x['e4']} {x['f4']} {x['g4']} {x['h4']}
3  {x['a3']} {x['b3']} {x['c3']} {x['d3']} {x['e3']} {x['f3']} {x['g3']} {x['h3']}
2  {x['a2']} {x['b2']} {x['c2']} {x['d2']} {x['e2']} {x['f2']} {x['g2']} {x['h2']}
1  {x['a1']} {x['b1']} {x['c1']} {x['d1']} {x['e1']} {x['f1']} {x['g1']} {x['h1']}
   A B C D E F G H
'''

if captures == None:
    print('No captures found')
else:
    print(f'Total Captures Found: {len(captures)}')
    print(displayBoard)



data = chm_function.captureCounter(captures)

graph_data = list(data.values())
df = []

#I have a list with 64 values that need to be split into 8 lists with 8 values each.
df = [graph_data[x:x+8] for x in range(0, len(graph_data), 8)]
    

fig = px.imshow(df,
        labels=dict(x='columns', y = 'rows',),
        x=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        y=['8', '7', '6', '5', '4', '3', '2', '1'],
        title=f'Account: {user} -- Total Captures: {len(captures)}',
        color_continuous_scale= 'thermal'
) 

fig.show()