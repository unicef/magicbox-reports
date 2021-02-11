# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import plotly.graph_objs as go
import geopandas as gpd
import os
import plotly.express as px
from plotly.subplots import make_subplots

#import dash_core_components as dcc

# The cwd is the root of the project. To access the data folder ./data
print (os.getcwd())



# %%
# load data as a dataframe
gdf = gpd.read_file('https://raw.githubusercontent.com/unicef/magicbox-reports/report/blogpost_stringency_measures/data/geodata_COVID-19_stringency_delay.geojson', driver='GeoJSON')

 # Scatter scatter plot
def total_cases_at_max_stringency_day_vs_delay_high_stringency_max_cases(): 
  figure = go.Figure(
            data= [
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
            layout = go.Layout(
                xaxis={'title': 'Days difference between maximum cases and first day high stringency'},
                yaxis={'type': 'log', 'title': 'Total COVID cases per 100k pop. at first day max stringency'},
                margin={'l': 100, 'b': 50, 't': 50, 'r': 100},
                legend={'x': 1, 'y': 0.5},
                hovermode='closest'
            )
          )
  return figure

figure = total_cases_at_max_stringency_day_vs_delay_high_stringency_max_cases
figure.show()


# %%
# Num countries vs first day max stringency
histo = pd.read_csv('/Users/merlos/devel/magicbox-reports/magicbox-reports/data/histo_num_countries_vs_first_day_max_stringency.csv')

def histo_num_countries_vs_first_day_max_stringency_figure():
  x = histo['start_date']
  y = histo['num_countries']
  colors = histo['color']
  figure = go.Figure(
    data=[go.Bar(y=y)],
    layout=go.Layout(
        title=go.layout.Title(text="First day of maximum stringency index"),
    
    )
  )  
  return figure
  #return dcc.Graph(
  #  id="histo_num_countries_vs_fist_day_stringency",
  #  config={'displaylogo': False},
  #  figure=figure
  #)
    
def histo_num_countries_vs_first_day_max_stringency():
  x = histo['start_date']
  y = histo['num_countries']
  colors = histo['color']
  marker=dict(
            color='LightSkyBlue',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
  figure = px.bar(histo, y='num_countries') 
  return figure

figure = histo_num_countries_vs_first_day_max_stringency()

figure.show()


# %%
from urllib.request import urlopen


with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
    print(json.dumps(countries, indent=2))

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    dtype={"fips": str})



def first_day_max_stringency_map1(): 
    fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig
    
print( countries)    
#figure = first_day_max_stringency_map1().show()
df.head()


# %%
geodata= None

with open("../../data/geodata_COVID-19_stringency_delay.geojson") as f:
    geodata = json.load(f)

json_formatted_str = json.dumps(geodata, indent=2)

print(json_formatted_str)


# %%
import json
import geopandas

geojson_file_path = "../../data/geodata_COVID-19_stringency_delay.geojson"

with open(geojson_file_path) as file:
    geodata = json.load(file)
    
gdf = geopandas.read_file(geojson_file_path)
gdf.head()


# %%
# Analize max and min
max = gdf.first_day_max_stringency_numerical.max()
min = gdf.first_day_max_stringency_numerical.min()
print (max, min, max-min)


# %%
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
    
   # colorbar = {"bgcolor": "rgba(10,10,10","tickmode:":"array", 
   #             "nticks": 5 }
   # fig.update_traces(colorbar=colorbar)

    return figure
    
figure = first_day_max_stringency_map().show()


# %%


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
        labels={'total_cases_per_100k_at_first_day_max_stringency':"Cases per 100k at 1st day of maximum stringency"}
        )
    figure.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    return figure
    
figure = total_cases_per_100k_at_first_day_max_stringency_map().show()


# %%
# color_delay_sim_max_stringency,
def delay_day_max_new_cases_per_100k_first_day_sim_max_stringency_map(): 
    # Create a column name with a shorter name
    gdf['delay_max_cases_with_max_stringency'] = gdf['delay_day_max_new_cases_per_100000_first_day_sim_max_stringency_numerical_2020-03-01_2020-06-30']
    figure = px.choropleth_mapbox(gdf, geojson=geodata, 
        locations='iso_a3', #  
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
    
    return figure
    
figure = delay_day_max_new_cases_per_100k_first_day_sim_max_stringency_map().show()


# %%
gdf["delay_day_max_new_cases_per_100000_first_day_sim_max_stringency_numerical_2020-03-01_2020-06-30"].min()


# %%
neg_delay = gdf.loc[gdf["delay_day_max_new_cases_per_100000_first_day_sim_max_stringency_numerical_2020-03-01_2020-06-30"] < 0]
neg_delay.loc[:,["iso_a3","first_day_max_stringency","delay_day_max_new_cases_per_100000_first_day_sim_max_stringency_numerical_2020-03-01_2020-06-30"]]


# %%
gdf.head()


# %%

stringency_df = pd.read_csv('/Users/merlos/devel/magicbox-reports/magicbox-reports/data/COVID-19_stats_stringency_index.csv')

UNICEF_ORANGE = '#F26A21'
UNICEF_DARK_BLUE = '#374EA2'
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
            marker_color=UNICEF_ORANGE,
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
            marker_color=UNICEF_ORANGE
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
    fig.update_layout(title=country_name, legend=dict( yanchor="top",y=1.3, xanchor="left",x=.5))
    
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>New COVID-19 cases per 100k population</b>", color=UNICEF_ORANGE, secondary_y=False)
    fig.update_yaxes(title_text="<b>Stringency Index</b>", color=UNICEF_DARK_BLUE, secondary_y=True)
    return fig


stringency_vs_cases().show()


# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



# %%



