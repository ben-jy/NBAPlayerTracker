import dash_bootstrap_components as dbc
from dash import html, dash_table
from data_api import DataAPI
import pandas as pd

class StatsArray(html.Div):
 
    def __init__(
        self,
    ):
    
        df_stats = get_players_stats()

        super().__init__([
                dash_table.DataTable(
                        data=df_stats.to_dict("records"),
                        columns=[
                            {"name": "First Name", "id": "first_name"},
                            {"name": "Last Name", "id": "last_name"},
                            {"name": "Position", "id": "position"},
                            {"name": "Team", "id": "team"},
                            {"name": "Salary", "id": "salary"},
                            {"name": "Score", "id": "score"},
                            {"name": "Points", "id": "PTS"},
                            {"name": "Assists", "id": "AST"},
                            {"name": "Rebounds", "id": "REB"},
                            {"name": "Steals", "id": "STL"},
                            {"name": "Blocks", "id": "BLK"},
                            {"name": "Turnovers", "id": "TOV"},
                            {"name": "FG%", "id": "FG%"},
                            {"name": "3P%", "id": "3P%"},
                            {"name": "FT%", "id": "FT%"},
                        ],
                        fixed_rows={'headers': True},
                        tooltip_header={
                            'FG%': 'Field Goal Percentage',
                            '3P%': '3 Points Percentage',
                            'FT%': 'Free Throw Percentage',
                        },
                        style_table={
                            'height': '390px',
                            'overflowX': 'auto',
                        },
                        style_cell={
                            'fontFamily': 'Segoe UI',
                            'backgroundColor': '#F2F2F2',
                            'textAlign': 'left',
                            'minWidth': '70px',
                            'whiteSpace': 'normal',
                        },
                        style_header={
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'backgroundColor': '#CCCCCC',
                        },
                        tooltip_delay=0,
                        tooltip_duration=None,
                        sort_action='native',
                        style_header_conditional=[{
                            'if': {'column_id': col},
                            'textDecoration': 'underline',
                            'textDecorationStyle': 'dotted',
                        } for col in ['FG%', '3P%', 'FT%']],
                        style_data_conditional=[{
                            'if': {'row_index': 'odd'},
                            'backgroundColor': '#FFFFFF',
                        }],     
                    ),
            ])
                

def get_players_stats():
    data = DataAPI.get_all_players_stats("2022", "2023")
    df = pd.DataFrame(data)
    df = df.transpose()
    df.insert(0, 'id_player', df.index)

    # For the last 3 columns, convert to pourcentage
    df['FG%'] = df['FG%']*100
    df['3P%'] = df['3P%']*100
    df['FT%'] = df['FT%']*100

    # # Foreach value in the column above, round to 2 decimal places
    df['score'] = df['score'].apply(lambda x: "%.1f" % x)
    df['PTS'] = df['PTS'].apply(lambda x: "%.1f" % x)
    df['AST'] = df['AST'].apply(lambda x: "%.1f" % x)
    df['REB'] = df['REB'].apply(lambda x: "%.1f" % x)
    df['STL'] = df['STL'].apply(lambda x: "%.1f" % x)
    df['BLK'] = df['BLK'].apply(lambda x: "%.1f" % x)
    df['TOV'] = df['TOV'].apply(lambda x: "%.1f" % x)
    df['FG%'] = df['FG%'].apply(lambda x: "%.1f" % x)
    df['3P%'] = df['3P%'].apply(lambda x: "%.1f" % x)
    df['FT%'] = df['FT%'].apply(lambda x: "%.1f" % x)

    # Convert score, PTS, AST, REB, STL, BLK, TOV, FG%, 3P%, FT% to float
    df['score'] = df['score'].astype(float)
    df['PTS'] = df['PTS'].astype(float)
    df['AST'] = df['AST'].astype(float)
    df['REB'] = df['REB'].astype(float)
    df['STL'] = df['STL'].astype(float)
    df['BLK'] = df['BLK'].astype(float)
    df['TOV'] = df['TOV'].astype(float)
    df['FG%'] = df['FG%'].astype(float)
    df['3P%'] = df['3P%'].astype(float)
    df['FT%'] = df['FT%'].astype(float)

    # Convert to string
    df['FG%'] = df['FG%'].astype(str) + '%'
    df['3P%'] = df['3P%'].astype(str) + '%'
    df['FT%'] = df['FT%'].astype(str) + '%'

    # Remove $ from salary
    df['salary'] = df['salary'].str.replace('$', '')

    # Transform salary to int
    df['salary'] = df['salary'].astype(int)

    # Transform salary as string with format XXX'XXX$
    df['salary'] = df['salary'].apply(lambda x: '{:,}'.format(x).replace(',', "'") + '$')

    # Sort by score
    df = df.sort_values(by=['score'], ascending=False)

    return df