import pybaseball
import pandas as pd
from typing import Literal
from lib.types import Date


class Team:
    def __init__(self):
        pass
    

    def statcast(
        self,
        start_date: Date | str,
        end_date: Date | str,
        team: str | None = None,
        verbose: bool = True,
        parallel: bool = True
    ) -> pd.DataFrame:
        """Return pitch-level statcast data for a given date or range."""
        return pd.DataFrame(
            pybaseball.statcast(
                start_date,
                end_dt = end_date,
                team = team,
                verbose = verbose,
                parallel = parallel
            )
        )
    

    def batting(
        self,
        start_season: int,
        end_season: int | None = None,
        league: Literal["all", "al", "nl", "mnl"] = "all",
        ind: int = 1
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_batting(
                start_season,
                end_season = end_season,
                league = league,
                ind = ind
            )
        )
    
    def batting_bref(
        self,
        team: str,
        start_season: int,
        end_season: int | None = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_batting_bref(
                team,
                start_season,
                end_season = end_season
            )
        )
    

    def fielding(
        self,
        start_season: int,
        end_season: int | None = None,
        league: Literal["all", "al", "nl", "mnl"] = "all",
        ind: int = 1
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_fielding(
                start_season,
                end_season = end_season,
                league = league,
                ind = ind
            )
        )
    

    def fielding_bref(
        self,
        start_season: int,
        end_season: int | None = None,
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_fielding_bref(
                start_season,
                end_season = end_season
            )
        )
    

    def pitching(
        self,
        start_season: int,
        end_season: int | None = None,
        league: Literal["all", "al", "nl", "mnl"] = "all",
        ind: int = 1
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_pitching(
                start_season,
                end_season = end_season,
                league = league,
                ind = ind
            )
        )
    
    def pitching_bref(
        self,
        team: str,
        start_season: int,
        end_season: int | None = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_pitching_bref(
                team,
                start_season,
                end_season = end_season
            )
        )
    

    def game_logs(
        self,
        season: int,
        team: str,
        log_type: Literal["batting", "pitching"] = "batting"
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_game_logs(
                season,
                team,
                log_type=log_type
            )
        )


    






