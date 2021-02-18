import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import homepage, errorpage, mom, sssg, dws, iws
import callbacks
from app import server


app.layout = html.Div([
    dcc.Location(id='url',refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content','children'),
              [Input('url','pathname')])
def display_page(pathname):
    if pathname == '/':
        return homepage.homePage
    elif pathname == '/mom':
        return mom.mom
    elif pathname == '/sssg':
        return sssg.sssg
    elif pathname == '/dws':
        return dws.dws
    elif pathname == '/iws':
        return iws.iws
    else:
        return errorpage.errorPage

if __name__ == '__main__':
    app.run_server(debug=True)