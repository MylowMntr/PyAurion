from flaskwebgui import FlaskUI
from app import app

FlaskUI(app, width=900, height=600, idle_interval=200, close_server_on_exit=True).run()