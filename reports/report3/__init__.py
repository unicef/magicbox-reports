import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

def layout():
  layout = html.Div([
    html.H3('Report 3'),
    dcc.Dropdown(
        id='app-3-dropdown',
        options=[
            {'label': 'App 3 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
  ])
  return layout

@app.callback(
    Output('app-3-display-value', 'children'),
    [Input('app-3-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)