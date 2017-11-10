import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def weapon():
    '''plot graph of weapon'''
    data = read()
    homocide_in_weapon = {} #count
    for weapon in data['Weapon']:
        if weapon in homocide_in_weapon:
            homocide_in_weapon[weapon] += 1
        else:
            homocide_in_weapon[weapon] = 1
    pie_chart = pygal.Pie(style=DarkStyle,title='Homocide in Weapon', x_title='Weapon', inner_radius=.4)
    for i in homocide_in_weapon:
        pie_chart.add(i, homocide_in_weapon[i])#in pygal you need to add value to make each pie_chart
    pie_chart.render_to_file('img/weapon.svg')#render it to file
weapon()