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
    knife_year = []
    cout_knife_year = []
    blunt = []
    blunt_year = []
    strangu_suffo = []
    strangu_suffo_year = []
    fire = []
    fire_year = []
    other = []
    other_year = []


    for year in data['Year']:
        homocide_in_year.append(year)
    for weapon in data['Weapon']:
        weapons.append(weapon)
    cout = 0
    for i in homocide_in_year:
        if weapons[cout] in ['Rifle', 'Firearm', 'Shotgun', 'Gun', 'Handgun']:
            gun_year.append(i)
        cout += 1
    cout = 0
    for i in homocide_in_year:
        if weapons[cout] == 'Knife':
            knife_year.append(i)
        cout += 1
    cout = 0
    for i in homocide_in_year:
        if weapons[cout] == 'Blunt Object':
            blunt.append(i)
        cout += 1
    cout = 0
    for i in homocide_in_year:
        if weapons[cout] in ['Strangulation', 'Suffocation', 'Drowning']:
            strangu_suffo.append(i)
        cout += 1
    cout = 0
    for i in homocide_in_year:
        if weapons[cout] == 'Fire':
            fire.append(i)
        cout += 1
    cout = 0
    for i in homocide_in_year:
        if weapons[cout] in ['Drugs', 'Explosives', 'Poison', 'Fall']:
            other.append(i)
        cout += 1

    for count in range(1980, 2015):
        years.append(gun_year.count(count))
    for count in range(1980, 2015):
        cout_knife_year.append(knife_year.count(count))
    for count in range(1980, 2015):
        blunt_year.append(blunt.count(count))
    for count in range(1980, 2015):
        strangu_suffo_year.append(strangu_suffo.count(count))
    for count in range(1980, 2015):
        fire_year.append(fire.count(count))
    for count in range(1980, 2015):
        other_year.append(other.count(count))

    bar = pygal.Line(legend_at_bottom=True,fill=True,style=DarkStyle,title='Homicide by Weapons in years', \
        show_minor_x_labels=False, x_label_rotation=20,truncate_legend=-1)
    bar.x_labels = map(str, range(1980, 2015))
    bar.x_labels_major = ['1980', '1985', '1990', \
    '1995', '2000','2005', '2010', '2014']
    bar.add('Firearm', years)
    bar.add('Knife', cout_knife_year)
    bar.add('Blunt Object', blunt_year)
    bar.add('Strangulation or Suffocation', strangu_suffo_year)
    bar.add('Fire', fire_year)
    bar.add('Others', other_year)
    bar.render_to_file('img/year_Weapon.svg')
year()
