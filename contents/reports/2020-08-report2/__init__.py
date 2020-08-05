import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

def metadata():
  return {
    "title": "Report title",
    "description": "report short description",
    "keywords": "report, keyword",
    "thumbnail": "report, thumbnail",
  }

def page(app):

  # assume you have a "long-form" data frame
  # see https://plotly.com/python/px-arguments/ for more options
  df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
  })

  fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

  markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

  app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
     dcc.Markdown(children=markdown_text)
  ])
