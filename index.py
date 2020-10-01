import re 
import importlib

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

import header
import lister
import about
from config import config
#from reports import report2, report3

app.renderer = '''
var renderer = new DashRenderer({
    request_pre: (payload) => {
        // print out payload parameter
        console.log(payload);
    },
    request_post: (payload, response) => {
        // print out payload and response parameter
        console.log(payload);
        console.log(response);
    }
})
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className="", id='page-header'),
    html.Div(className="doc container mt-4", id='page-content')
])

#
# if the query string (ie search) has embedded=true, then
# hide header
#
@app.callback(Output('page-header', 'children'),
              [Input('url', 'search')])
def display_header(search):
  print('display_header: search: ' + search) 
  hideHeader = re.search('embedded=true',search) 
  if hideHeader:
    return ''
  return header.layout()

#
# Router
#  
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_contents(pathname):
    reportName = re.search('^/reports/([\w\-]*)',pathname) 
    print('display_contents: pathname:' + pathname)
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
        #print("module name " + module_name)
        report = importlib.import_module(module_name)
        app.title = module_name
        return report.layout()
      except:
         return '404'
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
