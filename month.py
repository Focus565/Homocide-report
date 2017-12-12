import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def month():
    """plot graph of month"""
    data = read()
    homocide_in_month = {} #count
    for month in data['Month']:
        if month in homocide_in_month:
            homocide_in_month[month] += 1
        else:
            homocide_in_month[month] = 1
    bar = pygal.Bar(style=DarkStyle,title='Homocide in month', x_title='month')#make Bar graph if you want to make other kind of graph google pygal
    for i in homocide_in_month:
        bar.add(str(i), homocide_in_month[i])#in pygal you need to add value to make each bar
    bar.render_to_file('img/month.svg')#render it to file
month()