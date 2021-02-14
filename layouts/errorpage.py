import dash_core_components as dcc
import dash_html_components as html


errorPage = html.Div([
                html.H2('404 Page not found'),
                html.H6('This page is not available or the server is not responding..'),
                dcc.Link('Go to Home Page',href='/')
            ], className="error")