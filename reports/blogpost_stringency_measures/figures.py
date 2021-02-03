# additional libraries
import pandas as pd
import plotly.graph_objs as go
import geopandas as gpd
import os

import dash_core_components as dcc

# The cwd is the root of the project. To access the data folder ./data
#print (os.getcwd())

# load data as a dataframe
gdf = gpd.read_file('https://raw.githubusercontent.com/unicef/magicbox-reports/report/blogpost_stringency_measures/data/geodata_COVID-19_stringency_delay.geojson', driver='GeoJSON')

# Num countries vs first day max stringency
histo = pd.read_csv('./data/histo_num_countries_vs_first_day_max_stringency.csv')

 # Scatter scatter plot
def total_cases_at_max_stringency_day_vs_delay_high_stringency_max_cases(): 
  dcc.Graph(
        id='total_cases_at_max_stringency_day_vs_delay_high_stringency_max_cases',
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
    )

def histo_num_countries_vs_first_day_max_stringency():
  x = histo['start_date']
  y = histo['num_countries']
  colors = histo['color']
  figure = go.Figure(
    data=[go.Bar(x=x, y=y, marker= {'color': colors})],
    layout=go.Layout(
        title=go.layout.Title(text="First day of maximum stringency index"),
        xaxis={'title': 'First day of maximum stringency index'},
        yaxis={'title': 'Number of countries'},
        
    )
  )  
  return dcc.Graph(
    id="histo_num_countries_vs_fist_day_stringency",
    config={'displaylogo': False},
    figure=figure
  )
