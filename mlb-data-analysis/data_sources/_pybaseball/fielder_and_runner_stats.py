import pybaseball
import pandas as pd
from typing import Literal, Union
from lib.types import Date


class FielderAndRunner:
    def __init__(self):
        pass
    

    def statcast_outs_above_average(
        self,
        season: int,
        position: Union[int, str],
        min_attempts: Union[int, str] = "q",
        view: str = "Fielder"
    ) -> pd.DataFrame:
        """Returns statscast outs above average.

            OAA is a Statcast metric based on the 
            "cumulative effect of all individual plays 
            a fielder has been credited or debited with, 
            making it a range-based metric of fielding 
            skill that accounts for the number of 
            plays made and the difficulty of them".

            position: May be entered as integers or strings corresponding
            to the position abbreviation or the position number.

            min_attempts: The minimum number of fielding attempts 
            for the player to be included in the result. 
            Statcast's default is players, which is 1 
            fielding attempt per game played for 
            2B, SS, 3B, and OF and 1 fielding attempt 
            per every other game played for 1B.
        
        """
        return pd.DataFrame(
            pybaseball.statcast_outs_above_average(
                season,
                position,
                min_att = min_attempts,
                view = view
            )
        )
    

    def statcast_outfield_directional_oaa(
        self,
        season: int,
        min_opportunities: Union[int, str] = "q"
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_outfield_directional_oaa(
                season,
                min_opp = min_opportunities
            )
        )
    

    def statcast_outfield_catch_probability(
        self,
        season: int,
        min_opportunities: Union[int, str] = "q"
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_outfield_catch_prob(
                season,
                min_opp = min_opportunities
            )
        )
    

    def statcast_outfielder_jump(
        self,
        season: int, 
        min_attempts: Union[int, str] = "q"
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_outfielder_jump(
                season, 
                min_att = min_attempts
            )
        )
    

    def statcast_catcher_poptime(
        self,
        season: int,
        min_2b_sb_attempts: int,
        min_3b_sb_attempts: int
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_catcher_poptime(
                season,
                min_2b_sb_attempts,
                min_3b_sb_attempts
            )
        )
    

    def statcast_catcher_poptime(
        self,
        season: int,
        min_called_pitches: Union[int, str] = "q",
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_catcher_poptime(
                season,
                min_called_p = min_called_pitches
            )
        )
    

    def statcast_fielding_run_value(
        self,
        season: int,
        position: Union[int, str],
        min_innings: int = 100
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_fielding_run_value(
                season,
                position,
                min_inn = min_innings
            )
        )
    

    def statcast_sprint_speed(
        self,
        season: int,
        min_opportunities: int = 10,
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_sprint_speed(
                season,
                min_opp = min_opportunities
            )
        )
    

    def statcast_running_splits(
        self,
        season: int,
        min_opportunities: int = 5,
        raw_splits: bool = True
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.statcast_running_spits(
                season,
                min_opp = min_opportunities,
                raw_splits = raw_splits
            )
        )

