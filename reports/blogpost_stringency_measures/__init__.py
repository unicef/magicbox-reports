import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

# additional libraries
import pandas as pd
import plotly.graph_objs as go
import geopandas as gpd
import os



# load data as a dataframe
gdf = gpd.read_file('https://raw.githubusercontent.com/unicef/magicbox-reports/report/blogpost_stringency_measures/data/geodata_COVID-19_stringency_delay.geojson', driver='GeoJSON')

# print(gdf.dtypes)

def layout():
  layout = html.Div(
    className="doc container",
    children =[
    html.H1(className="display-4", children=["When to implement lockdowns?"] ),
    dcc.Markdown('''
   
    The World Health Organization declared COVID-19 a pandemic on 11 March 2020. Since then, COVID has deeply 
    changed our lives and the world we live in, and it is a situation that our governments and systems 
    have not seen for generations. While the virus predominantly causes mild symptoms, [a large fraction 
    of people can develop severe conditions](https://journal.chestnet.org/article/S0012-3692(20)34906-0/fulltext) which require prolonged intensive care.
    
    In addition, the long-term effects of COVID are still uncertain but include organ damage and long-term illness,
     even in young adults and persons with no underlying medical conditions. As such, curbing the transmission of the virus is important 
    to limit the number of people exposed to the virus and, consequently, to reduce the load on healthcare systems. 
    The latter is important because a strained healthcare system disrupts the access to vital services for non-COVID 
    patients in need of intensive care and treatments for [cancer](https://ascopubs.org/doi/full/10.1200/GO.20.00351 ),
    [tuberculosis](https://www.who.int/news/item/14-10-2020-who-global-tb-progress-at-risk), [malaria](https://www.nature.com/articles/s41591-020-1025-y), and many other 
    conditions. 

    To contain the virus a large majority of countries in the world implemented national lockdowns, in combination 
    with a suite of other non-pharmaceutical interventions (interventions other than getting vaccinated and taking 
    medicine) such as mandatory mask wearing and closing of schools. Here **we study the timeline of national lockdowns 
    and when individual countries implemented them**. Figure 1 shows that this happened in an almost synchronized manner
     with countries across multiple continents implementing lockdowns and other strict physical distancing measures at 
     the same time. What led to the cascade of lockdowns is an open question: **were decisions determined by local 
     epidemiological context or influenced by what other countries were doing?**  '''),
    dcc.Dropdown(
        id='app-blogpost-dropdown',
        options=[
            {'label': 'Blogpost - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    # add scatter plot
    dcc.Graph(
        id='total_cases_at_max_stringency_day-vs-delay_high_stringency_max_cases',
        config= {'displaylogo': False},
        figure={
            'data': [
                go.Scatter(
                    x=gdf.loc[gdf['continent'] == continent]['delay_day_max_new_cases_per_100000_first_day_sim_max_stringency_numerical_2020-03-01_2020-06-30'],
                    y=gdf.loc[gdf['continent'] == continent]['total_cases_per_100k_at_first_day_max_stringency'],
                    text=gdf.loc[gdf['continent'] == continent]['name'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 12, # gdf.loc[gdf['continent'] == continent]['max_stringency']
                        'line': {'width': 0.5, 'color': 'white'},
                        'color': i
                    },
                    name=continent
                ) for i,continent in enumerate(gdf['continent'].unique())
            ],
            'layout': go.Layout(
                xaxis={'title': 'Days difference between maximum cases and first day high stringency'},
                yaxis={'type': 'log', 'title': 'Total COVID cases per 100k pop. at first day max stringency'},
                margin={'l': 100, 'b': 50, 't': 50, 'r': 100},
                legend={'x': 1, 'y': 0.5},
                hovermode='closest'
            ),
        }
    ),
  ])
  return layout

@app.callback(
    Output('app-blogpost-display-value', 'blogpost'),
    [Input('app-blogpost-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)