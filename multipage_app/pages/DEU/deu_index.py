import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback

from pages.DEU.deu_east_berlin_tab import get_deu_east_berlin_content
from pages.DEU.deu_east_leipzig_tab import get_deu_east_leipzig_content
from pages.DEU.deu_west_koln_tab import get_deu_west_koln_content
from pages.DEU.deu_west_frankfurt_tab import get_deu_west_frankfurt_content

from styles_info import get_styles_info

dash.register_page(__name__, name='DEU', path = '/DEU')

SIDEBAR_STYLE, CONTENT_STYLE = get_styles_info()

sidebar = html.Div(
                    [
                        html.H2("GERMANY Cities", className="display-8"),
                        html.Hr(),
                        html.P("Information on GERMANY cities", className="lead"),
                        dbc.Nav(
                                [dbc.NavLink("East", href=f"/DEU/east/berlin", active="exact"),
                                 dbc.NavLink("West", href=f"/DEU/west/koln", active="exact"),
                                ],
                                vertical=True,
                                pills=True,
                                 ),
                    ],
    style=SIDEBAR_STYLE,
)

deu_east = html.Div([
                    dbc.Tabs(
                                [
                                dbc.Tab(label="BERLIN", tab_id="deu_east_berlin_id"),
                                dbc.Tab(label="LEIPZIG", tab_id="deu_east_leipzig_id"),
                                ],
                                id="tabs",
                                active_tab="deu_east_berlin_id",
                             ),
                    html.Div(id="deu_tab-content", className="p-4"),
                    ])

deu_west = html.Div([
                            dbc.Tabs(
                                    [
                                    dbc.Tab(label="KOLN", tab_id="deu_west_koln_id"),
                                    dbc.Tab(label="FRANKFURT", tab_id="deu_west_frankfurt_id"),
                                    ],
                                    id="tabs",
                                    active_tab="deu_west_koln_id",
                                     ),
                            html.Div(id="deu_tab-content", className="p-4"),
                    ])

content = html.Div(id="deu_page_content", style=CONTENT_STYLE)

layout = html.Div([dcc.Location(id="deu_url"), sidebar, content])

deu_east_berlin_content = get_deu_east_berlin_content()
deu_east_leipzig_content = get_deu_east_leipzig_content()

deu_west_koln_content = get_deu_west_koln_content()
deu_west_frankfurt_content = get_deu_west_frankfurt_content()

@callback(
          Output("deu_page_content", "children"),
          [Input("deu_url", "pathname")])

def render_page_content(pathname):
    if pathname == f"/DEU" or pathname == f"/DEU/east" or pathname == f"/DEU/east/berlin":
        return deu_east
    elif pathname == f"/DEU/west" or pathname == f"/DEU/west/koln":
        return deu_west


@callback(
    Output("deu_tab-content", "children"),
    [Input("tabs", "active_tab")])

def render_tab_content(active_tab):

    if active_tab:
        if active_tab == "deu_east_berlin_id":
            return deu_east_berlin_content
        elif active_tab == "deu_east_leipzig_id":
            return deu_east_leipzig_content
        elif active_tab == "deu_west_koln_id":
            return deu_west_koln_content
        elif active_tab == "deu_west_frankfurt_id":
            return deu_west_frankfurt_content
