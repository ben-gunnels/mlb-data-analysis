import pandas as pd
from pybaseball import lahman as _lahman


class LahmanAPI:
    """Thin wrapper around pybaseball.lahman that always returns pandas DataFrames."""

    @staticmethod
    def _df_call(func_name: str) -> pd.DataFrame:
        """Call lahman.<func_name>() and coerce to DataFrame."""
        fn = getattr(_lahman, func_name, None)
        if fn is None:
            raise AttributeError(f"pybaseball.lahman has no function named '{func_name}'")
        result = fn()
        return pd.DataFrame(result)
    

    # People
    def people(self) -> pd.DataFrame:
        return self._df_call("people")
    

    # Parks
    def parks(self) -> pd.DataFrame:
        return self._df_call("parks")
    

    # All stars
    def all_star(self) -> pd.DataFrame:
        return self._df_call("all_star_full")
    

    # Appearances
    def appearances(self) -> pd.DataFrame:
        return self._df_call("appearances")
    

    # Manager awards
    def manager_awards(self) -> pd.DataFrame:
        return self._df_call("awards_manager")
    

    # Player awards
    def player_awards(self) -> pd.DataFrame:
        return self._df_call("awards_players")


    # Managers awards share
    def manager_awards_share(self) -> pd.DataFrame:
        return self._df_call("awards_share_managers")
    

    # Player awards share
    def player_awards_share(self) -> pd.DataFrame:
        return self._df_call("awards_share_players")
    

    def batting(self) -> pd.DataFrame:
        return self._df_call("batting")


    # Batting (postseason)
    def batting_post(self) -> pd.DataFrame:
        return self._df_call("batting_post")


    # College playing history
    def college_playing(self) -> pd.DataFrame:
        return self._df_call("college_playing")


    # Fielding
    def fielding(self) -> pd.DataFrame:
        return self._df_call("fielding")


    # Fielding OF appearances (LF/CF/RF counts)
    def fielding_of(self) -> pd.DataFrame:
        return self._df_call("fielding_of")


    # LF/CF/RF splits
    def fielding_of_split(self) -> pd.DataFrame:
        return self._df_call("fielding_of_split")


    # Fielding (postseason)
    def fielding_post(self) -> pd.DataFrame:
        return self._df_call("fielding_post")


    # Hall of Fame voting
    def hall_of_fame(self) -> pd.DataFrame:
        return self._df_call("hall_of_fame")


    # Home game attendance by park and year
    def home_games(self) -> pd.DataFrame:
        # Some versions expose this as `homegames`
        try:
            return self._df_call("home_games")
        except AttributeError:
            return self._df_call("homegames")


    # Managers by team and year
    def managers(self) -> pd.DataFrame:
        return self._df_call("managers")


    # Split-season managers
    def managers_half(self) -> pd.DataFrame:
        return self._df_call("managers_half")


    # Pitching (regular season)
    def pitching(self) -> pd.DataFrame:
        return self._df_call("pitching")


    # Pitching (postseason)
    def pitching_post(self) -> pd.DataFrame:
        return self._df_call("pitching_post")


    # Salaries
    def salaries(self) -> pd.DataFrame:
        return self._df_call("salaries")


    # Schools
    def schools(self) -> pd.DataFrame:
        return self._df_call("schools")


    # Playoff series results
    def series_post(self) -> pd.DataFrame:
        return self._df_call("series_post")


    # Teams by year (record, division, stadium, attendance, etc.)
    def teams(self) -> pd.DataFrame:
        return self._df_call("teams")


    # Franchises (current & historical)
    def teams_franchises(self) -> pd.DataFrame:
        return self._df_call("teams_franchises")


    # Team split-season data
    def teams_half(self) -> pd.DataFrame:
        return self._df_call("teams_half")
    

    
