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

    years = []
    victims = []
    perpetrators = []


    white_white = []
    white_white_year = []

    white_black = []
    white_black_year = []

    white_other = []
    white_other_year = []

    for year in data['Year']:
        years.append(year)
    for i in data['Victim Race']:
        victims.append(i)
    for i in data['Perpetrator Race']:
        perpetrators.append(i)
    print(perpetrators[0:10])

    cout = 0
    for i in years:
        if victims[cout] == 'White' and perpetrators[cout] == 'White':
            white_white.append(i)
        cout += 1

    cout = 0
    for i in years:
        if victims[cout] == 'White' and perpetrators[cout] == 'Black':
            white_black.append(i)
        cout += 1

    cout = 0
    for i in years:
        if victims[cout] == 'White' and perpetrators[cout] in ['Native American/Alaska Native', 'Unknown', 'Asian/Pacific Islander']:
            white_other.append(i)
        cout += 1


    for count in range(1980, 2015):
        white_white_year.append(white_white.count(count))
    for count in range(1980, 2015):
        white_black_year.append(white_black.count(count))
    for count in range(1980, 2015):
        white_other_year.append(white_other.count(count))

    bar = pygal.Line(legend_at_bottom=True,fill=True,style=DarkStyle,title='Homicide in year with race', \
        show_minor_x_labels=False, x_label_rotation=20,truncate_legend=-1)
    bar.x_labels = map(str, range(1980, 2015))
    bar.x_labels_major = ['1980', '1985', '1990', \
    '1995', '2000','2005', '2010', '2014']

    bar.add('White killed by White', white_white_year)
    bar.add('White killed by Black', white_black_year)
    bar.add('White killed by Other', white_other_year)
    bar.render_to_file('docs/img/year_Race.svg')
year()
