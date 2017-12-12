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
    homicide_in_state = {} #count
    for state in data['State']:
        if state in homicide_in_state:
            homicide_in_state[state] += 1
        else:
            homicide_in_state[state] = 1
    people = sorted(homicide_in_state, key=homicide_in_state.__getitem__, reverse=True)
    num = sorted(homicide_in_state.values(), reverse=True)
    bar = pygal.Bar(legend_at_bottom=True, style=DarkStyle, title='homicide in state', x_title='State')#make Bar graph if you want to make other kind of graph google pygal
    for i in range(len(people)):
        bar.add(people[i], num[i])#in pygal you need to add value to make each bar
    bar.render_to_file('docs/img/state.svg')#render it to file
state()