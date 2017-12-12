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
    homicide_in_weapon = {} #count
    for weapon in data['Weapon']:
        if weapon in homicide_in_weapon and weapon != 'Unknown':
            homicide_in_weapon[weapon] += 1
        elif weapon != 'Unknown':
            homicide_in_weapon[weapon] = 1

    weaponkind = sorted(homicide_in_weapon, key=homicide_in_weapon.__getitem__, reverse=True)
    numweapon = sorted(homicide_in_weapon.values(), reverse=True)

    pie_chart = pygal.Pie(style=DarkStyle,title='Homicide by Weapons', inner_radius=.4)
    for i in range(len(weaponkind)):
        pie_chart.add(weaponkind[i], numweapon[i])#in pygal you need to add value to make each pie_chart
    pie_chart.render_to_file('docs/img/weapon.svg')#render it to file
weapon()