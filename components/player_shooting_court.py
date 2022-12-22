from dash import html, dcc
import plotly.graph_objs as go
import numpy as np


COURT_RATIO = 0.94
COURT_WIDTH = 450


class PlayerShootingCourt(html.Div):
    def __init__(
            self,
            player  # the dataframe containing the location of the shots, and the number of shots made,
            # attempted and the shooting percentage per location
    ):
        if player is None:
            super().__init__([
            ])
            return

        empty = False
        player_shooting = player["shooting"]
        # if the dataframe is empty, add a dummy row to avoid errors
        if player_shooting.empty:
            player_shooting = player_shooting.append(
                {"LOC_X": 0, "LOC_Y": 0, "SHOT_MADE": 0, "SHOT_ATTEMPT": 0, "SHOOTING_PERCENTAGE": 1}, ignore_index=True)
            player_shooting = player_shooting.append(
                {"LOC_X": 0, "LOC_Y": 1, "SHOT_MADE": 0,
                    "SHOT_ATTEMPT": 0, "SHOOTING_PERCENTAGE": 0},
                ignore_index=True)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                # min x = 0, max x = 50, min y = 0, max y = 47
                x=player_shooting['LOC_X'] + 25,
                y=player_shooting['LOC_Y'],
                mode='markers',
                marker=dict(
                    size=player_shooting['SHOT_ATTEMPT'],
                    color=player_shooting['SHOOTING_PERCENTAGE'],
                    # colorscale='cividis',
                    colorscale=[
                                [0, "rgb(255, 176, 0)"],
                                [0.25, "rgb(254, 97, 0)"],
                                [0.50, "rgb(220, 38, 127)"],
                                [0.75, "rgb(120, 94, 240)"],
                                [1, "rgb(100, 143, 255)"],
                    ],
                    showscale=True,
                    colorbar=dict(
                        title='FG%',
                        tickformat=',.0%'
                    ),
                ),
            ))
            # disable hover
            fig.update_traces(hoverinfo='skip')

        else:
            # use a scatter plot to display the shots made (with a color gradient) and
            # the shots attempted (with a size gradient)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                # min x = 0, max x = 50, min y = 0, max y = 47
                x=player_shooting['LOC_X']+25,
                y=player_shooting['LOC_Y'],
                mode='markers',
                marker=dict(
                    size=np.log(player_shooting['SHOT_ATTEMPT']*100),
                    color=player_shooting['SHOOTING_PERCENTAGE'],
                    colorscale=[
                                [0, "rgb(255, 176, 0)"],
                                [0.25, "rgb(254, 97, 0)"],
                                [0.50, "rgb(220, 38, 127)"],
                                [0.75, "rgb(120, 94, 240)"],
                                [1, "rgb(100, 143, 255)"],
                    ],
                    showscale=True,
                    colorbar=dict(
                        title='FG%',
                        tickformat=',.0%'
                    ),
                ),
                # compute for each location the number of shots made and attempted
                customdata=np.stack(
                    (player_shooting['SHOT_MADE'], player_shooting['SHOT_ATTEMPT']), axis=1),
                # change the opacity of the tooltip when hovering
                hovertemplate='<b>FG%: %{marker.color:.1%}</b><br>FGM: %{customdata[0]}<br>FGA: %{customdata[1]}<extra></extra>',
            ))

        draw_plotly_court(fig)

        # remove graduation in axes x and y
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        # add background image in the figure
        fig.update_layout(
            xaxis_showgrid=False,
            yaxis_showgrid=False,
            xaxis=dict(range=[0, 50]),
            yaxis=dict(range=[0, 47]),
            width=COURT_WIDTH,
            height=COURT_WIDTH * COURT_RATIO,
            # template='plotly_dark'
        )

        super().__init__([
            html.Br(),
            dcc.Graph(
                figure=fig
            ),
        ])


