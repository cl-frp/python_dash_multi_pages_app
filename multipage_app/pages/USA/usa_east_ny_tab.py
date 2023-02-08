
def get_usa_east_ny_content():
    
    from dash import dcc, html, Input, Output, callback
    import plotly.express as px
    import pandas as pd

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    layout = html.Div([
                        dcc.Graph(id='usa_east_ny_graph'),
                        dcc.Slider(
                                    df['year'].min(),
                                    df['year'].max(),
                                    step=None,
                                    value=df['year'].min(),
                                    marks={str(year): str(year) for year in df['year'].unique()},
                                    id='year-slider-ny'
                                    )
                        ])

    @callback(
                Output('usa_east_ny_graph', 'figure'),
                Input('year-slider-ny', 'value')
             )

    def update_figure(selected_year):

        filtered_df = df[df.year == selected_year]

        fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                         size="pop", color="continent", hover_name="country",
                         log_x=True, size_max=55)

        fig.update_layout(transition_duration=500)

        return fig

    return layout