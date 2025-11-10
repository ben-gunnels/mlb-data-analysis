import pybaseball
import pandas as pd
from typing import Literal, List
from lib.types import Date
from .lahman import LahmanAPI


class PlayerSearch:
    def __init__(self):
        self.lahman = LahmanAPI()
    

    def statcast_all_players(
        self,
        start_date: Date | str,
        end_date: Date | str,
        team: str | None = None,
        verbose: bool = True,
        parallel: bool = True
    ) -> pd.DataFrame:
        return pd.DataFrame(pybaseball.statcast(
            start_dt=start_date,
            end_dt=end_date,
            team=team,
            verbose=verbose,
            parallel=parallel
        ))
    

    def lookup_playerid(
        self,
        last_name: str,
        first_name: str | None = None,
        fuzzy: bool = False
    ) -> pd.DataFrame:
        return pd.DataFrame(pybaseball.playerid_lookup(
            last_name,
            first=first_name,
            fuzzy=fuzzy
        ))
    

    def lookup_playerid_reverse(
        self,
        player_ids: list[int],
        key_type: Literal["mlbam", "retro", "bbref", "fangraphs"] = "mlbam"
    ) -> pd.DataFrame:
        return pd.DataFrame(pybaseball.playerid_reverse_lookup(
            player_ids,
            key_type=key_type
        ))
    

    def search_player_list(
        self,
        player_list: List
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.player_search_list(player_list)
        )
    

    def chadwick(
        self,
        save: bool = False
    )-> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.chadwick_register(save=save)
        )
    