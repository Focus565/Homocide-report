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
    for year in data['Year']:
        homocide_in_year.append(year)
    for count in range(1980, 2015):
        years.append(homocide_in_year.count(count))

    bar = pygal.Line(style=DarkStyle,title='Homocide in year', \
        show_minor_x_labels=False, x_label_rotation=20)
    bar.x_labels = map(str, range(1980, 2015))
    bar.x_labels_major = ['1980', '1985', '1990', \
    '1995', '2000','2005', '2010', '2014']
    bar.add('Year', years)
    bar.render_to_file('img/year.svg')
year()
