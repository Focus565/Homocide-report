import pandas as pd
import pygal
def main():

    data = pd.read_csv(open('database.csv'))
    bar = pygal.Pie()
    dic = {}
    for i in data['Victim Sex']:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    bar.title = 'psit in %'
    for i in dic:
        bar.add(i, dic[i])
    bar.render_to_file('docs/img/stuff.svg')
main()
