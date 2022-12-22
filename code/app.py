import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import pandas as pd
from utils import compare_stats, get_player, get_all_players
from components.buttons_stats import ButtonsStats
from components.stats_graph import GraphStats
from components.player_shooting_court import PlayerShootingCourt
from components.player_card import PlayerCard
from components.stats_array import StatsArray

from data_api import DataAPI

start_year = 2012
end_year = 2022
players_names_list = get_all_players(start_year=2022, end_year=2023)
slider_years = pd.DataFrame({'year': range(start_year, end_year+1)})

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

server = app.server

app.layout = dbc.Container(
    [
        # TITLE
        html.Br(),
        html.H2("NBA Player Tracker", style={'text-align': 'center'}),
        html.Br(),
        dbc.Row(
            [
                # DATATABLE
                dbc.Col(dbc.Card(([
                    dbc.CardBody(
                        [
                            html.H5("Last season data"),
                            html.Div(StatsArray()),
                        ],
                        style={'background-color': '#F7F7F7'},
                    ),
                ]),
                style={'margin-left': '25px', 'margin-right': '25px'},),
                ),
            ],
            align="start",
        ),
        html.Br(),
        html.Br(),
        
        dbc.Card([
            dbc.CardHeader([
                html.H5("Players comparison"),]),
        # YEARS RANGE SLIDER
        dbc.Row(
        dcc.RangeSlider(slider_years['year'].min(), slider_years['year'].max(),
            step=None,
            id='year-range-slider',
            value=[slider_years['year'].min(), slider_years['year'].max()],
            marks={str(year): str(year)+"\u02D7"+str(abs(year+1) % 100) for year in slider_years['year'].unique()},
            #pushable=1
            ),
        style={'margin-top': '25px', 'margin-left': '25px', 'margin-right': '25px'},),


        dbc.RadioItems(
            value=None,
            id='dropdown-stat'
        ),
        html.Br(),
        html.Br(),

        dbc.Row(
            [   
                # PLAYER 1
                dbc.Col(dbc.Card([
                    dbc.CardHeader([
                        dcc.Dropdown(players_names_list, id='player_1_dropdown', value=players_names_list[0]["value"],placeholder="Select a player", style={
                                     'color': 'black', 'font-size': 20}),
                    ]),
                    dbc.CardBody(dbc.Row([
                        dbc.Col(
                            id="player_1_card"
                        ),
                        dbc.Col(
                            id="player_1_shots"
                        ),

                    ], align="center",))
                ])),
                
                # PLAYER 2
                dbc.Col(dbc.Card([
                    dbc.CardHeader([
                        dcc.Dropdown(players_names_list, id='player_2_dropdown', value=players_names_list[1]["value"],placeholder="Select a player", style={
                                     'color': 'black', 'font-size': 20}),
                    ]),
                    dbc.CardBody(dbc.Row([
                        dbc.Col(
                            id="player_2_card"
                        ),
                        dbc.Col(
                            id="player_2_shots"
                        ),

                    ], align="center"))
                ])),
            ],
            align="center",
            style={'margin-left': '25px', 'margin-right': '25px'},
        ),
        html.Br(),
        html.Br(),
        
        # GRAPH STATS
        dbc.Row(
            [
                dbc.Col(dbc.Card([
                    dbc.CardHeader([
                        html.H5("Statistics evolution"),
                    ]),
                    dbc.CardBody(id="buttons_stats"),
                    dbc.CardBody(id="graph_stats")
                ]), style={}),
            ],
            align="center",
        style={'margin-left': '25px', 'margin-right': '25px', 'margin-bottom': '25px'},),
    ],
    style={'margin-left': '25px', 'margin-right': '25px', 'margin-bottom': '25px'},
    ),],
    className="pad-row",
    fluid=True,
)


# PLAYERS CALLBACK
@app.callback(
    Output('player_1_card', 'children'), Output('player_2_card', 'children'), Output(
        'player_1_shots', 'children'), Output('player_2_shots', 'children'),Output('buttons_stats', 'children'),
    [Input('player_1_dropdown', 'value'), Input('player_2_dropdown', 'value'), Input('year-range-slider', 'value')])
def update_card_player(player_1_id, player_2_id, year_range):
        player_1 = get_player(1, player_1_id, year_range, None)
        player_2 = get_player(2, player_2_id, year_range, None)
        return PlayerCard(player_1, compare_stats(player_1, player_2)), PlayerCard(player_2, compare_stats(player_2, player_1)), PlayerShootingCourt(player_1), PlayerShootingCourt(player_2), ButtonsStats()

# STATS GRAPH CALLBACK
@app.callback(
    Output('graph_stats', 'children'),Output('dropdown-stat', 'value'),
    [Input('player_1_dropdown', 'value'), Input('player_2_dropdown', 'value'), Input('year-range-slider', 'value'), Input('dropdown-stat', 'value')])
def update_stats_graph(player_1_id, player_2_id, year_range, stat):
    if stat is not None:
        player_1 = get_player(1, player_1_id, year_range, stat)
        player_2 = get_player(2, player_2_id, year_range, stat)
        return GraphStats(player_1, player_2),stat
    return None,None

if __name__ == "__main__":
    app.run_server()