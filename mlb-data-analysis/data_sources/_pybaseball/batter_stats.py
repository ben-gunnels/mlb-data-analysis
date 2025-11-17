import pybaseball
import pandas as pd
from typing import Literal
from lib.types import Date


class Batter:
    def __init__(self):
        pass


    def stats(
        self,
        start_season: int = 2025, 
        end_season: int | None = None,
        league: Literal["all", "nl", "al", "mnl"] = "all",
        qual: int = 1,
        ind: int = 1
    ) -> pd.DataFrame:
        """Returns season level batting stats via FanGraphs.
        """
        return pd.DataFrame(
            pybaseball.batting_stats(
                start_season,
                end_season=end_season,
                league=league,
                qual=qual,
                ind=ind
            )
        ) 
    

    def bref_stats(
        self,
        season: int = 2025
    ) -> pd.DataFrame: 
        return pd.DataFrame(pybaseball.batting_stats_bref(season))
    

    def stats_range(
        self, 
        start_date: str | Date,
        end_date: str | Date | None = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.batting_stats_range(
                start_date,
                end_dt=end_date
            )
        )
    

    def bref_war(
        self,
        season: int | None = None,
        return_all: bool = False
    ) -> pd.DataFrame:
        response_object = pd.DataFrame(pybaseball.bwar_bat(return_all))

        if season is not None:
            return response_object[response_object["year_ID"] == season]

        return response_object

    def splits(
        player_id: int,
        season: int = None,
        player_info: bool = False
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.get_splits(
                player_id,
                year = season,
                player_info = player_info
            )
        )
    

    def statcast(
        self,
        start_date: str | Date,
        player_id: int,
        end_date: str | Date | None = None,
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_batter(
                start_date,
                player_id=player_id,
                end_dt=end_date
            )
        )
    

    def statcast_exit_velos(
        self,
        season: int = 2025,
        min_batted_balls: int | None = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_batter_exitvelo_barrels(
                season, 
                minBBE=min_batted_balls
            )
        )
    

    def statcast_expected_stats(
        self,
        season: int = 2025,
        min_pa: int | None = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_batter_expected_stats(
                season, 
                minPA=min_pa
            )
        )
    
    
    def statcast_percentile_ranks(
        self,
        season: int = 2025,
    ) -> pd.DataFrame:
        return pd.DataFrame(pybaseball.statcast_batter_percentile_ranks(season))
    

    def statcast_pitch_breakdown(
            self,
            season: int = 2025,
            min_pa: int = 25
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_batter_pitch_arsenal(
                season, 
                minPA=min_pa
            )
        )
        
    
  


    
