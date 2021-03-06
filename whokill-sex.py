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
    homicide_in_relationship = {} #count
    data[(data['Victim Sex'] != 'Unknown') | (data['Perpetrator Sex'] != 'Unknown')]
    data[(data['Victim Sex'] == 'Male') & (data['Perpetrator Sex'] == 'Male')] = 'Male kill Male'
    data[(data['Victim Sex'] == 'Female') & (data['Perpetrator Sex'] == 'Male')] = 'Male kill Female'
    data[(data['Victim Sex'] == 'Male') & (data['Perpetrator Sex'] == 'Female')] = 'Female kill Male'
    data[(data['Victim Sex'] == 'Female') & (data['Perpetrator Sex'] == 'Female')] = 'Female kill Female'

    for i in data['Victim Sex']:
        if i in homicide_in_relationship:
            homicide_in_relationship[i] += 1
        else:
            homicide_in_relationship[i] = 1

    del homicide_in_relationship['Female']
    del homicide_in_relationship['Male']
    del homicide_in_relationship['Unknown']
    
    people = sorted(homicide_in_relationship, key=homicide_in_relationship.__getitem__, reverse=True)
    num = sorted(homicide_in_relationship.values(), reverse=True)

    pie_chart = pygal.Pie(style=DarkStyle,title='Homicide compare by Gender', inner_radius=.4, truncate_legend=-1)
    for i in range(len(people)):
        pie_chart.add(people[i], num[i])#in pygal you need to add value to make each pie_chart
    pie_chart.render_to_file('docs/img/whokill-sex.svg')#render it to file
relationship()