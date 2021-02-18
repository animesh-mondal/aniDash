import dash_core_components as dcc
import dash_html_components as html


sssg = html.Div([
                html.H2('Hi from SSSG Page'),
                dcc.Link('Goto Home', href="/")   
            ],style={'color':'white'})