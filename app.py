from re import template
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)

app = Dash(__name__)

data = pd.read_csv("42_Cases_under_crime_against_women.csv")

dt4= data.groupby(["Sub_Group_Name","Area_Name"],as_index=False).mean()
dtx=dt4.groupby(["Sub_Group_Name"],as_index=False).sum()
dty=data.groupby(["Sub_Group_Name"],as_index=False).sum()

crimesGroups = ['01. Rape', 
'02. Kidnapping & Abduction of Women & Girls', 
'03. Dowry Deaths', 
'04. Molestation', 
'05. Sexual Harassment', 
'06. Cruelty by Husband and Relatives', 
'07. Importation of Girls', 
'08. Immoral Traffic Prevention Act', 
'09. Dowry Prohibition Act', 
'10. Indecent Representation of Women(Prohibition) Act', 
'11. Sati Prevention Act']

crimeMarks = ['Rape', 
'Kidnapping & Abduction of Women & Girls', 
'Dowry Deaths', 
'Molestation', 
'Sexual Harassment', 
'Cruelty by Husband and Relatives', 
'Importation of Girls', 
'Immoral Traffic Prevention Act', 
'Dowry Prohibition Act', 
'Indecent Representation of Women(Prohibition) Act', 
'Sati Prevention Act']

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div(
    className="main",
    children=[

    html.H1(
        className="title",
        children="Crimes against women in india"),

    html.Div(
        className="chloro-box",
        children=[
            
            html.Div(
                className="graph-card side",
                children=[
                    dcc.Slider(
                        0, 10, 1, value=0,
                        className="slider",
                        id="slct_year",                
                        marks={
                        i: {'label': crimeMarks[i], 'style': {'width': 200}}
                        for i in range(0, 11)},
                        included= False,
                        vertical=True),
                        html.Div(
                            [
                                html.Div(
                                    className="info-box",
                                    children=[
                                        html.Div(
                                            className="box",
                                            children=[
                                                html.H3("Average cases in India over 10 years", style={"padding-bottom": "15px"}),
                                                html.H3(id="avg-cases", children="", style={}),
                                            ]
                                        ),
                                        html.Div(
                                            className="box",
                                            children=[
                                                html.H3("State with maximum cases", style={"padding-bottom": "15px"}),
                                                html.H3(id="max-cases", children="", style={"color": "red"}),
                                            ]
                                        ),
                                        html.Div(
                                            className="box",
                                            children=[
                                                html.H3("State with minimum cases", style={"padding-bottom": "15px"}),
                                                html.H3(id="min-cases", children="", style={"color": "green"}),
                                            ]
                                        ),
                                    ]
                                ),
                                
                                dcc.Graph(id='graph_1', figure={}),
                            ]
                        ),
                        
                ]
            ),
        ]
    ),

    
    
    html.Div(
        className="grid",
        children=[
            html.Div(
                className="graph-card-2",
                children=[
                    dcc.Graph(id='graph_2', figure={}),
                ]
            ),

            html.Div(
                className="graph-card-2",
                children=[
                    dcc.Graph(id='graph_3', figure={})
                ]
            ),
            
        ]
    ),

    html.Div(
                className="graph-card",
                children=[
                    dcc.Graph(id='graph_4', figure={})
                ]
            ),

    html.Div(
                className="graph-card",
                children=[
                    dcc.Graph(id='graph_5', figure={})
                ]
            ),

    html.Div(
        className="grid",
        children=[
            html.Div(
                className="graph-card-2",
                children=[
                    dcc.Graph(id='graph_6', figure={})
                ]
            ),

            html.Div(
                className="graph-card-2",
                children=[
                    dcc.Graph(id='graph_7', figure={})
                ]
            ),
            
        ]
    ),

    

    html.Div(
                className="names-list",
                children=[
                    html.H1("Team Guard", className="team-title"),
                    html.Div(
                        className="team-names",
                        children=[
                            html.Div(
                                className="teammate",
                                children=[
                                    html.Img(
                                        src="assets/Khushang.jpg",
                                        className="photo",
                                        alt="photo",
                                    ),
                                    html.H3("Khushang Thakkar", className="name"),
                                    html.H3("20BCE2014", className="name"),
                                ]
                            ),
                            html.Div(
                                className="teammate",
                                children=[
                                    html.Img(
                                        src="assets/Prarthavi.jpg",
                                        className="photo",
                                        alt="photo",
                                    ),
                                    html.H3("Prarthavi Garge", className="name"),
                                    html.H3("20BCE0420", className="name"),
                                ]
                            ),
                            html.Div(
                                className="teammate",
                                children=[
                                    html.Img(
                                        src="assets/Tirth.jpg",
                                        className="photo",
                                        alt="photo",
                                    ),
                                    html.H3("Tirth Patel", className="name"),
                                    html.H3("20BCE2022", className="name"),
                                ]
                            ),
                            html.Div(
                                className="teammate",
                                children=[
                                    html.Img(
                                        src="assets/Sachi.jpg",
                                        className="photo",
                                        alt="photo",
                                    ),
                                    html.H3("Sachi Kaushik", className="name"),
                                    html.H3("20BCE2481", className="name"),
                                ]
                            ),
                            html.Div(
                                className="teammate",
                                children=[
                                    html.Img(
                                        src="assets/Prakhar.jpg",
                                        className="photo",
                                        alt="photo",
                                    ),
                                    html.H3("Prakhar", className="name"),
                                    html.H3("20BCE2113", className="name"),
                                ]
                            ),
                        ]
                    ),
                    html.H4("Made with 📈", style={"text-align": "center", "color": "white","padding-top": "50px"}),
                ]
            ),
    

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        Output(component_id='avg-cases', component_property='style'),
        Output(component_id='avg-cases', component_property='children'),
        Output(component_id='max-cases', component_property='children'),
        Output(component_id='min-cases', component_property='children'),
        Output(component_id='graph_1', component_property='figure'),
        Output(component_id='graph_2', component_property='figure'),
        Output(component_id='graph_3', component_property='figure'),
        Output(component_id='graph_4', component_property='figure'),
        Output(component_id='graph_5', component_property='figure'),
        Output(component_id='graph_6', component_property='figure'),
        Output(component_id='graph_7', component_property='figure'),
    ],
    Input(component_id='slct_year', component_property='value')
)
def update_graph(option_slctd):
    d = dt4[dt4["Sub_Group_Name"]==crimesGroups[option_slctd]]

    dtot = dtx[dtx["Sub_Group_Name"]==crimesGroups[option_slctd]]['Cases_Reported'].values[0]
    dtot = round(dtot, 2)

    y=dt4[(dt4["Sub_Group_Name"]==crimesGroups[option_slctd])]

    maxState=""
    minState=""
    
    maxState = y[(y['Cases_Reported']==y['Cases_Reported'].max())]["Area_Name"].values[0]
    minState = y[(y['Cases_Reported']==y['Cases_Reported'].min())]["Area_Name"].values[0]


    color = "white"

    if(dtot<1000):
        color = "green"
    elif(dtot<10000):
        color = "yellow"
    elif(dtot<20000):
        color = "orange"
    else:
        color = "red"

    style = {"color": color}
    

    fig = px.choropleth(
        d,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='Area_Name',
        color='Cases_Reported',
        color_continuous_scale='YlOrBr',
        template="plotly_dark",
        title="Crimewise heatmap in all of India: {}".format(crimeMarks[option_slctd]),
    )

    fig.update_geos(fitbounds="geojson", visible=False)

    #----------------------------------------------------------------------------------------------------------------------------------------

    g = pd.DataFrame(data.groupby(['Year'])['Cases_Reported'].sum().reset_index())
    g.columns = ['Year', 'Total Cases Reported']
    fig2 = px.bar(g,x='Year',y='Total Cases Reported',color='Total Cases Reported', text_auto='.2s', title="Yearwise total cases reported", template="plotly_dark")

    #----------------------------------------------------------------------------------------------------------------------------------------

    dt3=data.groupby(["Year"],as_index=False).sum()
    dt3["Difference"]=dt3["Cases_Reported"]-dt3["Cases_Sent_for_Trial"]
    dt3=dt3[["Year","Cases_Reported","Cases_Sent_for_Trial","Difference"]]
    fig3 = px.bar(dt3,x='Year',y='Difference',color='Difference', text_auto='.2s',template="plotly_dark",title="Yearwise difference between cases reported and cases sent for trial")

    #----------------------------------------------------------------------------------------------------------------------------------------

    dt2 = pd.DataFrame(data.groupby(['Group_Name','Year'])['Cases_Reported'].sum().reset_index())

    fig4 = px.line(dt2, x=dt2.Year, y=dt2.Cases_Reported, color=dt2.Group_Name, template="plotly_dark", title="Crimewise cases reported", height=600)

    #----------------------------------------------------------------------------------------------------------------------------------------

    dt=data.groupby(["Area_Name"]).mean().round()
    q1=dt[["Cases_Convicted", "Cases_Reported"]]

    states=data.Area_Name

    fig5 = go.Figure(data=[
        go.Bar(name='Cases Reported', x=states, y=q1['Cases_Reported']),
        go.Bar(name='Cases Convicted', x=states, y=q1['Cases_Convicted'])
    ])

    fig5.update_layout(barmode='group', xaxis_title='State', yaxis_title='Number of cases', template="plotly_dark", title="Statewise mean cases reported vs cases convicted", height= 600)

    #----------------------------------------------------------------------------------------------------------------------------------------

    fig6 = px.scatter(
        data, x='Cases_Pending_Investigation_at_Year_End', y='Cases_Pending_Trial_at_Year_End', opacity=0.65,
        trendline='ols', trendline_color_override='darkred', animation_frame="Year", title="Yearwise regression between pending investigations and pending trials", template="plotly_dark",
    )

    #----------------------------------------------------------------------------------------------------------------------------------------

    d1=data[["Year","Area_Name","Cases_Reported","Cases_Convicted","Total_Cases_for_Trial","Cases_Compounded_or_Withdrawn"]]
    fig7 =  px.imshow(d1.corr(), template="plotly_dark", title="Correlation between all variables", color_continuous_scale='YlOrBr')
    
    #----------------------------------------------------------------------------------------------------------------------------------------

    return style, dtot, maxState, minState, fig, fig2, fig3, fig4, fig5, fig6, fig7


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server()