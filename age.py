import pandas as pd
import pygal
from pygal.style import DarkStyle
def main():
    data = pd.read_csv(open('database.csv'))
    bar = pygal.Bar(style=DarkStyle)
    perpetrator_age = [0, 0, 0, 0, 0, 0]
    range_age = ['0-11', '12-20', '21-35', '36-50', '51-80', '81-100']
    row = 0
    data.columns = [col.replace(" ", "") for col in data.columns]
    data.dropna(axis=0)
    data.PerpetratorAge = pd.to_numeric(data.PerpetratorAge, errors='coerec')
    dfs = data['PerpetratorAge'].dropna(axis=0)
    for age in dfs:
        if age <= 11 and age > 0:
            perpetrator_age[0] += 1
        elif age <= 20:
            perpetrator_age[1] += 1
        elif age <= 35:
            perpetrator_age[2] += 1
        elif age <= 50:
            perpetrator_age[3] += 1
        elif age <= 80:
            perpetrator_age[4] += 1
        else:
            perpetrator_age[5] += 1
    bar.title = 'Perpetrator Age'
    bar.x_title = 'Age'
    bar.x_labels = ('0-11', '12-20', '21-35', '36-50', '51-80', '81-100')
    bar.add('Incident', perpetrator_age)
    bar.render_to_file('docs/img/age.svg')
main()
