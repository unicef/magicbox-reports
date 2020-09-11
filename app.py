# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import importlib
import os
from config import config
from lib.UnicefDash import UnicefDash 

external_stylesheets = ['https://cdn.jsdelivr.net/npm/@unicef/design-system/dist/css/unicef.css',
'https://cdn.jsdelivr.net/npm/@unicef/design-system/dist/css/doc.css'
]

# Instantiate the app 
app = UnicefDash(__name__, 
  external_stylesheets=external_stylesheets,
  update_title='Loading...')

# Expose server 
server = app.server

# 
os.walk(config['reports_dir'])

# Dynamically import all the folders/
#import reports.report1 as report
#report.report(app)
module_name = 'contents.reports.report1'
report = importlib.import_module(module_name)


# Put app metadata
metadata = report.metadata()
report.page(app)


if __name__ == '__main__':
    app.run_server(debug=True)