import pandas as pd 
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

df_us = pd.read_csv('fg_us_240917.csv')
#df_kor = 
df_crypto = pd.read_csv('fg_crypto_240917.csv')

date_show = df_us.iloc[-1]['Date']
value_show = int(df_us.iloc[-1]['fear_and_greed_historical'])
cat_show = df_us.iloc[-1]['rating']

value_show2 = df_crypto.iloc[-1]['value']
cat_show2 = df_crypto.iloc[-1]['value_classification']

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

fig1 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_show,
    mode = "gauge+number",
    title = {'text': "Fear and Greed (US)"},
    #title = dict(text= 'FAST', x=0.5, y=0.25, font=dict(size=70)),
    #delta = {'reference': 40},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 100}}))

fig2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_show2,
    mode = "gauge+number",
    title = {'text': "Fear and Greed (Crypto)"},
    #title = dict(text= 'FAST', x=0.5, y=0.25, font=dict(size=70)),
    #delta = {'reference': 40},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 100}}))

fig0 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = value_show2,
    mode = "gauge+number",
    title = {'text': "Fear and Greed (KOR)"},
    #title = dict(text= 'FAST', x=0.5, y=0.25, font=dict(size=70)),
    #delta = {'reference': 40},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 50], 'color': "lightgray"},
                 {'range': [50, 100], 'color': "gray"}],
            'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 100}}))

fig0.update_layout(margin=dict(l=30, r=30, t=0, b=0))
fig1.update_layout(margin=dict(l=30, r=30, t=0, b=0))
fig2.update_layout(margin=dict(l=30, r=30, t=0, b=0))

fig_us_timeseries = px.scatter(df_us, x='Date', y='fear_and_greed_historical', color='rating',
                                template='simple_white')

fig_us_timeseries.update_layout(
    title_text = "CNN Fear & Greed Timeline (전체)",
    margin=dict(l=20, r=20, t=30, b=0),
)

app.layout = html.Div(
    [
        dbc.Stack([
            html.Div(html.H2("Market Sentiment Indicator" + " " + date_show)),
            html.Div(
                dbc.Row(
                [
                    dbc.Col(dcc.Graph(figure=fig0), width=4),
                    dbc.Col(dcc.Graph(figure=fig1), width=4),
                    dbc.Col(dcc.Graph(figure=fig2), width=4)
                ],
                align="center", className="g-0"
                )
            ),
            html.Div(
                dbc.Row(
                #dash_table.DataTable(data=df_us.to_dict('records'), page_size=10)
                dcc.Graph(figure=fig_us_timeseries)
                )
            ),
        ],gap=0
        )
    ], style={'padding': '0px 20px 20px 20px'}
)

# app.layout = html.Div(
#     [
#         html.H2("Market Sentiment Indicator" + " " + date_show),
#         dbc.Row(
#             [
#                 dbc.Col(dcc.Graph(figure=fig0), width=4),
#                 dbc.Col(dcc.Graph(figure=fig1), width=4),
#                 dbc.Col(dcc.Graph(figure=fig2), width=4)
#             ],
#             align="center",
#         ),

#         dbc.Row(
#             #dash_table.DataTable(data=df_us.to_dict('records'), page_size=10)
#             dcc.Graph(figure=fig_us_timeseries)
#         )
#     ]
# )

if __name__ == '__main__':
    app.run(debug=True, )