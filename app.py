import dash
from config import config
from lib.UnicefDash import UnicefDash


app = UnicefDash(__name__, 
    external_stylesheets=config['external_stylesheets'],
    update_title='Loading...',
    suppress_callback_exceptions=True)

server = app.server