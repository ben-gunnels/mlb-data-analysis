"""Loosely wraps the data API for the MLBStats-API:  https://github.com/toddrob99/MLB-StatsAPI/wiki

    Api endpoints ending in _data return json data.
    Methods of the MLBStatsAPI class will omit this suffix as the standard.

    Consider this for supplementary data or to fill in the cracks if any from pybaseball source.
"""
import statsapi
import logging
import pandas as pd
from typing import Literal, Dict, Any
from lib.types import TimeCode


logger = logging.getLogger('statsapi')
logger.setLevel(logging.DEBUG)
rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)8s - %(name)s(%(thread)s) - %(message)s")
ch.setFormatter(formatter)
rootLogger.addHandler(ch)


class MLBStatsAPI:
    def __init__(self):
        self.statsapi = statsapi 


    def boxscore(
        self,
        game_pk: int,
        timecode: TimeCode | None = None
    ) -> dict:
        return self.statsapi.boxscore_data(gamePk=game_pk, timecode=timecode)


    def game_pace(
        self, 
        season: str = "2025",
        sport_id: int = 1
    ) -> pd.DataFrame:
        response_object = self.statsapi.game_pace_data(season=season, sportId=sport_id)
        
        if "sports" in response_object:
            return pd.DataFrame(response_object["sports"])
        return pd.DataFrame({})


    def game_scoring_play(
        self, 
        game_pk: int
    ) -> dict:
        return self.statsapi.game_scoring_play_data(gamePk=game_pk)


    def latest_season(
        self, 
        sport_id: int = 1
    ) -> pd.DataFrame:
        response_object = self.statsapi.latest_season(sportId=sport_id)

        return pd.DataFrame([response_object])


    def league_leader(
        self,
        category: str,
        season: str = "2025",
        limit: int = 10,
        stat_group=None, 
        league_id=None,
        game_types=None,
        player_pool=None,
        sport_id=1,
        stat_type=None
    ):
        response_object = self.statsapi.league_leader_data(
            category,
            season=season,
            limit=limit,
            statGroup=stat_group,
            leagueId=league_id,
            gameTypes=game_types,
            playerPool=player_pool,
            sportId=sport_id,
            statType=stat_type
        )

        leaders_data = [{"rank": rk, "player": pl, "team": tm, "val": val} for (rk, pl, tm, val) in response_object]
        df = pd.DataFrame(leaders_data)

        # Cast the statistical category of interest to numeric
        df["val"] = pd.to_numeric(df["val"])
        return df


    def lookup_player(
        self,
        lookup_value: str,
        game_type: str = "R",
        season="2025",
        sport_id: int = 1
    ) -> pd.DataFrame:
        """Looks up player information from a name entry in lookup_value.
        Note: if using a full last name as the lookup_value and that last name could be part of another player's lastname, e.g. Nola is part of Nolan, include a comma on the end of the last name in order to match on the initLastName field which looks like Nola, A
        """
        response_object = self.statsapi.lookup_player(
            lookup_value,
            gameType=game_type,
            season=season,
            sportId=sport_id
        ) or []
        
        if len(response_object):
            return self._compile_player_lookup_to_dataframe(response_object)
        return pd.DataFrame([])
    

    def lookup_team(
        self,
        lookup_value: str, 
        active_status: Literal["Y", "N", "B"] = "Y", 
        season: str = None, 
        sport_ids: int = 1
    ) -> pd.DataFrame:
        response_object = statsapi.lookup_team(
            lookup_value,
            activeStatus=active_status,
            season=season,
            sportIds=sport_ids
        )

        if not len(response_object):
            return pd.DataFrame([])
        
        keep_keys = ["id", "name", "teamCode", "teamName", "locationName"]
        team_info = [{k: v for k, v in team.items() if k in keep_keys} for team in response_object]

        return pd.DataFrame(team_info) 


    def player_statistics(
        self,
        player_id,
        group: list[Literal["hitting", "pitching", "fielding"]],
        data_type: str = "season",
        sport_id: int = 1,
        season: str = "2025"
    ) -> pd.DataFrame:
        # Expects a string that looks like a list
        group_reformatted = f"[{','.join([g for g in group])}]"

        response_object = self.statsapi.player_stat_data(
            player_id,
            group=group_reformatted,
            type=data_type,
            sportId=sport_id,
            season=season
        )
        return self._compile_player_stats_to_dataframe(response_object)


    def schedule(
        self,
        date: str = None, 
        start_date: str = None, 
        end_date: str = None, 
        team: str = "", 
        opponent: str = "", 
        sport_id: int = 1, 
        game_id: int = None, 
        season: bool = None, 
        include_series_status: bool = True
    ) -> pd.DataFrame:
        response_object = self.statsapi.schedule(
            date=date,
            start_date=start_date,
            end_date=end_date,
            team=team,
            opponent=opponent,
            sportId=sport_id,
            game_id=game_id,
            season=season,
            include_series_status=include_series_status
        )
        return pd.DataFrame(response_object)


    def standings(
        self,
        league_id: Literal["103", "104"],
        division: Literal["all", "nlw", "nlc", "nle", "alw", "alc", "ale"],
        include_wildcard: bool = True,
        season: str = "2025",
        standings_types=None,
        date=None
    ) -> dict:
        # Enforce that 103 is American League and 104 is National League
        league_division_match = { 
            "103": ["all", "alw", "alc", "ale"], 
            "104": ["all", "nlw", "nlc", "nle"] 
        }

        valid_divisions = league_division_match.get(league_id)
        if not valid_divisions or division not in valid_divisions:
            raise ValueError(
                f"Invalid league_id/division pair: ({league_id}, {division}). "
                "Valid pairs: (103, al*), (104, nl*)."
            )
        return self.statsapi.standings_data(
            leagueId=league_id,
            division=division,
            include_wildcard=include_wildcard,
            season=season,
            standingsTypes=standings_types,
            date=date
        )
    

    def team_leaders(
        self,
        team_id,
        leader_categories,
        season: str = "2025",
        leader_game_types="R",
        limit=10
    ) -> list:
        return self.statsapi.team_leader_data(
            teamId=team_id,
            leaderCategories=leader_categories,
            season=season,
            leaderGameTypes=leader_game_types,
            limit=limit
        )
    

    def _compile_player_stats_to_dataframe(self, stats: Dict[str, Any]) -> pd.DataFrame:
        """
        Flatten a player's stats payload into a tidy DataFrame.
        Expects `stats` like:
        {
            ...player info...,
            "stats": [
            {"group": "...", "season": "YYYY", "stats": {...}},
            ...
            ]
        }
        """
        # Everything except the nested "stats" list is constant player-level info
        info = {k: v for k, v in stats.items() if k != "stats"}

        groups = stats.get("stats", [])
        rows = [
            {
                **info,                                # constant player info
                "stat_type": g.get("group"),
                "season": g.get("season"),
                **(g.get("stats") or {}),              # actual stat fields
            }
            for g in groups
        ]

        df = pd.DataFrame.from_records(rows)

        df = df.convert_dtypes()
        for col in df.select_dtypes(include="number"):
            df[col] = df[col].fillna(0)

        return df
    

    def _compile_player_lookup_to_dataframe(self, players: list[Dict[str, Any]]) -> pd.DataFrame:
        """
        Flatten a player's lookup payload into a tidy DataFrame.
        Expects `players` like:
        [
        {
            ...player info...,
        }...
        ]
        """
        keep_keys = [
            "id", 
            "firstName", 
            "lastName", 
            "primaryNumber", 
            "currentTeam", 
            "primaryPosition", 
            "nickName"
        ]
        players_filtered = [{k: v for k, v in player.items() if k in keep_keys} for player in players]
        return pd.DataFrame(players_filtered)
