import pybaseball
import pandas as pd
from typing import Literal
from lib.types import Date


class DraftAndProspects:
    def __init__(self):
        pass
    
    
    def amateur_draft(
        self,
        season: int,
        draft_round: int,
        keep_stats: bool = True
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.amateur_draft(
                season,
                draft_round,
                keep_stats = keep_stats
            )
        )
    
    
    def amateur_draft_by_team(
        self,
        team: str,
        season: int, 
        keep_stats: bool = True
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.amateur_draft_by_team(
               team,
               season, 
               keep_stats = keep_stats 
            )
        )
    
    
    def top_prospects(
        self,
        team: str | None = None,
        player_type: str | None = None
    ) -> pd.DataFrame:
        return pd.DataFrame(
            pybaseball.top_prospects(
                teamName = team,
                playerType = player_type
            )
        )
    


    


