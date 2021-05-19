#!Python3
# Fetches chess games, tallies captures to coordinates, renders a simple ascii capture map.

import re, os, requests


def getGamesFromLichess(data):
    BASE_URL = 'https://lichess.org/api/games/user/'
    response = requests.get(BASE_URL + data)

    if response.status_code == 200:
        file = open('games.pgn', 'wb')
        file.write(response.content)
        file.close
    else:
        print(response.status_code)


def captureFinder(data):
    captureRegex = re.compile(r'(x([a-hA-H][1-8]))', re.VERBOSE)

    for groups in captureRegex.findall(data):
        captures.append(groups[1])


def captureCounter(data):
    for capture in data:
        captureCounts[capture] += 1


# Flow
captures = []
user = ''

user = input('Enter lichess username:')
getGamesFromLichess(user)

g = open('games.pgn', 'r')
games = g.read()


captureFinder(games)
g.close()

# There must be a more elegant way to store this data
captureCounts = {
    "a8": 0, "b8": 0, "c8": 0, "d8": 0, "e8": 0, "f8":0, "g8": 0, "h8": 0,
    "a7": 0, "b7": 0, "c7": 0, "d7": 0, "e7": 0, "f7":0, "g7": 0, "h7": 0,
    "a6": 0, "b6": 0, "c6": 0, "d6": 0, "e6": 0, "f6":0, "g6": 0, "h6": 0,
    "a5": 0, "b5": 0, "c5": 0, "d5": 0, "e5": 0, "f5":0, "g5": 0, "h5": 0,
    "a4": 0, "b4": 0, "c4": 0, "d4": 0, "e4": 0, "f4":0, "g4": 0, "h4": 0,
    "a3": 0, "b3": 0, "c3": 0, "d3": 0, "e3": 0, "f3":0, "g3": 0, "h3": 0,
    "a2": 0, "b2": 0, "c2": 0, "d2": 0, "e2": 0, "f2":0, "g2": 0, "h2": 0,
    "a1": 0, "b1": 0, "c1": 0, "d1": 0, "e1": 0, "f1":0, "g1": 0, "h1": 0
}

captureCounter(captures)


# Shortened variable name to simplify the displayboard 
x = captureCounts

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
