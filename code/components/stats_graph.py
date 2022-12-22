from dash import html, dcc
import plotly.graph_objs as go
from utils import config

class GraphStats(html.Div):
    def __init__(
        self,
        player1_stats,
        player2_stats,
    ):
        if player1_stats is None and player2_stats is None:
            super().__init__([
            ])
            return

        fig = go.Figure()

        if player1_stats is not None and player2_stats is not None:
            self.add_player_stat_trace(fig, player1_stats)
            self.add_player_stat_trace(fig, player2_stats)
        elif player1_stats is not None and player2_stats is None:
            self.add_player_stat_trace(fig, player1_stats)
        elif player1_stats is None and player2_stats is not None:
            self.add_player_stat_trace(fig, player2_stats)

        #fig.update_layout(template='plotly_dark')
        
        super().__init__([
            dcc.Graph(
                figure=fig
            ),

        ])

    def add_player_stat_trace(self, fig, player):
            fig.update_layout(
                margin=dict(l=20, r=20, t=20, b=20),
            )
            if len(player["stat_evolution"].keys()) != 1:
                    fig.add_trace(go.Scatter(
                        x=list(player["stat_evolution"].keys()),
                        y=list(player["stat_evolution"].values()),
                        name=player["info"]["first_name"] +
                        " " + player["info"]["last_name"],
                        marker_color=get_color(player["card_id"]),
                        line=dict(color=get_color(player["card_id"]), dash=get_line_style(player["card_id"]))
                        ))
            else:
                fig.add_trace(go.Scatter(
                    x=list(player["stat_evolution"].keys()),
                    y=list(player["stat_evolution"].values()),
                    name=player["info"]["first_name"] +
                    " " + player["info"]["last_name"],
                    marker_color=get_color(player["card_id"]),
                    mode='markers'
                    ))
        

def get_color(id):
    if id == 1:
        color = config["PLAYER_1_COLOR"]
    elif (id == 2):
        color = config["PLAYER_2_COLOR"]
    else:
        color = "red"
    return color

def get_line_style(id):
    if id == 1:
        dash = 'solid'
    elif (id == 2):
        dash = 'dot'
    else:
        dash = "dash"
    return dash