def draw_plotly_court(fig, fig_width=600, margins=10):
    def ellipse_arc(x_center=25, y_center=5.25, a=10.5, b=10.5, start_angle=0.0, end_angle=2 * np.pi, N=200, closed=False):
        t = np.linspace(start_angle, end_angle, N)
        x = x_center + a * np.cos(t)
        y = y_center + b * np.sin(t)
        path = f'M {x[0]}, {y[0]}'
        for k in range(1, len(t)):
            path += f'L{x[k]}, {y[k]}'
        if closed:
            path += ' Z'
        return path

    fig_height = fig_width * (470 + 2 * margins) / (500 + 2 * margins)
    fig.update_layout(width=fig_width, height=fig_height)

    threept_break_y = 14.2
    # three_line_col = "#FFFFFF"
    # main_line_col = "#FFFFFF"
    three_line_col = "black"
    main_line_col = "black"

    width_line = 3

    fig.update_layout(
        # Line Horizontal
        margin=dict(l=20, r=20, t=20, b=20),
        # paper_bgcolor="#292b2c",
        # plot_bgcolor="#292b2c",
        paper_bgcolor="white",
        plot_bgcolor="white",

        yaxis=dict(
            scaleanchor="x",
            scaleratio=1,
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=False,
            ticks='',
            showticklabels=False,
            fixedrange=True,
        ),
        shapes=[
            dict(
                type="rect", x0=0, y0=0, x1=50, y1=47,
                line=dict(color=main_line_col, width=width_line),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="rect", x0=17, y0=0, x1=33, y1=19,
                line=dict(color=main_line_col, width=width_line),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(

                type="rect", x0=19, y0=0, x1=31, y1=19,
                line=dict(color=main_line_col, width=width_line),
                # fillcolor='#333333',
                layer='below'
            ),
            dict(
                type="circle", x0=19, y0=13, x1=31, y1=25, xref="x", yref="y",
                line=dict(color=main_line_col, width=width_line),
                # fillcolor='#dddddd',
                layer='below'
            ),
            dict(
                type="line", x0=19, y0=19, x1=31, y1=19,
                line=dict(color=main_line_col, width=width_line),
                layer='below'
            ),


            # Basketball hoop
            dict(
                type="rect", x0=24.8, y0=4.53, x1=25.2, y1=4,
                line=dict(color="#ec7607", width=width_line),
                fillcolor='#ec7607',
            ),
            dict(
                type="circle", x0=24.25, y0=4.5, x1=25.75, y1=6, xref="x", yref="y",
                line=dict(color="#ec7607", width=width_line),
            ),
            dict(
                type="line", x0=22, y0=4, x1=28, y1=4,
                line=dict(color="#ec7607", width=width_line),
            ),


            # Three point line
            dict(type="path",
                 path=ellipse_arc(a=4, b=4, start_angle=0, end_angle=np.pi),
                 line=dict(color=main_line_col, width=width_line), layer='below'),
            dict(type="path",
                 path=ellipse_arc(
                     a=23.75, b=23.75, start_angle=0.386283101, end_angle=np.pi - 0.386283101),
                 line=dict(color=main_line_col, width=width_line), layer='below'),
            dict(
                type="line", x0=3, y0=0, x1=3, y1=threept_break_y,
                line=dict(color=three_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=3, y0=0, x1=3, y1=threept_break_y,
                line=dict(color=three_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=47, y0=-0, x1=47, y1=threept_break_y,
                line=dict(color=three_line_col, width=width_line), layer='below'
            ),



            dict(
                type="line", x0=0, y0=28, x1=3, y1=28,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=50, y0=28, x1=47, y1=28,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),

            dict(
                type="line", x0=16, y0=7, x1=17, y1=7,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=16, y0=8, x1=17, y1=8,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=16, y0=11, x1=17, y1=11,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=16, y0=14, x1=17, y1=14,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=34, y0=7, x1=33, y1=7,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=34, y0=8, x1=33, y1=8,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=34, y0=11, x1=33, y1=11,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),
            dict(
                type="line", x0=34, y0=14, x1=33, y1=14,
                line=dict(color=main_line_col, width=width_line), layer='below'
            ),

            dict(type="path",
                 path=ellipse_arc(y_center=47, a=6, b=6,
                                  start_angle=-0, end_angle=-np.pi),
                 line=dict(color=main_line_col, width=width_line), layer='below'),

        ]
    )
    return True
