"""Make graph victim age"""
import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def age():
    '''plot graph of victim age'''
    data = read()
    victim_age = [0, 0, 0, 0, 0, 0]
    range_age = ['0-11', '12-20', '21-35', '36-50', '51-80', '81-100']
    for age in data['Victim Age']:
        if age <= 11:
            victim_age[0] += 1
        elif age <= 20:
            victim_age[1] += 1
        elif age <= 35:
            victim_age[2] += 1
        elif age <= 50:
            victim_age[3] += 1
        elif age <= 80:
            victim_age[4] += 1
        else:
            victim_age[5] += 1
    bar = pygal.Bar(style=DarkStyle,title='Victim Age', x_title='Age')#make bar graph if you want to make other kind of graph google pygal
    bar.x_labels = ('0-11', '12-20', '21-35', '36-50', '51-80', '81-100')
    bar.add('Casualty', victim_age)#in pygal you need to add value to make each bar
    bar.render_to_file('img/victim_age.svg')#render it to file
age()
