def get_usa_west_la_content():

    from dash import dcc, html, Input, Output, callback
    import plotly.express as px
    import pandas as pd

    avocado = pd.read_csv('https://raw.githubusercontent.com/chainhaus/pythoncourse/master/avocado.csv')

    geo_dropdown_la = dcc.Dropdown(options=avocado['region'].unique(),
                                value='Albany')

    layout = html.Div(children=[
        html.H1(children='USA West Los Angeless'),
        geo_dropdown_la,
        dcc.Graph(id='usa_west_la_graph')
    ])

    @callback(
                Output(component_id='usa_west_la_graph', component_property='figure'),
                Input(component_id=geo_dropdown_la, component_property='value')
             )

    def update_graph(selected_geography):

        filtered_avocado = avocado[avocado['geography'] == selected_geography]
        line_fig = px.line(filtered_avocado,
                           x='date', y='average_price',
                           color='type',
                           title=f'Information about the City of Los Angeles')

        return line_fig

    return layout