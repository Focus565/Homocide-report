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
        if weapon in homocide_in_weapon and weapon != 'Unknown':
            homocide_in_weapon[weapon] += 1
        elif weapon != 'Unknown':
            homocide_in_weapon[weapon] = 1

    weaponkind = sorted(homocide_in_weapon, key=homocide_in_weapon.__getitem__, reverse=True)
    numweapon = sorted(homocide_in_weapon.values(), reverse=True)

    pie_chart = pygal.Pie(style=DarkStyle,title='Homocide in Weapon', x_title='Weapon', inner_radius=.4)
    for i in range(len(weaponkind)):
        pie_chart.add(weaponkind[i], numweapon[i])#in pygal you need to add value to make each pie_chart
    pie_chart.render_to_file('img/weapon.svg')#render it to file
weapon()