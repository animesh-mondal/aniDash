import dash_core_components as dcc
import dash_html_components as html


dws = html.Div([
                html.H2('Hi from Day Wise Sales Page'),
                dcc.Link('Goto Home', href="/")
            ],style={'color':'white'})