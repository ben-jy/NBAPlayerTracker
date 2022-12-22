import dash_bootstrap_components as dbc
from dash import html


class ButtonsStats(html.Div):
    def __init__(
        self,
    ):
        super().__init__([
            dbc.RadioItems(
                className="btn-group",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                        {'label': 'Points', 'value': 'PTS'},
                        {'label': 'Rebounds', 'value': 'REB'},
                        {'label': 'Assists', 'value': 'AST'},
                        {'label': 'Steals', 'value': 'STL'},
                        {'label': 'Blocks', 'value': 'BLK'},
                        {'label': 'Turnovers', 'value': 'TOV'},
                        {'label': 'FG%', 'value': 'FG%'},
                        {'label': '3P%', 'value': '3P%'},
                        {'label': 'FT%', 'value': 'FT%'},
                         ],
                value="PTS",
                id='dropdown-stat'
            ),
        ])
