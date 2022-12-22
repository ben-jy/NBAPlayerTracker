
from data_api import DataAPI

init_compare_dict = {"height": 0, "weight": 0, "PTS": 0, "REB": 0, "AST": 0, "STL": 0, "BLK": 0, "TOV": 0, "FG%": 0, "3P%": 0, "FT%": 0}

def get_all_players(start_year, end_year):
    players_list = DataAPI.get_all_players_stats(
        season_start=str(start_year)+"-"+str(abs(start_year+1) % 100), season_end=str(end_year)+"-"+str(abs(end_year+1) % 100))

    players_names_list = []
    for player_id in list(players_list.keys()):
        players_names_list.append(
            {'label': players_list[player_id]['first_name']+" "+ players_list[player_id]['last_name'], 'value': player_id})

    # sort players_names_list by first_name
    players_names_list.sort(key=lambda x: x['label'].split(" ")[0])
    return players_names_list

def get_player(card_id, player_id, year_range, selected_stat):
    if(player_id is None):
        return None
    
    start_season = str(year_range[0])+"-"+str(abs(year_range[1]+1) % 100)
    end_season = str(year_range[1])+"-"+str(abs(year_range[1]+1) % 100)
    player = {}
    player["id"] = player_id
    player["card_id"] = card_id
    player["info"] = DataAPI.get_player_info(player_id=player_id)
    player["stats"] = DataAPI.get_player_stats(
        player_id=player_id, season_start=start_season, season_end=end_season)
    player["shooting"] = DataAPI.get_player_shooting_chart(
        player_id=player_id, season_start=start_season, season_end=end_season)
    if selected_stat is not None:
        player["stat_evolution"] = DataAPI.get_player_stat_evolution(
            player_id=player_id, season_start=start_season, season_end=end_season, stat=selected_stat)
        if selected_stat == "FT%" or selected_stat == "FG%" or selected_stat == "3P%":
            for season in player["stat_evolution"].keys():
                player["stat_evolution"][season] = round(
                    float(player["stat_evolution"][season])*100, 1)
    return player


def compare_stats(player, other_player):
    comparaison_dict = init_compare_dict
    if player is not None and other_player is not None:
        player_stats = player["stats"]
        other_player_stats = other_player["stats"]
        for stat in comparaison_dict.keys():
            if(stat == "height"):
                ft_player = float(player["info"]["height"].split("-")[0])
                inch_player = float(player["info"]["height"].split("-")[1])
                ft_other = float(other_player["info"]["height"].split("-")[0])
                inch_other = float(
                    other_player["info"]["height"].split("-")[1])
                if(ft_player != ft_other):
                    comparaison_dict = set_comparaison_dict(
                        comparaison_dict, "height", ft_player, ft_other)
                else:
                    comparaison_dict = set_comparaison_dict(
                        comparaison_dict, "height", inch_player, inch_other)
            elif(stat == "weight"):
                weight_player = float(player["info"]["weight"])
                weight_other = float(other_player["info"]["weight"])
                comparaison_dict = set_comparaison_dict(
                    comparaison_dict, "weight", weight_player, weight_other)
            elif(stat.__contains__("%")):
                player_stat = round(float(player_stats[stat])*100,1)
                other_player_stat = round(float(other_player_stats[stat])*100,1)
                comparaison_dict = set_comparaison_dict(
                    comparaison_dict, stat, player_stat, other_player_stat)
            else:
                player_stat = round(float(player_stats[stat]),1)
                other_player_stat = round(float(other_player_stats[stat]),1)
                comparaison_dict = set_comparaison_dict(
                    comparaison_dict, stat, player_stat, other_player_stat)
    return comparaison_dict


def set_comparaison_dict(dict, stat, player_stat, other_player_stat):
    if(player_stat > other_player_stat):
        dict[stat] = 1
    elif(player_stat == other_player_stat):
        dict[stat] = 0
    else:
        dict[stat] = -1
    return dict


config = {
    "PLAYER_1_COLOR": "#648DFE",
    "PLAYER_2_COLOR": "#FFAD00",
}
