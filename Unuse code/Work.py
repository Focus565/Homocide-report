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
    for relationship in data['Relationship']:
        if relationship in homicide_in_relationship:
            homicide_in_relationship[relationship] += 1
        elif relationship == 'Employee' or relationship == 'Employer':
            homicide_in_relationship[relationship] = 1

    people = sorted(homicide_in_relationship, key=homicide_in_relationship.__getitem__, reverse=True)
    num = sorted(homicide_in_relationship.values(), reverse=True)

    pie_chart = pygal.Pie(style=DarkStyle,title='homicide in Relationship', x_title='Work', inner_radius=.4)
    for i in range(len(people)):
        pie_chart.add(people[i], num[i])#in pygal you need to add value to make each pie_chart
    pie_chart.render_to_file('docs/img/Work.svg')#render it to file
relationship()