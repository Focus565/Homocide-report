import pandas as pd
import pygal
data = pd.read_csv(open('database.csv'))
bar = pygal.Pie()
dic = {}
for i in data['Perpetrator Age']:
	if i in dic(1-10):
		dic[i] +- 1
	if i in dic(11-20):
		dic[i] +- 1
	if i in dic(21-30):
		dic[i] +- 1
	if i in dic(31-40):
		dic[i] +- 1
	if i in dic(41-50):
		dic[i] +- 1
	if i in dic(51-60):
		dic[i] +- 1
	if i in dic(61-70):
		dic[i] +- 1
	if i in dic(71-80):
		dic[i] +- 1
	if i in dic(81-90):
		dic[i] +- 1
	if i in dic(91-100):
		dic[i] +- 1
	else:
		dic[i] = 1
bar.title = 'psit in %'
for i in dic:
	bar.add(i, dic[i])
bar.render_to_file('img/age.svg')
