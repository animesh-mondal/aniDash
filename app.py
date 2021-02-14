import dash
import dash_bootstrap_components as dbc
import dash_auth
from flask import send_file

VALID_USERNAME_PASSWORD_PAIRS = [['tanu','mondal']]

#add external fonts
gFont = """
    https://fonts.googleapis.com/css2?family=Nunito&family=Pacifico&family=Roboto&display=swap

    """

#Creating app
app = dash.Dash(__name__,suppress_callback_exceptions=True,external_stylesheets=[dbc.themes.BOOTSTRAP, gFont])
server = app.server
app.title = "Wow! Dashboard"

auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)

# downloading a file 

@server.route("/download")
def download():
    """Serve a file from the upload directory."""
    file = "data/Sales.csv"
    return send_file(file, as_attachment=True)