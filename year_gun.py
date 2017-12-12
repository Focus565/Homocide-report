import pandas as pd
import pygal
from pygal.style import DarkStyle
def read():
    '''use to read file and return as dataframe'''
    file = 'database.csv'
    return pd.read_csv(open(file))

def year():
    '''plot graph of year'''
    data = read()

    homocide_in_year = []
    years = []
    weapons = []
    gun_year = []

    for year in data['Year']:
        homocide_in_year.append(year)


    for weapon in data['Weapon']:
        weapons.append(weapon)

    cout = 0
    for i in homocide_in_year:
        if weapons[cout] in ['Rifle', 'Firearm', 'Shotgun', 'Gun', 'Handgun']:
            gun_year.append(i)
        cout += 1

    for count in range(1980, 2015):
        years.append(gun_year.count(count))

    bar = pygal.Line(style=DarkStyle,title='Homocide in year kill by firearm', \
        show_minor_x_labels=False, x_label_rotation=20)
    bar.x_labels = map(str, range(1980, 2015))
    bar.x_labels_major = ['1980', '1985', '1990', \
    '1995', '2000','2005', '2010', '2014']
    bar.add('Year', Years)
    bar.render_to_file('img/year_Gun.svg')
year()
