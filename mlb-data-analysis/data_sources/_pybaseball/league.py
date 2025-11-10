import pybaseball
import pandas as pd
from typing import Literal
from lib.types import Date


class League:
    def __init__(self):
        pass


    def team_ids(
        self,
        season: int,
        league: Literal["all", "al", "nl", "mnl"] = "all",
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.team_ids(
                season,
                league
            )
        )
    

    def schedule_and_record(
        self,
        season: int,
        team: str
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.schedule_and_record(
                season,
                team
            )
        )
    

    def standings(
        self, 
        season: int
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.standings(season)
        )