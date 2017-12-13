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
    homicide_in_month = {} #count
    for month in data['Month']:
        if month in homicide_in_month:
            homicide_in_month[month] += 1
        else:
            homicide_in_month[month] = 1
    bar = pygal.Bar(style=DarkStyle,title='homicide in month', x_title='month')#make Bar graph if you want to make other kind of graph google pygal
    for i in homicide_in_month:
        bar.add(str(i), homicide_in_month[i])#in pygal you need to add value to make each bar
    bar.render_to_file('docs/img/month.svg')#render it to file
month()