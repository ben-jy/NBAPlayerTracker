from utils import config
from dash import html
import dash_bootstrap_components as dbc


class PlayerCard(html.Div):

    def __init__(
        self,
        player,
        compare_stats,
    ):

        if player is None:
            super().__init__([
              ])
            return

        score_color = get_score_color(player["info"]["score"], 5.8, 9.6)
        update_salary(player)
        color = get_color(player["card_id"])

        height_style = get_stats_styles(compare_stats["height"])
        weight_style = get_stats_styles(compare_stats["weight"])
        points_style = get_stats_styles(compare_stats["PTS"])
        rebounds_style = get_stats_styles(compare_stats["REB"])
        assists_style = get_stats_styles(compare_stats["AST"])
        blocks_style = get_stats_styles(compare_stats["BLK"])
        steals_style = get_stats_styles(compare_stats["STL"])
        turnovers_style = get_stats_styles(compare_stats["TOV"])
        fg_pourcentage_style = get_stats_styles(compare_stats["FG%"])
        tree_fg_pourcentage_style = get_stats_styles(compare_stats["3P%"])
        ft_pourcentage_style = get_stats_styles(compare_stats["FT%"])

        # Define the component's layout
        super().__init__([
            dbc.Card(
                [
                    # dbc.CardHeader([
                    #     dbc.Row(
                    #         [
                    #             dbc.Col(
                    #                 html.H4(player["info"]["first_name"] + " " + player["info"]["last_name"]),
                    #             ),
                    #         ],
                    #         justify="between",
                    #     ),
                    # ]),
                    dbc.CardBody([
                            # player infos
                            dbc.Row([
                                dbc.Col(html.Div(html.Img(src="https://cdn.nba.com/headshots/nba/latest/1040x760/"+str(player["id"])+".png", style={
                                    'height': '80%', 'width': '80%'})), className="col-md-4"),

                                dbc.Col([
                                    html.P(player["info"]["team"],
                                        className="card-text",),
                                    html.P(player["info"]["position"],
                                        className="card-text",),
                                    html.P(player["info"]["salary"],
                                        className="card-text",),
                                ],
                                    className="col-md-5"),
                                dbc.Col(
                                    html.H3(["",
                                            dbc.Badge(
                                                player["info"]["score"], color=score_color)]),
                                    align="right", width=2),
                            ]
                            ),

                            html.Br(),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    html.P("Height", className="card-text",),
                                    html.P("Weight", className="card-text",),
                                ],
                                    width=5),
                                dbc.Col([
                                    html.P(player["info"]["height"].split("-")[0] + " ' " + player["info"]["height"].split("-")[1] + "''",
                                        className="card-text",),
                                    html.P(str(player["info"]["weight"])+" lbs",
                                        className="card-text",),
                                ],
                                    width=4),
                                dbc.Col([
                                    html.P(className=height_style[0], style={
                                        "color": height_style[1]}),
                                    html.P(className=weight_style[0], style={
                                        "color": weight_style[1]}),
                                ],
                                    width=2),

                            ]
                            ),
                            html.Hr(),

                            # player stats
                            dbc.Row([
                                # labels collumn
                                dbc.Col([
                                    html.P("Points", className="card-text",),
                                    html.P("Rebounds", className="card-text",),
                                    html.P("Assists", className="card-text",),
                                    html.P("Steals", className="card-text",),
                                    html.P("Blocks", className="card-text",),
                                    html.P("Turnovers",className="card-text",),
                                    html.P("FG%", className="card-text",),
                                    html.P("3P%", className="card-text",),
                                    html.P("FT%", className="card-text",),
                                ],
                                    width=5),
                                # values collumn
                                dbc.Col([
                                    html.P(round(player["stats"]["PTS"], 1),
                                        className="card-text",),
                                    html.P(round(player["stats"]["REB"], 1),
                                        className="card-text",),
                                    html.P(round(player["stats"]["AST"], 1),
                                        className="card-text",),
                                    html.P(round(player["stats"]["STL"], 1),
                                        className="card-text",),
                                    html.P(round(player["stats"]["BLK"], 1),
                                        className="card-text",),
                                    html.P(round(player["stats"]["TOV"], 1),
                                        className="card-text",),
                                    html.P(str(round(player["stats"]["FG%"]*100, 1))+"%",
                                        className="card-text",),
                                    html.P(str(round(player["stats"]["3P%"]*100, 1))+"%",
                                        className="card-text",),
                                    html.P(str(round(player["stats"]["FT%"]*100, 1))+"%",
                                        className="card-text",),
                                ],
                                    width=4),
                                dbc.Col([
                                    html.P(className=points_style[0], style={
                                        "color": points_style[1]}),
                                    html.P(className=rebounds_style[0], style={
                                        "color": rebounds_style[1]}),
                                    html.P(className=assists_style[0], style={
                                        "color": assists_style[1]}),

                                    html.P(className=blocks_style[0], style={
                                        "color": blocks_style[1]}),
                                    html.P(className=steals_style[0], style={
                                        "color": steals_style[1]}),
                                    html.P(className=turnovers_style[0], style={
                                        "color": turnovers_style[1]}),

                                    html.P(className=fg_pourcentage_style[0], style={
                                        "color": fg_pourcentage_style[1]}),

                                    html.P(className=tree_fg_pourcentage_style[0], style={
                                        "color": tree_fg_pourcentage_style[1]}),

                                    html.P(className=ft_pourcentage_style[0], style={
                                        "color": ft_pourcentage_style[1]}),
                                ],
                                    width=2),
                            ]
                            ),
                        ],
                        style={'min-width': '300px'},
                    ),                    
                ],
                outline=True,
                style={
                    "border-color": color,
                    "border-width": "2px",
                    },
            )
        ])


def get_score_color(score, min, max):
    if score >= min and score < min+((max - min) / 3):
        color="red"
    elif score >= min+(max - min) / 3 and score < min+(max - min) * 2/3:
        color="orange"
    else:
        color="success"
    return color

def get_color(id):
    if id == 1:
        color=config["PLAYER_1_COLOR"]
    elif (id == 2):
        color=config["PLAYER_2_COLOR"]
    else:
        color="red"
    return color


def get_stats_styles(compare_value):
    if compare_value > 0:
        return ["bi bi-arrow-bar-up", "green"]
    elif compare_value < 0:
        return ["bi bi-arrow-bar-down", "red"]
    else:
        return ["bi bi-dash", "orange"]

def update_salary(player):
    # Remove the $ sign
    player["info"]["salary"] = player["info"]["salary"][1:]

    # Transform the salary into an integer
    player["info"]["salary"]=int(player["info"]["salary"].replace(",", ""))

    # Transform the salary into a string with the $ sign and the format 1'000'000
    player["info"]["salary"]='{:,}'.format(
        player["info"]["salary"]).replace(',', "'") + '$'
