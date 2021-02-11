# additional libraries
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import geopandas as gpd
import json
import os

import dash_core_components as dcc

# The cwd is the root of the project. To access the data folder ./data
#print (os.getcwd())


geojson_file_path = "./data/geodata_COVID-19_stringency_delay.geojson"

# GeoJSON data as a dataframe
gdf = gpd.read_file(geojson_file_path, driver='GeoJSON')

# Load GeoJSON as a JSON
with open(geojson_file_path) as file:
    geodata = json.load(file)

# Num countries vs first day max stringency
histo = pd.read_csv('./data/histo_num_countries_vs_first_day_max_stringency.csv')
  

# Scatter plot
def total_cases_at_max_stringency_day_vs_delay_high_stringency_max_cases(): 
  return dcc.Graph(
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
        xaxis={'title': 'First day of maximum stringency index'},
        yaxis={'title': 'Number of countries'},
        
    )
  )  
  return dcc.Graph(
    id="histo_num_countries_vs_fist_day_stringency",
    config={'displaylogo': False},
    figure=figure
  )

def first_day_max_stringency_map():
  figure = px.choropleth_mapbox(gdf, geojson=geodata, 
        locations='iso_a3', #  
        featureidkey="properties.iso_a3",
        color='first_day_max_stringency_numerical',                
        color_continuous_scale="YlOrRd", #https://plotly.com/python/builtin-colorscales/
        #range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=1, 
        center = {"lat": 0.0, "lon": 0.0},
        opacity=.8,
        labels={'first_day_max_stringency':'First day maxinun stringency'}
        )
  figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

  return dcc.Graph(
    id="first_day_max_stringency_map",
    config={'displaylogo': False},
    figure=figure
  )
  
def total_cases_per_100k_at_first_day_max_stringency_map():
  figure = px.choropleth_mapbox(gdf, geojson=geodata, 
        locations='iso_a3', #  
        featureidkey="properties.iso_a3",
        color='total_cases_per_100k_at_first_day_max_stringency',                
        color_continuous_scale="Reds", #https://plotly.com/python/builtin-colorscales/
        #range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=1, 
        center = {"lat": 0.0, "lon": 0.0},
        opacity=.8,
        labels={'total_cases_per_100k_at_first_day_max_stringency':"Cases per 100k"}
        )
  figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  return dcc.Graph(
    id="total_cases_per_100k_at_first_day_max_stringency_map",
    config={'displaylogo': False},
    figure=figure
  )

  return None

def delay_day_max_new_cases_per_100k_first_day_sim_max_stringency_map():
  # Create a column name with a shorter name
  gdf['delay_max_cases_with_max_stringency'] = gdf['delay_day_max_new_cases_per_100000_first_day_sim_max_stringency_numerical_2020-03-01_2020-06-30']
  figure = px.choropleth_mapbox(gdf, geojson=geodata, 
        locations='iso_a3',   
        featureidkey="properties.iso_a3",
        color='delay_max_cases_with_max_stringency',                
        color_continuous_scale="matter", #https://plotly.com/python/builtin-colorscales/
        #range_color=(0, 12),
        mapbox_style="carto-positron",
        zoom=1, 
        center = {"lat": 0.0, "lon": 0.0},
        opacity=.9,
        labels={'delay_max_cases_with_max_stringency':"Delay in days"}
        )
  figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
  return dcc.Graph(
    id="delay_day_max_new_cases_per_100k_first_day_sim_max_stringency_map",
    config={'displaylogo': False},
    figure=figure
  )

stringency_df = pd.read_csv('/Users/merlos/devel/magicbox-reports/magicbox-reports/data/COVID-19_stats_stringency_index.csv')

UNICEF_ORANGE = '#F26A21'
UNICEF_DARK_BLUE = '#374EA2'
UNICEF_RED="#E2231A"
def stringency_vs_cases(iso_code='SGP'):

    # Get stats only for the selected country
   
    filtered = stringency_df.loc[stringency_df['iso_code'] == iso_code]
    country_name = filtered.iloc[0].location
    print(country_name)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    #fig = go.Figure()
    # Cases per 100k
    fig.add_trace(
        go.Scatter(    
            x=filtered['date'], 
            y=filtered['new_cases_per_100000'], 
            mode='markers', 
            name="Cases per 100k pop",
            marker_color=UNICEF_RED,
        )
    )
    # update marker
    fig.update_traces(mode='markers', marker_line_width=0, marker_size=2)
    fig.add_trace(
        go.Scatter(
            x=filtered['date'], 
            y=filtered['new_cases_per_100000_7_day_average'], 
            mode='lines', 
            name="cases per 100k pop (7 day average)",
            marker_color=UNICEF_RED
        )
    )
    fig.add_trace(
        go.Scatter(
            x=filtered['date'], 
            y=filtered['stringency_index'], 
            mode='lines+markers',
            name="Stringency index",
            marker=dict(size=3, color=UNICEF_DARK_BLUE)
        ),
        secondary_y=True,
    )
    
    # Set the position of the legend
    fig.update_layout(
       title=country_name, 
      legend=dict( 
        yanchor="top",
        y=1.3, 
        xanchor="left",
        x=.3
      )
    )
    
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>New COVID-19 cases per 100k population</b>", color=UNICEF_RED, secondary_y=False)
    fig.update_yaxes(title_text="<b>Stringency Index</b>", color=UNICEF_DARK_BLUE, secondary_y=True)
    return dcc.Graph(
      id=f"stringency_vs_cases_{iso_code}",
      config={'displaylogo': False},
      figure=fig
    )  