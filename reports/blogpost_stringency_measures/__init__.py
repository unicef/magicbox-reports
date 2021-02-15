import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from lib import unicef_html_components as uhtml
from lib import unicef_dash_core_components as udcc
from app import app

# additional libraries
import pandas as pd
import plotly.graph_objs as go
import geopandas as gpd
import os

from . import figures 

# load data as a dataframe
gdf = gpd.read_file('https://raw.githubusercontent.com/unicef/magicbox-reports/report/blogpost_stringency_measures/data/geodata_COVID-19_stringency_delay.geojson', driver='GeoJSON')

# print(gdf.dtypes)

def layout():
  layout = html.Div(
    className="doc container",
    children =[
    html.H1(className="display-4", children=["When to implement lockdowns"] ),
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
        'NYC', 'MTL', 'LA']]
    ),
  figures.total_cases_at_max_stringency_day_vs_delay_high_stringency_max_cases(),
  dcc.Markdown('''
    Placeholder paragraph text. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit sem odio, 
    et efficitur augue fermentum id. Phasellus justo ligula, convallis vel sapien a, pulvinar 
    posuere lacus. Vivamus dapibus, arcu quis consectetur mollis, arcu purus ultrices urna, et
     finibus felis augue sed nisl. Cras feugiat erat lectus, facilisis vestibulum quam posuere quis.
      Sed convallis tellus quis varius ultricies. Sed malesuada facilisis finibus. Fusce condimentum orci 
      ut turpis porta eleifend. '''),
  figures.histo_num_countries_vs_first_day_max_stringency(),
  dcc.Markdown('''
    Placeholder paragraph text, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit sem odio, 
    et efficitur augue fermentum id. Phasellus justo ligula, convallis vel sapien a, pulvinar posuere lacus. 
    Vivamus dapibus, arcu quis consectetur mollis, arcu purus ultrices urna, et finibus felis augue sed nisl. 
    Cras feugiat erat lectus, facilisis vestibulum quam posuere quis. Sed convallis tellus quis varius ultricies.
     Sed malesuada facilisis finibus. Fusce condimentum orci ut turpis porta eleifend. '''),
  figures.first_day_max_stringency_map(),
  dcc.Markdown('''
    Placeholder paragraph text, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit sem odio, 
    et efficitur augue fermentum id. Phasellus justo ligula, convallis vel sapien a, pulvinar posuere lacus. 
    Vivamus dapibus, arcu quis consectetur mollis, arcu purus ultrices urna, et finibus felis augue sed nisl. 
    Cras feugiat erat lectus, facilisis vestibulum quam posuere quis. Sed convallis tellus quis varius ultricies.
     Sed malesuada facilisis finibus. Fusce condimentum orci ut turpis porta eleifend. '''),
  figures.total_cases_per_100k_at_first_day_max_stringency_map(),
  dcc.Markdown('''
    Placeholder paragraph text, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit sem odio, 
    et efficitur augue fermentum id. Phasellus justo ligula, convallis vel sapien a, pulvinar posuere lacus. 
    Vivamus dapibus, arcu quis consectetur mollis, arcu purus ultrices urna, et finibus felis augue sed nisl. 
    Cras feugiat erat lectus, facilisis vestibulum quam posuere quis. Sed convallis tellus quis varius ultricies.
     Sed malesuada facilisis finibus. Fusce condimentum orci ut turpis porta eleifend. '''),
  figures.delay_day_max_new_cases_per_100k_first_day_sim_max_stringency_map(),
  dcc.Markdown('''
    Placeholder paragraph text, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit sem odio, 
    et efficitur augue fermentum id. Phasellus justo ligula, convallis vel sapien a, pulvinar posuere lacus. 
    Vivamus dapibus, arcu quis consectetur mollis, arcu purus ultrices urna, et finibus felis augue sed nisl. 
    Cras feugiat erat lectus, facilisis vestibulum quam posuere quis. Sed convallis tellus quis varius ultricies.
     Sed malesuada facilisis finibus. Fusce condimentum orci ut turpis porta eleifend. '''),
  uhtml.two_cols(
    figures.stringency_vs_cases('IND'),
    figures.stringency_vs_cases('SGP')
  ),
  dcc.Markdown('''
    Placeholder paragraph text, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus blandit sem odio, 
    et efficitur augue fermentum id. Phasellus justo ligula, convallis vel sapien a, pulvinar posuere lacus. 
    Vivamus dapibus, arcu quis consectetur mollis, arcu purus ultrices urna, et finibus felis augue sed nisl. 
    Cras feugiat erat lectus, facilisis vestibulum quam posuere quis. Sed convallis tellus quis varius ultricies.
     Sed malesuada facilisis finibus. Fusce condimentum orci ut turpis porta eleifend. '''),
  uhtml.two_cols(
    udcc.graph(
      figures.heatmap_by_gdp("stringency_index"),
      id="new_cases_heatmap"
    ),
    udcc.graph(
      figures.heatmap_by_gdp("new_cases_per_100000_7_day_average", colorscale="reds"),
      id="stringency_heatmap"
    )
  )   
  ])
  return layout

@app.callback(
    Output('app-blogpost-display-value', 'blogpost'),
    [Input('app-blogpost-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)