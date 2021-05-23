import plotly.express as px
import acm_function


captures = ['c3', 'a8', 'c4', 'e4', 'e3', 'a2', 'a2', 'b4', 'g3', 'h2', 'f3']

data = acm_function.captureCounter(captures)


graph_data = list(data.values())
df = []



#I have a list with 64 values that need to be split into 8 lists with 8 values each.
df = [graph_data[x:x+8] for x in range(0, len(graph_data), 8)]
    

'''
data = [[1 , 2, 3, 4, 5, 6, 7, 9],
        [23, 4, 5, 3, 6, 3,22,55],
        [10,40,50, 1,89,99,60, 3],
        [12,32,34,56,43,23,67,12],
        [1 , 2, 3, 4, 5, 6, 7, 9],
        [23, 4, 5, 3, 6, 3,22,55],
        [10,40,50, 1,89,99,60, 3],
        [12,32,34,56,43,23,67,12],
    ]
'''

fig = px.imshow(df,
        labels=dict(x='columns', y = 'rows'),
        x=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        y=['8', '7', '6', '5', '4', '3', '2', '1']
) 

fig.show()