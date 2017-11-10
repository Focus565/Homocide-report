"""Make graph victim sex"""
import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def sex():
    '''plot graph of victim sex'''
    data = read()
    victim_sex = {}#count
    for sex in data['Victim Sex']:
        if sex in victim_sex:
            victim_sex[sex] += 1
        else:
            victim_sex[sex] = 1
    pie = pygal.Pie(style=DarkStyle,title='Victim Sex', x_title='Victim Sex')#make pie graph if you want to make other kind of graph google pygal
    for i in victim_sex:
        pie.add(i, victim_sex[i])#in pygal you need to add value to make each pie
    pie.render_to_file('img/victim_sex.svg')#render it to file
sex()
