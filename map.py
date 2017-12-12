import pandas as pd
import plotly.offline as offline
import plotly.graph_objs as go
def state():
    data = pd.read_csv('database.csv')
    state_to_code = { "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Northern Mariana Islands": "MP", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Palau": "PW", "Pennsylvania": "PA", "Puerto Rico": "PR", "Rhodes Island": "RI", "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virgin Islands": "VI", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"}
    code = []
    for i in data['State']:
        code.append(state_to_code[i])
    data['State Code'] = code
    count = {}
    for i in data['State']:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    trc = dict(type='choropleth', text = data['State'].unique(), locations = data['State Code'].unique(), locationmode = 'USA-states', colorscale = 'Reds', z = list(count.values()))
    lyt = dict(geo = dict(scope='usa'))
    mapping = go.Figure(data=[trc], layout=lyt)
    offline.plot(mapping, filename='img/map.html')
state()
