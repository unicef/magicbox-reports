# %%
# additional libraries
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import geopandas as gpd
import json
import os

import dash_core_components as dcc

UNICEF_ORANGE = '#F26A21'
UNICEF_DARK_BLUE = '#374EA2'
UNICEF_RED = '#E2231A'
UNICEF_TEXT =  '#4A4A4A'

# The cwd is the root of the project. To access the data folder ./data
#print (os.getcwd())

# %%
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
    fig = go.Figure()
    fig.add_trace(
        go.Bar(x=x, y=y, marker={'color': colors})
    )
    
    fig.update_layout(
        xaxis={'title': 'First day of maximum stringency index'},
        yaxis={'title': 'Number of countries'},
    )
    return fig

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

# %%
stringency_df = pd.read_csv('./data/COVID-19_stats_stringency_index.csv')

# Get the dataframe with the stringency index of the countries to plot 
stringency_plt_df = stringency_df.loc[(stringency_df['country_to_plot'] == True)]


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
      title=dict(
        text=f'<b>{country_name}</b>',
        x=0.5,
        font= dict(
          size=20,
          color=UNICEF_TEXT
        )
      ),
      showlegend=False, 
      legend=dict( 
        yanchor="top",
        y=1.3, 
        xanchor="left",
        x=.3
      ),
      margin=dict(t=40, b=20, l=0, r=0)
    )
    
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>New COVID-19 cases per 100k population</b>", color=UNICEF_RED, secondary_y=False)
    fig.update_yaxes(title_text="<b>Stringency Index</b>", color=UNICEF_DARK_BLUE, secondary_y=True)
    
    # Where dtick tells to have monthly ticks ('M'), one per each month ('1'), 
    # tickformat you can change it (in the static plots was "%d.%m", but not crucial), 
    # ticks='outside' is to have small tick lines marking them below the x axis
    #fig.update_xaxes(dtick="M1", tickformat="%b\n%Y", ticks='outside')
    return fig  

# %%
def heatmap_by_gdp(values_column, 
                   title="Heatmap", 
                   colorscale = "blues"):
    """
    Using "COVID-19_stats_stringency_index.csv" as dataset, returns a plot with 3 heatmaps for the 
    "high", "middle", "poor" categories in the column "category_gdp_per_capita" for the countries that 
    have the mark "country_to_plot".any 

    Parameters
    ----------
    - values_column: (string)is the name of the column in COVID-19_stats_stringency_index.csv that we want to display.
    - colorscale: (string) one of the builtin color scales https://plotly.com/python/builtin-colorscales/
    """
    # TODO: Should we get rid of the null?

    # Column "category_gdp_per_capita" possible values
    gdp_categories = ["poor", "middle", "rich"]

    min_date = "2020-01-31"
    max_date = "2020-09-29"
    
    # Because we cannot call a country poor, we need a better title.. 
    gdp_titles = ["Low income", "Middle income", "High income"]
    # Create the figure with as many categories of gdp 
    fig = make_subplots(rows=len(gdp_categories), 
                        cols=1, 
                        shared_yaxes=False,
                        subplot_titles=gdp_titles)
    fig.update_layout(height=1024, title_text=title)

    # Remove null values 
    for i in range(len(gdp_categories)):
        gdp = gdp_categories[i]
        gdp_title = gdp_titles[i]
        # Filter by gdp per capita. 
        # Then get rid of the other columns of the df. heatmap-df contains only the data we need for the 
        heatmap_df = stringency_plt_df.loc[(stringency_plt_df['category_gdp_per_capita'] == gdp)].loc[:, ['location', "Date", values_column]]

        # Ensure min date and max date range
        # For max date we just keep only dates < max date
        heatmap_df = heatmap_df.loc[heatmap_df["Date"] < max_date]
        # For min date, as we know that the dataset does not contain it, we set a fake col with that value
        min_date_row = {'Date': min_date, "location": heatmap_df.iloc[0].location, values_column: None}
        heatmap_df = heatmap_df.append(min_date_row, ignore_index=True)
        
        #print ("max_col", heatmap_df[values_column].max(), "date-range", heatmap_df["Date"].min(), heatmap_df["Date"].max())
        
        # Dataframe with a pivot table that has country as index the columns are the dates 
        # Countries 20-mar 21-mar 22-mar
        # USA       1.0    2.0    3.0
        # Italy     2.0    2.1    2.2
        # Spain     3.0    3.1    3.2
        pivot_df = heatmap_df.pivot(index="location", columns="Date", values=values_column)
        
        # Fill empty values with prev column valida value and the remainings with 0
        pivot_df = pivot_df.fillna(axis=1, method="pad").fillna(0)
        
        #print(pivot_df.head())
        
        #Normalize (specially for cases )
        max_cols = pivot_df.max(axis=1)
        pivot_df = pivot_df.div(max_cols, axis=0) *100

        # Gets an array version of the pivot dataframe, a format tha can be used 
        # in the heatmap. 
        heatmap_values = pivot_df.to_numpy()
        #Get the list of countries (y axes)
        countries = heatmap_df.loc[:,'location'].unique()
        # get the list of dates (x axes in the heatmap)
        dates = pivot_df.columns
        
        #print(heatmap_values.shape)
        #print('date numpy', len(heatmap_df['Date'].to_numpy()))
        #print('location', len(heatmap_df['location']))
        #print(len(heatmap_df[values_column]))
        #print(pivot_df.columns)
        #print(countries, len(countries))

        fig.append_trace(
            go.Heatmap(
                z=heatmap_values,
                y=countries,
                x=dates,
                colorscale=colorscale,
                colorbar=dict(
                    yanchor="top",
                    y=(3-i)/3, # TODO fix position of this this
                    len=200, 
                    ypad=10,
                    lenmode="pixels",
                    title=gdp_title,

                    thickness=15)
            ),
            row=i+1, # for starts in 0, row starts in 1.
            col=1
        )
    
    return fig


