import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback

from pages.USA.usa_east_ny_tab import get_usa_east_ny_content
from pages.USA.usa_east_philly_tab import get_usa_east_philly_content
from pages.USA.usa_west_la_tab import get_usa_west_la_content
from pages.USA.usa_west_sa_tab import get_usa_west_sa_content

from styles_info import get_styles_info

dash.register_page(__name__, name='USA', path = '/usa')

SIDEBAR_STYLE, CONTENT_STYLE = get_styles_info()

sidebar = html.Div(
    [
        html.H2("USA Cities", className="display-8"),
        html.Hr(),
        html.P(
            "Information on USA cities", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("East Coast", href=f"usa/east/ny", active="exact"),
                dbc.NavLink("West Coast", href=f"usa/west/la", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

usa_east = html.Div([
                            dbc.Tabs(
                                [
                                    dbc.Tab(label="NEW YORK", tab_id="usa_east_ny_id"),
                                    dbc.Tab(label="PHILADELPHIA", tab_id="usa_east_philly_id"),
                                ],
                                id="tabs",
                                active_tab="usa_east_ny_id",
                            ),
                            html.Div(id="usa_tab-content", className="p-4"),
                            ])

usa_west = html.Div([
                            dbc.Tabs(
                                [
                                    dbc.Tab(label="LOS ANGELES", tab_id="usa_west_la_id"),
                                    dbc.Tab(label="SAN FRANCISCO", tab_id="usa_west_sa_id"),
                                ],
                                id="tabs",
                                active_tab="usa_west_la_id",
                            ),
                            html.Div(id="usa_tab-content", className="p-4"),
                            ])

content = html.Div(id="usa_page-content", style=CONTENT_STYLE)

layout = html.Div([dcc.Location(id="url_usa"), sidebar, content])

usa_east_ny_content = get_usa_east_ny_content()
usa_east_philly_content = get_usa_east_philly_content()

usa_west_la_content = get_usa_west_la_content()
usa_west_sa_content = get_usa_west_sa_content()

@callback(
          Output("usa_page-content", "children"),
          [Input("url_usa", "pathname")])

def render_page_content(pathname):

    if pathname == f"/" or pathname == f"/usa" or pathname == f"/usa/east" or pathname == f"/usa/east/ny":
        return usa_east
    elif pathname == f"/usa/west" or pathname == f"/usa/west/la":
        return usa_west


@callback(
          Output("usa_tab-content", "children"),
          [Input("tabs", "active_tab")],
          )

def render_tab_content(active_tab):

    if active_tab:
        if active_tab == "usa_east_ny_id":
            return usa_east_ny_content
        elif active_tab == "usa_east_philly_id":
            return usa_east_philly_content
        elif active_tab == "usa_west_la_id":
            return usa_west_la_content
        elif active_tab == "usa_west_sa_id":
            return usa_west_sa_content
