# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import importlib
import os

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['https://cdn.jsdelivr.net/npm/@unicef/design-system/dist/css/unicef.css']
reports_dir = 'reports'

# Instantiate the app 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Expose server
server = app.server

# load the header

os.walk(reports_dir)

# Dynamically import all the folders/
#import reports.report1 as report
#report.report(app)

mod_name = 'contents.reports.report1'
report_mod = importlib.import_module(mod_name)
report_mod.page(app)

if __name__ == '__main__':
    app.run_server(debug=True)