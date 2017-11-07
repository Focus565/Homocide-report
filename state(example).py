import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def state():
    '''plot graph of state'''
    data = read()
    homocide_in_state = {} #count
    for state in data['State']:
        if state in homocide_in_state:
            homocide_in_state[state] += 1
        else:
            homocide_in_state[state] = 1
    bar = pygal.Bar(style=DarkStyle,title='Homocide in state', x_title='State')#make Bar graph if you want to make other kind of graph google pygal
    for i in homocide_in_state:
        bar.add(i, homocide_in_state[i])#in pygal you need to add value to make each bar
    bar.render_to_file('img/state.svg')#render it to file
state()