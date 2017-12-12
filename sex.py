import pandas as pd
import pygal
from pygal.style import DarkStyle
def main():
    data = pd.read_csv(open('database.csv'))
    bar = pygal.Pie(style=DarkStyle)
    dic = {}
    for i in data['Victim Sex']:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    bar.title = 'Sex'
    for i in dic:
        bar.add(i, dic[i])
    bar.render_to_file('docs/img/sex.svg')
main()
