import dash_core_components as dcc
import dash_html_components as html

from app import app

def layout():

  markdown_text = '''
# About us

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''
  return dcc.Markdown(markdown_text)
  