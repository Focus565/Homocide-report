import pandas as pd
import pygal
data = pd.read_csv(open('database.csv'))
bar = pygal.Pie()
dic = {}
for i in data['Victim Race']:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
bar.title = 'Victim Race in %'
for i in dic:
    bar.add(i, dic[i])
bar.render_to_file('img/victim race.svg')
