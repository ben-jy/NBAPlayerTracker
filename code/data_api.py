# API to retrieve data from the database, containing NBA data

import os
import json
from typing import Dict
from definitions import ROOT_DIR
import numpy as np
import pandas as pd

PLAYERS_INFO_FOLDER = ROOT_DIR + '/data/json_data/players_info'
PLAYERS_STATS_FOLDER = ROOT_DIR + '/data/json_data/players_stats'
PLAYERS_SHOOTING_FOLDER = ROOT_DIR + '/data/json_data/players_shooting'
PLAYERS_SHOOTING_CSV_FOLDER = ROOT_DIR + '/data/csv_shots_data'
PLAYERS_LIST = [int(player_id.split('.')[0]) for player_id in os.listdir(PLAYERS_INFO_FOLDER)]


class DataAPI:
    @staticmethod
    def get_player_info(player_id: int) -> Dict:
        """Returns a dictionary of player information

        Parameters:
            player_id (int): The id of the player

        Returns:
            Dict: A dictionary of player information
        """
        with open(os.path.join(PLAYERS_INFO_FOLDER, f'{player_id}.json')) as f:
            player_info = json.load(f)
        return player_info

    @staticmethod
    def get_player_stats(player_id: int, season_start: str, season_end: str) -> Dict[str, Dict]:
        """Returns the average stats of a player during a certain period (defined by start_year and end_year)

        Parameters:
            player_id (int): The id of the player
            season_start (str): The start season of the period
            season_end (str): The end season of the period

        Returns:
            Dict: A dictionary of average stats of a player for a
            certain period
        """

        # get the stats of the player
        with open(os.path.join(PLAYERS_STATS_FOLDER, f'{player_id}.json')) as f:
            player_stats = json.load(f)

        # parse the year to make comparison easier
        season_start = int(season_start.split('-')[0])
        season_end = int(season_end.split('-')[0])

        # for the period given, compute the PTS, AST, REB, STl, BLK and TOV per game, and the FG%, 3P% and FT%
        stats = {}
        for season in player_stats:
            # parse the year to make comparison easier
            season_year = int(season.split('-')[0])
            if season_start <= season_year <= season_end:
                # get the stats of the season
                season_stats = player_stats[season]
                # compute the PTS, AST, REB, STl, BLK and TOV per game
                for stat in ['PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA']:
                    if stat in stats:
                        stats[stat] += season_stats[stat]
                    else:
                        stats[stat] = season_stats[stat]
                # add the number of games
                if 'GP' in stats:
                    stats['GP'] += season_stats['GP']
                else:
                    stats['GP'] = season_stats['GP']

        # check if the player played during the period
        if 'GP' in stats:
            # compute the average for stat per game
            for stat in ['PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV']:
                stats[stat] /= stats['GP']
            # compute the FG%, 3P% and FT%
            # check if the player attempted at least one shot
            if stats['FGA'] > 0:
                stats['FG%'] = stats['FGM'] / stats['FGA']
            else:
                stats['FG%'] = 0
            if stats['FG3A'] > 0:
                stats['3P%'] = stats['FG3M'] / stats['FG3A']
            else:
                stats['3P%'] = 0
            if stats['FTA'] > 0:
                stats['FT%'] = stats['FTM'] / stats['FTA']
            else:
                stats['FT%'] = 0

            # return only the wanted stats
            return {stat: stats[stat] for stat in ['PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG%', '3P%', 'FT%']}
        else:
            # return 0 for all stats
            return {stat: 0 for stat in ['PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV', 'FG%', '3P%', 'FT%']}

    @staticmethod
    def get_all_players_stats(season_start: str, season_end: str) -> Dict[int, Dict]:
        """Returns the average stats of all players during a certain period (defined by start_year and end_year) and
        their static information

        Parameters:
            season_start (str): The start season of the period
            season_end (str): The end season of the period

        Returns:
            Dict: A dictionary of average stats of all players for a certain period and their static information
        """

        # for each player, get the average stats for the period
        players_stats = {}
        for player_id in PLAYERS_LIST:
            player_info = DataAPI.get_player_info(player_id)
            # only keep first_name, last_name, position, team, salary and score
            players_stats[player_id] = {key: player_info[key] for key in
                                        ['first_name', 'last_name', 'position', 'team', 'salary', 'score']}
            players_stats[player_id].update(DataAPI.get_player_stats(player_id, season_start, season_end))

        return players_stats

    @staticmethod
    def get_player_stat_evolution(player_id: int, stat: str, season_start: str, season_end: str) -> Dict[str, float]:
        """
        Returns the evolution of a stat for a player during a certain period (defined by start_year and end_year)

        Parameters:
            player_id (int): The id of the player
            stat (str): The stat to get the evolution of. Can be PTS, AST, REB, STL, BLK, TOV, FG%, 3P% or FT%
            season_start (str): The start season of the period
            season_end (str): The end season of the period

        Returns:
            Dict: A dictionary of the evolution of the stat for the player during the period
        """

        # get the stats of the player
        with open(os.path.join(PLAYERS_STATS_FOLDER, f'{player_id}.json')) as f:
            player_stats = json.load(f)

        # parse the year to make comparison easier
        season_start = int(season_start.split('-')[0])
        season_end = int(season_end.split('-')[0])

        # init the stats dict (to 0.0 for each season (in format 2019-20) between season_start and season_end)
        stats = {f'{year}-{str(year + 1)[2:]}': 0.0 for year in range(season_start, season_end + 1)}

        # for the period given, compute the stat per game
        for season in player_stats:
            # parse the year to make comparison easier
            season_year = int(season.split('-')[0])
            if season_start <= season_year <= season_end:
                if stat in ['PTS', 'AST', 'REB', 'STL', 'BLK', 'TOV']:
                    games_played = player_stats[season]['GP']
                    if games_played > 0:
                        stats[season] = player_stats[season][stat] / games_played
                elif stat == 'FG%':
                    if player_stats[season]['FGA'] > 0:
                        stats[season] = player_stats[season]['FGM'] / player_stats[season]['FGA']
                elif stat == '3P%':
                    if player_stats[season]['FG3A'] > 0:
                        stats[season] = player_stats[season]['FG3M'] / player_stats[season]['FG3A']
                elif stat == 'FT%':
                    if player_stats[season]['FTA'] > 0:
                        stats[season] = player_stats[season]['FTM'] / player_stats[season]['FTA']

        return stats

    @staticmethod
    def get_player_shooting_chart(player_id: int, season_start: str, season_end: str) -> pd.DataFrame:
        """
        Returns the shooting chart of a player during a certain period (defined by start_year and end_year)

        Parameters:
            player_id (int): The id of the player
            season_start (str): The start season of the period
            season_end (str): The end season of the period

        Returns:
            Dict: A dataframe of the shooting chart of the player during the period
        """

        # get the csv file of the shooting chart
        shooting_chart = pd.read_csv(os.path.join(PLAYERS_SHOOTING_CSV_FOLDER, f'{player_id}.csv'))

        # parse the year to make comparison easier
        season_start = int(season_start.split('-')[0])
        season_end = int(season_end.split('-')[0])

        # filter the shooting chart (we must parse the year from the season column)
        shooting_chart = shooting_chart[shooting_chart['SEASON_ID'].apply(lambda x: season_start <= int(x.split('-')[0]) <= season_end)]

        # remove the SEASON_ID and PLAYER_ID columns and group by the LOC_X and LOC_Y columns
        shooting_chart = shooting_chart.drop(columns=['SEASON_ID', 'PLAYER_ID']).groupby(['LOC_X', 'LOC_Y']).sum().reset_index()

        # create a shooting percentage column
        shooting_chart['SHOOTING_PERCENTAGE'] = shooting_chart['SHOT_MADE'] / shooting_chart['SHOT_ATTEMPT']

        # return the shooting chart
        return shooting_chart

    @staticmethod
    def get_id_name_mapping():
        """
        Utility method that returns a dictionary of player id to player name mapping.

        Returns:
            Dict: A dictionary of player id to player name mapping
        """
        id_name_mapping = {}
        for player_id in PLAYERS_LIST:
            player_info = DataAPI.get_player_info(player_id)
            id_name_mapping[player_id] = f"{player_info['first_name']} {player_info['last_name']}"
        return id_name_mapping


if __name__ == '__main__':
    test_dict = DataAPI.get_player_shooting_chart_df(2544, '2017-18', '2019-20')
    # print the total of shots made
    print(test_dict)

