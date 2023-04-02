import plotly.express as px
import chm_function

#!Python3
# Fetches chess games, tallies captures to coordinates, renders a simple ascii capture map.

import re, os, requests, sys
import chm_function as chm


def make_heatmap(user, search_data, search_title):
    # Shortened variable name to simplify the display board
    x = chm.captureCounter(search_data)

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

    if search_data is None:
        print(f'No {search_title} found')
    else:
        print(f'Total {search_title} Found: {len(search_data)}')
        print(displayBoard)

    data = chm_function.captureCounter(search_data)

    graph_data = list(data.values())

    # I have a list with 64 values that need to be split into 8 lists with 8 values each.
    df = [graph_data[x:x + 8] for x in range(0, len(graph_data), 8)]

    fig = px.imshow(df,
                    labels=dict(x='columns', y='rows', ),
                    x=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                    y=['8', '7', '6', '5', '4', '3', '2', '1'],
                    title=f'Account: {user} -- Total {search_title}: {len(search_data)}',
                    color_continuous_scale='thermal'
                    )

    if not os.path.exists("Images"):
        os.mkdir("Images")
    if not os.path.exists(f"Images/{user}"):
        os.mkdir(f"Images/{user}")

    fig.write_image(f'Images/{user}/{search_title}_heat_map_{user}.png')


def main():
    users = input("Enter usernames separated by commas(,): ").split(",")
    for user in users:
        user = user.strip()
        if not os.path.exists(f'{user}.pgn'):
            response = chm.getGamesFromLichess(user)
            if response.status_code == 200:
                chm.write_games(response, user)
            else:
                print(str(response.status_code) + " account not found. Try again.")
                break

        for match_option in ['c', 'm']:
            with open(f'{user}.pgn', 'r') as g:
                games = g.read()

                if match_option == 'c':
                    search_data = chm.captureFinder(games)
                    search_title = 'Captures'
                else:
                    search_data = chm.mateFinder(games)
                    search_title = 'Checkmates'

                make_heatmap(user, search_data, search_title)


if __name__ == "__main__":
    main()