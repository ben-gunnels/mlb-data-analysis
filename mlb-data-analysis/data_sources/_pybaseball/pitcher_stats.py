import pybaseball
import pandas as pd
from typing import Literal
from lib.types import Date
    
    
class Pitcher:
    def __init__(self):
        pass
    

    def stats(
        self,
        start_season: int,
        end_season: int | None = None,
        league: Literal["all", "nl", "al", "mnl"] = "all",
        qual: int = None,
        ind: int = 1
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.pitching_stats(
                start_season,
                end_season=end_season,
                league=league,
                qual=qual,
                ind=ind
            )
        )
    

    def bref_stats(
        self,
        season: int,
    ) -> pd.DataFrame:
        return pd.DataFrame(pybaseball.pitching_stats_bref(season))
    

    def stats_range(
        self,
        start_date: Date | str,
        end_date: Date | str = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.pitching_stats_range(
                start_date,
                end_dt=end_date
            )
        )
    

    def splits(
        player_id: int,
        season: int = None,
        player_info: bool = False
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.get_splits(
                player_id,
                year = season,
                player_info = player_info,
                pitching_splits = True
            )
        )
    

    def statcast(
        self,
        start_date: Date | str,
        player_id: int,
        end_date: Date | str = None
    ) -> pd.DataFrame: 
        return pd.DataFrame(
            pybaseball.statcast_pitcher(
                start_date,
                end_dt = end_date,
                player_id = player_id
            )
        )
    

    def statcast_expected_stats(
        self,
        season: int,
        min_plate_appearances_against: int,
    ) -> pd.DataFrame: 
        return pd.DataFrame(
            pybaseball.statcast_pitcher_expected_stats(
                season,
                minPa = min_plate_appearances_against
            )
        )
    

    def statcast_arsenal(
        self,
        season: int,
        min_pitches: int,
        arsenal_type: Literal["average_speed", "n_", "average_spin"] = "average_speed"
    ) -> pd.DataFrame: 
        return pd.DataFrame(
            pybaseball.statcast_pitcher_pitch_arsenal(
                season,
                minP = min_pitches,
                arsenal_type = arsenal_type
            )
        )
    

    def statcast_arsenal_stats(
        self,
        season: int,
        min_plate_appearances_against: int,
    ) -> pd.DataFrame: 
        return pd.DataFrame(
            pybaseball.statcast_pitcher_arsenal_stats(
                season,
                minPA = min_plate_appearances_against
            )
        )
    

    def statcast_pitch_movement(
        self,
        season: int,
        min_pitches: int,
        pitch_type: Literal["FF", "SIFT", "CH", "CUKC", "FC", "SL", "FS", "ALL"]
    ) -> pd.DataFrame: 
        return pd.DataFrame(
            pybaseball.statcast_pitcher_pitch_movement(
                season,
                minP = min_pitches,
                pitch_type = pitch_type
            )
        )
    

    def statcast_active_spin(
        self,
        season: int,
        min_pitches: int,
    ) -> pd.DataFrame: 
        """Active spin stats on all of a pitchers' pitches in a given year."""
        return pd.DataFrame(
            pybaseball.statcast_pitcher_active_spin(
                season,
                minP = min_pitches
            )
        )
    

    def statcast_spin(
        self,
        start_date: Date | str,
        player_id: int,
        end_date: Date | str
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_pitcher_spin(
                start_date,
                end_dt = end_date,
                player_id = player_id
            )
        )
    

    def statcast_percentile_ranks(
        self,
        season
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_pitcher_percentile_ranks(
                season
            )
        )
    

    def statcast_spin_dir_comparison(
        self,
        season: int = None,
        pitch_a: str = None,
        pitch_b: str = None,
        min_pitches: int = None,
        pitcher_pov: bool = True # Direction of spin
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_pitcher_spin_dir_comp(
                season,
                pitch_a = pitch_a,
                pitch_b = pitch_b,
                minP = min_pitches,
                pitcher_pov = pitcher_pov
            )
        )
    




    

    


    

        