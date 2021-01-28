import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

# additional libraries
import pandas as pd
import plotly.graph_objs as go

# load data as a dataframe
df = pd.read_csv('https://raw.githubusercontent.com/unicef/magicbox-reports/master/data/country_merged.csv')


def layout():
  layout = html.Div([
    html.H3('Report 3'),
    dcc.Dropdown(
        id='app-3-dropdown',
        options=[
            {'label': 'Report 3 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    # add scatter plot
    dcc.Graph(
        id='travel-distance',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['admin2'] == i]['distance_travelled'],
                    y=df[df['admin2'] == i]['date'],
                    #text=df[df['admin2'] == i]['urban'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 13,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.admin2.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Travel Distance (km)'},
                yaxis={'title': 'Date'},
                margin={'l': 100, 'b': 50, 't': 50, 'r': 100},
                legend={'x': 1, 'y': 0.5},
                hovermode='closest'
            )
        }
    ),
  ])
  return layout

@app.callback(
    Output('app-3-display-value', 'children'),
    [Input('app-3-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)