import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
                        html.H1('World App'),

                        dbc.Navbar(
                            [
                                dbc.Button(f"{page['name']}",
                                                       href=page["relative_path"],
                                                       color="primary",
                                                       className="me-1")
                                for page in dash.page_registry.values()
                            ],
                        ),

                        dash.page_container,

                        ])


if __name__ == '__main__':

    app.run_server()
