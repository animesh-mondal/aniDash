import dash_core_components as dcc
import dash_html_components as html


mom = html.Div([
                html.H2('Hi from MOM Page'),
                dcc.Link('Goto Home', href="/")
            ],style={'color':'white'})