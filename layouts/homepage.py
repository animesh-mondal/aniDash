import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from data import sale
from datetime import date, timedelta
from components.controls import navbar, footer


dropOptions = [{'label': i, 'value': i} for i in sale['City'].unique()]
dropOptions.append({'label': 'All City', 'value': 'All City'}.copy())
brand = ['All Brand','Wow! Momo', 'Wow! China','Combo']
dropOptionsBrand = [{'label': i, 'value': i} for i in brand]

homePage = html.Div([
            navbar,
            dbc.Row(
                dbc.Col(
                    html.H1("Welcome to the Wow! Dashboard", className="header text-center"),
                ),
            ),
            dbc.Container([
                dbc.Row([ 
                    dbc.Col([
                        dcc.Dropdown(
                            id="dropD1",
                            options= dropOptions,
                            value="All City",
                            clearable=False,
                        )
                    ],className="col-3"),
                    dbc.Col([
                        dcc.Dropdown(
                            id="dropDBrand",
                            options= dropOptionsBrand,
                            value="All Brand",
                            clearable=False
                        )
                    ],className="col-3"),
                    dbc.Col([
                        dcc.DatePickerRange(
                                id="datePicker",
                                # min_date_allowed=dt(2020, 12, 1),
                                # max_date_allowed=dt(2021, 1, 31),
                                initial_visible_month=date.today() - timedelta(days=1),
                                start_date=(date.today() - timedelta(days=1)).replace(day=1),
                                end_date=date.today() - timedelta(days=1),
                                className= "m-3"
                            ),
                    ],className= "col-4" ),
                    dbc.Col(
                        dbc.Button(children="Submit", id="submit-btn", n_clicks=0, className="btn btn-info")
                    ),
                        
                ],className="align-items-center"),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Total Sales"),
                            dbc.CardBody(
                                [
                                    html.H4(id="total-sale", className="card-title"),
                                    html.P(id="total-sale-gd", className="card-text"),
                                ]
                            ),
                            dbc.CardFooter(id="total-sale-lm"),
                        ],className = "card-ani")
                    ),
                    dbc.Col(
                        dbc.Card(
                        [
                            dbc.CardHeader("Total Transaction"),
                            dbc.CardBody(
                                [
                                    html.H4(id="total-trans" , className="card-title"),
                                    html.P(id="total-trans-gd", className="card-text"),
                                ]
                            ),
                            dbc.CardFooter(id="total-trans-lm"),
                        ],className = "card-ani")
                    ),
                    dbc.Col(
                        dbc.Card(
                        [
                            dbc.CardHeader("APC"),
                            dbc.CardBody(
                                [
                                    html.H4(id="total-apc" , className="card-title"),
                                    html.P(id="total-apc-gd", className="card-text"),
                                ]
                            ),
                            dbc.CardFooter(id="total-apc-lm"),
                        ],className = "card-ani")
                    ),
                    dbc.Col(
                        dbc.Card(
                        [
                            dbc.CardHeader("Last Day Sale"),
                            dbc.CardBody(
                                [
                                    html.H4(id="total-last-day-sale" , className="card-title"),
                                    html.P(id="total-last-day-sale-gd", className="card-text"),
                                ]
                            ),
                            dbc.CardFooter(id="total-last-day-sale-lw"),
                        ],className = "card-ani")
                    ),
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(
                            id="total-sale-gph",
                            config={'displaylogo': False},
                        )
                    ],className = "col-lg-6"),
                    dbc.Col([
                        dcc.Graph(
                            id="total-mode-sale-gph",
                            config={'displaylogo': False}
                        )
                    ],className = "col-lg-6")
                ],className = "mt-3 mb-3"),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(
                            id="total-txn-gph",
                            config={'displaylogo': False}
                        )
                    ],className = "col-lg-6"),
                    dbc.Col([
                        dcc.Graph(
                            id="total-mode-txn-gph",
                            config={'displaylogo': False}
                        )
                    ],className = "col-lg-6")
                ],className = "mt-3 mb-3"),
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(
                            id="total-apc-gph",
                            config={'displaylogo': False}
                        )
                    ],className = "col-lg-6"),
                    dbc.Col([
                        dcc.Graph(
                            id="total-mode-apc-gph",
                            config={'displaylogo': False}
                        )
                    ],className = "col-lg-6")
                ],className = "mt-3 mb-3"),
                
            ]),
            footer
        ])
