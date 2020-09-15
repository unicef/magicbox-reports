import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

def layout():
  layout = html.Div([
    html.H3('Report 2'),
    dcc.Dropdown(
      id='app-1-dropdown',
      options=[
          {'label': 'Report 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
  ])
  return layout


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)