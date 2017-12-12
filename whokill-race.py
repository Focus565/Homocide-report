import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def race():
    '''plot graph of race'''
    data = read()
    homicide_in_race = {} #count
    data[(data['Victim Race'] != 'Unknown') | (data['Perpetrator Race'] != 'Unknown')]

    data[(data['Victim Race'] == 'Asian/Pacific Islander') & (data['Perpetrator Race'] == 'Asian/Pacific Islander')] = 'Asian/Pacific Islander kill Asian/Pacific Islander'
    data[(data['Victim Race'] == 'Black') & (data['Perpetrator Race'] == 'Asian/Pacific Islander')] = 'Asian/Pacific Islander kill Black'
    data[(data['Victim Race'] == 'White') & (data['Perpetrator Race'] == 'Asian/Pacific Islander')] = 'Asian/Pacific Islander kill White'
    data[(data['Victim Race'] == 'Native American/Alaska Native') & (data['Perpetrator Race'] == 'Asian/Pacific Islander')] = 'Asian/Pacific Islander kill Native American/Alaska Native'

    data[(data['Victim Race'] == 'Asian/Pacific Islander') & (data['Perpetrator Race'] == 'Black')] = 'Black kill Asian/Pacific Islander'
    data[(data['Victim Race'] == 'Black') & (data['Perpetrator Race'] == 'Black')] = 'Black kill Black'
    data[(data['Victim Race'] == 'White') & (data['Perpetrator Race'] == 'Black')] = 'Black kill White'
    data[(data['Victim Race'] == 'Native American/Alaska Native') & (data['Perpetrator Race'] == 'Black')] = 'Black kill Native American/Alaska Native'

    data[(data['Victim Race'] == 'Asian/Pacific Islander') & (data['Perpetrator Race'] == 'White')] = 'White kill Asian/Pacific Islander'
    data[(data['Victim Race'] == 'Black') & (data['Perpetrator Race'] == 'White')] = 'White kill Black'
    data[(data['Victim Race'] == 'White') & (data['Perpetrator Race'] == 'White')] = 'White kill White'
    data[(data['Victim Race'] == 'Native American/Alaska Native') & (data['Perpetrator Race'] == 'White')] = 'White kill Native American/Alaska Native'

    data[(data['Victim Race'] == 'Asian/Pacific Islander') & (data['Perpetrator Race'] == 'Native American/Alaska Native')] = 'Native American/Alaska Native kill Asian/Pacific Islander'
    data[(data['Victim Race'] == 'Black') & (data['Perpetrator Race'] == 'Native American/Alaska Native')] = 'Native American/Alaska Native kill Black'
    data[(data['Victim Race'] == 'White') & (data['Perpetrator Race'] == 'Native American/Alaska Native')] = 'Native American/Alaska Native kill White'
    data[(data['Victim Race'] == 'Native American/Alaska Native') & (data['Perpetrator Race'] == 'Native American/Alaska Native')] = 'Native American/Alaska Native kill Native American/Alaska Native'

    for i in data['Victim Race']:
        if i in homicide_in_race:
            homicide_in_race[i] += 1
        else:
            homicide_in_race[i] = 1

    del homicide_in_race['Asian/Pacific Islander']
    del homicide_in_race['Black']
    del homicide_in_race['White']
    del homicide_in_race['Native American/Alaska Native']
    del homicide_in_race['Unknown']
    
    people = sorted(homicide_in_race, key=homicide_in_race.__getitem__, reverse=True)
    num = sorted(homicide_in_race.values(), reverse=True)

    bar = pygal.Bar(style=DarkStyle,title='Homicide compare by Race', inner_radius=.4, truncate_legend=-1)
    for i in range(len(people)):
        bar.add(people[i], num[i])#in pygal you need to add value to make each bar
    bar.render_to_file('docs/img/whokill-race.svg')#render it to file
race()