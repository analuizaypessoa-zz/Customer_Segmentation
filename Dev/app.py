# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

## load data and build the plots
#EXAMPLE PLOT
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
df3 = pd.read_csv("../Outputs/Clusters_Mode.csv", index_col=[0])
fig = px.bar(df, y="Fruit", x="Amount", color="City", barmode="group")
## Plot related to the analisys
categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig2 = go.Figure()

fig2.add_trace(go.Scatterpolar(
      r=[1, 5, 2, 2, 3],
      theta=categories,
      fill='toself',
      name='Product A'
))
fig2.add_trace(go.Scatterpolar(
      r=[4, 3, 2.5, 1, 2],
      theta=categories,
      fill='toself',
      name='Product B'
))

fig2.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)


## PIE CHART OF CLUSTERS
df2 = pd.read_csv("../Outputs/Clusters_Mode.csv", index_col=[0]) ## read df
df2 = df2[['Labels', 'GENDER', 'AGE', 'EMPLOYMENT', 'INCOME', 'FREQUENCY_VISIT',
       'TIME_PER_VISIT',
       'DISTANCE_TO_NEAREST_STORE', 'MEMBER', 'SPEND_PER_VISIT', 
    'FG_DIGITAL_MEDIA', 
       'FG_FISIC']] ### selecting the desired columns to show
df2= df2.sort_values(by = 'Labels')
df3 = df2['Labels'].value_counts()
df3 = df3.reset_index(name = 'Contagem')
fig3 = px.pie(df3, values='Contagem', names='index', title='Population of European continent')
available_indicators = df2["INCOME"].unique()
## TABLE CLUSTERS RESULTS
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ], style = {"background-color": "#f5f5f5",
                "font-size":"0.75vw",
                "border-bottom": "1px solid #ddd",
                "width": "100vw",
                "height": "100vh"}
    )


app.layout = html.Div(children=[

    html.Nav(className = "nav nav-pills"),
    html.H1(children='Customer Segmentation - Starbucks', style = {
                                                        "color": "white",
                                                        "text-align" : "center",
                                                        "font-size": "28px",
                                                        "background-color":"darkgreen",
                                                        "display":"flex",
                                                        "height":"70px",
                                                        "margin": "0"
                                                        }),
    html.Div(children='''
        This dash presents the results of a customer segmentation project based on a starbucks survey
    ''',
    style = {"background-color":"gainsboro","color": "black", "font-size": "15px", "height":"45px", "margin":"0"}
    ),

    html.Div(children = [  
            html.Div(children = [
                html.Br(),
                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': u'Montréal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                ],
                value=['MTL', 'SF'],
                multi=True
                ),
                html.Br(),
                html.Label('Text Input'),
                dcc.Input(value='MTL', type='text'),
                html.Br(),
                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                    value=5,),
                html.Br(),
                dcc.RadioItems( options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}],
                    value='MTL'),
                html.Br(),
                dcc.Dropdown(id = "drop_down_2", options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ], value= "MTL")
                    ],
                                        style = {
                                            "text-align": "center",
                                            "height":"460px",
                                            "background-color":"whitesmoke",
                                            "margin": "0",
                                            "padding": "0",
                                            
                                        }
                ),
            dcc.Graph(
                id='example-graph',
                figure=fig2,
                ),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='total_income'
            ),

        ], style = {"width": "100%", "paffing": 10, 'columnCount': 2 } ),

    html.H4(children='Mode of Variables per cluster', 
    style = {"background-color":"gainsboro","color": "black", "font-size": "24px", "height":"60px", "margin":"0"}
    ),
    generate_table(df2)
], style = {"width": "100%", "paffing": 10, 'columnCount': 1 })

if __name__ == '__main__':
    app.run_server(debug=True)