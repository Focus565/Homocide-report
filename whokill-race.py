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
    homocide_in_race = {} #count
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
        if i in homocide_in_race:
            homocide_in_race[i] += 1
        else:
            homocide_in_race[i] = 1

    del homocide_in_race['Asian/Pacific Islander']
    del homocide_in_race['Black']
    del homocide_in_race['White']
    del homocide_in_race['Native American/Alaska Native']
    del homocide_in_race['Unknown']
    
    people = sorted(homocide_in_race, key=homocide_in_race.__getitem__, reverse=True)
    num = sorted(homocide_in_race.values(), reverse=True)

    line = pygal.Pie(style=DarkStyle,title='Homicide compare by Race', x_title='Compare Race', inner_radius=.4, truncate_legend=-1)
    for i in range(len(people)):
        line.add(people[i], num[i])#in pygal you need to add value to make each line
    line.render_to_file('img/whokill-race.svg')#render it to file
race()