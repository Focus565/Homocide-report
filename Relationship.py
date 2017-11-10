import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def relationship():
    '''plot graph of relationship'''
    data = read()
    homocide_in_relationship = {} #count
    for relationship in data['Relationship']:
        if relationship in homocide_in_relationship:
            homocide_in_relationship[relationship] += 1
        else:
            homocide_in_relationship[relationship] = 1
    bar = pygal.Bar(style=DarkStyle,title='Homocide in Relationship', x_title='Relationship')
    for i in homocide_in_relationship:
        bar.add(i, homocide_in_relationship[i])#in pygal you need to add value to make each bar
    bar.render_to_file('img/relationship.svg')#render it to file
relationship()