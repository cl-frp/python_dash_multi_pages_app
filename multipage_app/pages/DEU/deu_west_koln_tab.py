def get_deu_west_koln_content():

    from dash import dcc, html, Input, Output, callback
    import plotly.express as px
    import pandas as pd

    avocado = pd.read_csv('https://raw.githubusercontent.com/chainhaus/pythoncourse/master/avocado.csv')

    geo_dropdown_koln = dcc.Dropdown(options=avocado['region'].unique(),
                                value='Albany')

    layout = html.Div(children=[
                                html.H1(children='DEU West Koln'),
                                geo_dropdown_koln,
                                dcc.Graph(id='deu_west_koln_graph')
                                ]
                      )

    @callback(
                Output(component_id='deu_west_koln_graph', component_property='figure'),
                Input(component_id=geo_dropdown_koln, component_property='value')
             )

    def update_graph(selected_geography):

        filtered_avocado = avocado[avocado['region'] == selected_geography]
        line_fig = px.line(filtered_avocado,
                           x='date', y='average_price',
                           color='type',
                           title=f'Information about the City of Koln')
        return line_fig

    return layout