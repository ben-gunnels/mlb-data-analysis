import re
import pytest
from data.mlb_stats_api_wrapper import MLBStatsAPI  # adjust if needed

api = MLBStatsAPI()

pytestmark = pytest.mark.integration  # so we can run these separately

def test_boxscore_smoke(vcr):
    # Known historical game (example: 2019) so results are stable
    game_pk = 565997  # LAD @ CHC on 2019-04-24/25
    timecode = "20190425_012240"  # UTC timecode example
    
    data = api.boxscore(game_pk, timecode)
    # Minimal invariants that should hold across time
    assert isinstance(data, dict)
    # Common top-level keys present in boxscore_data
    for k in ["teams", "officials", "info", "people"]:
        assert k in data

def test_latest_season(vcr):
    season = api.latest_season()  # hits statsapi.latest_season
    assert isinstance(season, str)
    assert re.fullmatch(r"\d{4}", season)

def test_schedule_window(vcr):
    # Small time window to keep response small & stable
    out = api.schedule(
        start_date="2019-04-24",
        end_date="2019-04-25",
        sport_id=1,
        season="2019",
    )
    assert isinstance(out, dict)
    assert "dates" in out
    # Every item in "dates" should have "games"
    for d in out.get("dates", []):
        assert "games" in d

def test_league_leader_smoke(vcr):
    out = api.league_leaders(
        category="homeRuns",
        season="2019",
        limit=5,
        stat_group="hitting",
        sport_id=1,
        stat_type="season",
    )
    assert isinstance(out, dict)
    assert "leagueLeaders" in out
    assert len(out.get("leagueLeaders", [])) <= 5
