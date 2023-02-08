def get_usa_west_sa_content():

    from datetime import datetime, timedelta
    import pandas as pd
    import plotly.express as px
    from dash import dcc, Output, Input, callback
    from dash import html

    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
    data = pd.read_csv(url, sep=",")
    df = data.copy()
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d %H:%M:%S.%f')

    init_start_date = df['Date'].min().strftime('%Y-%m-%d')
    init_end_date = df['Date'].max().strftime('%Y-%m-%d')

    layout = html.Div(children=[
                                dcc.DatePickerRange(
                                                    id='date-picker-range-sa',
                                                    start_date=init_start_date,
                                                    end_date=init_end_date,
                                                    minimum_nights=0,
                                                    display_format='YYYY/MM/DD'
                                                    ),
                                dcc.Graph(id='usa_west_sa_graph'),
                                ])

    @callback(
                Output('usa_west_sa_graph', 'figure'),
                Input('date-picker-range-sa', 'start_date'),
                Input('date-picker-range-sa', 'end_date')
             )

    def update_figure(start_date, end_date):

        if start_date is not None and end_date is not None:
            start_date = datetime.fromisoformat(start_date)
            end_date = datetime.fromisoformat(end_date) + timedelta(days=1)
            filtered_df = df[(start_date <= df['Date']) & (df['Date'] <= end_date)]
            scatter_fig_sa = px.scatter(filtered_df, x='Date', y=['DATA 1', 'DATA 2', 'DATA 3', 'DATA 4'])

            return scatter_fig_sa

    return layout