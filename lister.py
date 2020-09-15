import importlib
import os

import dash_core_components as dcc
import dash_html_components as html

from app import app

metadata = {
 "title": 'Home' 
}


def report_item(metadata, url):
  print(metadata.description)
  
  # TODO provide default values in case some of the metadata does not exist

  return html.A( 
    href=url,
    className='row report-item',
    children = [
      html.Div( 
        className="col-sm-4",
        children= [
          html.Img(
            className="img-thumbnail",
            alt=metadata.thumb_alt,
            src=app.get_asset_url(metadata.thumb))
        ]
      ),
      html.Div( 
        className="col-sm-8",
        children= [
          html.H2(metadata.title),
          html.P(metadata.summary)
        ]
      )
    ])
    
#
# Lists modules in the folder
#
def layout(dir):
  items = []

  #TODO support module that is in a second level
  # if dir is /reports/subreports and the report is  -> module path would be reports.subreports.myreport
  dir_files = os.listdir(dir)
  for dir_file in dir_files:
    # Create full path
    full_path = os.path.join(dir, dir_file)
    # If entry is a directory then get the list of files in this directory 
    if os.path.isdir(full_path) and dir_file != '__pycache__':
      # if it is a folder, it must comply with the requirements and have a metadata 
      # import metadata
      module_name = dir + '.' + dir_file + '.metadata'
      print("module name " + module_name)
      metadata = importlib.import_module(module_name)
      item_url = '/' + dir + '/' + dir_file + '/'
      items.append(report_item(metadata, item_url))
 
  # get reports dir
  markdown_text = '''
  # Home
'''
  layout = html.Div( 
    className="home", 
    children= [
      dcc.Markdown(markdown_text),
      html.Div(className="reports",
      children=items)
    ])
  return layout 
  