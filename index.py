import re 
import importlib

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import lister
import about
from config import config
#from reports import report2, report3


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Router 
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    reportName = re.search('^/reports/([\w\-]*)',pathname) 
    print('pathname:' + pathname)
    print(reportName) 
    if pathname == '/':
      return lister.layout(config['reports_dir'])
    elif pathname == '/about':  
      return about.layout()
    elif reportName:
      # try to search the report
      #os.walk(config['reports_dir'])
      print(reportName.group(1))
      try:
        module_name = 'reports.' + reportName.group(1)
        print("module name " + module_name)
        report = importlib.import_module(module_name)
        app.title = module_name
        return report.layout()
      except:
         return '404'
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)