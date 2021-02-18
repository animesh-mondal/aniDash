import dash_bootstrap_components as dbc
import dash_html_components as html

navbar = dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/")),
                # dbc.NavItem(dbc.NavLink("Sales Analysis", href="#")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Sales Analysis", header=True),
                        dbc.DropdownMenuItem("M-O-M", href="/mom"),
                        dbc.DropdownMenuItem("SSSG", href="/sssg"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Sales Analysis",
                ),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Reports", header=True),
                        dbc.DropdownMenuItem("Day Wise Sales", href="/dws"),
                        dbc.DropdownMenuItem("Item Wise Sales", href="/iws"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="Reports",
                ),
            ],
            brand="Wow!",
            brand_href="/",
            color="dark",
            dark=True,
            sticky="top",
        )

footer = dbc.Row(
            dbc.Col(
                html.P("Copyright @ Animesh - 2021", className="footer")
            )
        )