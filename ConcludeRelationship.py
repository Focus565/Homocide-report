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
    data = data[data['Relationship'] != 'Unknown']
    data = data[data['Relationship'] != 'Boyfriend/Girlfriend']
    data[(data['Relationship'] == 'Employee') | (data['Relationship'] == 'Employer')] = 'Work'
    data[(data['Relationship'] == 'Father') | (data['Relationship'] == 'Mother') | (data['Relationship'] == 'Stepmother') | (data['Relationship'] == 'Stepfather')] = 'Parent'
    data[(data['Relationship'] == 'Husband') | (data['Relationship'] == 'Boyfriend') | (data['Relationship'] == 'Ex-Husband') | (data['Relationship'] == 'Common-Law Husband')] = 'MalePartner'
    data[(data['Relationship'] == 'Wife') | (data['Relationship'] == 'Girlfriend') | (data['Relationship'] == 'Ex-Wife') | (data['Relationship'] == 'Common-Law Wife')] = 'FemalePartner'
    print(data['Relationship'].unique())
    for i in data['Relationship']:
        if i in homocide_in_relationship:
            homocide_in_relationship[i] += 1
        else:
            homocide_in_relationship[i] = 1

    people = sorted(homocide_in_relationship, key=homocide_in_relationship.__getitem__, reverse=True)
    num = sorted(homocide_in_relationship.values(), reverse=True)

    bar = pygal.Bar(style=DarkStyle,title='Homicide in Relationship', x_title='Relationship')
    for i in range(len(people)):
        bar.add(people[i], num[i])#in pygal you need to add value to make each bar
    bar.render_to_file('img/ConcludeRelationship.svg')#render it to file
relationship()