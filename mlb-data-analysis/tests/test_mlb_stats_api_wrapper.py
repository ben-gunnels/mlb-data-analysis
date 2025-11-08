import types
import pytest

from data import mlb_stats_api_wrapper as mod


@pytest.fixture
def api():
    """Create a fresh MLBStatsAPI with a real module reference to monkeypatch."""
    return mod.MLBStatsAPI()


def _stub(monkeypatch, target_obj, name, return_value=None, side_effect=None, capture=None):
    """Helper to monkeypatch a function on target_obj and capture calls.
    capture: a dict that will receive {"called": True, "args": ..., "kwargs": ...}
    """
    def _fn(*args, **kwargs):
        if capture is not None:
            capture["called"] = True
            capture["args"] = args
            capture["kwargs"] = kwargs
        if side_effect:
            return side_effect(*args, **kwargs)
        return return_value
    monkeypatch.setattr(target_obj, name, _fn)
    return _fn


def test_boxscore_with_timecode(monkeypatch, api):
    called = {}
    expected = {"ok": True, "kind": "boxscore"}
    _stub(monkeypatch, mod.statsapi, "boxscore_data", return_value=expected, capture=called)

    # TimeCode is imported in your code; it’s structurally a str like "YYYYMMDD_HHMMSS"
    timecode = "20190425_012240"
    game_pk = 565997

    out = api.boxscore(game_pk, timecode)

    assert out == expected
    assert called["called"] is True
    assert called["args"] == (game_pk, timecode)
    assert called["kwargs"] == {}


def test_game_pace_defaults(monkeypatch, api):
    called = {}
    expected = {"pace": "fast"}
    _stub(monkeypatch, mod.statsapi, "game_pace_data", return_value=expected, capture=called)

    out = api.game_pace()  # uses defaults season="2025", sport_id=1

    assert out == expected
    assert called["args"] == ("2025", 1)


def test_game_pace_custom(monkeypatch, api):
    called = {}
    expected = {"pace": "slow"}
    _stub(monkeypatch, mod.statsapi, "game_pace_data", return_value=expected, capture=called)

    out = api.game_pace(season="1999", sport_id=1)

    assert out == expected
    assert called["args"] == ("1999", 1)


def test_game_scoring_play(monkeypatch, api):
    called = {}
    expected = {"plays": [1, 2, 3]}
    _stub(monkeypatch, mod.statsapi, "game_scoring_play_data", return_value=expected, capture=called)

    out = api.game_scoring_play(12345)

    assert out == expected
    assert called["args"] == (12345,)


def test_latest_season(monkeypatch, api):
    called = {}
    expected = "2025"
    _stub(monkeypatch, mod.statsapi, "latest_season", return_value=expected, capture=called)

    out = api.latest_season()
    assert out == "2025"
    assert called["args"] == (1,)

    out2 = api.latest_season(sport_id=1)
    assert out2 == "2025"
    assert called["args"] == (1,)


def test_league_leader_full_signature(monkeypatch, api):
    called = {}
    expected = {"leaders": ["A", "B"]}
    _stub(monkeypatch, mod.statsapi, "league_leader_data", return_value=expected, capture=called)

    out = api.league_leaders(
        category="homeRuns",
        season="2024",
        limit=5,
        stat_group="hitting",
        league_id=103,
        game_types="R",
        player_pool="ALL",
        sport_id=1,
        stat_type="season"
    )

    assert out == expected
    assert called["args"] == (
        "homeRuns", "2024", 5, "hitting", 103, "R", "ALL", 1, "season"
    )


def test_lookup_player(monkeypatch, api):
    called = {}
    expected = [{"id": 123, "fullName": "Shohei Ohtani"}]
    _stub(monkeypatch, mod.statsapi, "lookup_player", return_value=expected, capture=called)

    out = api.lookup_player("Ohtani", game_type="R", season="2025", sport_id=1)

    assert out == expected
    assert called["args"] == ("Ohtani", "R", "2025", 1)


@pytest.mark.parametrize("group", ["hitting", "pitching", "fielding"])
def test_player_statistics(monkeypatch, api, group):
    called = {}
    expected = {"group": group}
    _stub(monkeypatch, mod.statsapi, "player_stat_data", return_value=expected, capture=called)

    out = api.player_statistics(
        player_id=660271,  # example player id
        group=group,
        data_type="season",
        sport_id=1,
        season="2025"
    )

    assert out == expected
    assert called["args"] == (660271, group, "season", 1, "2025")


def test_schedule_defaults_and_args(monkeypatch, api):
    called = {}
    expected = {"games": []}
    _stub(monkeypatch, mod.statsapi, "schedule", return_value=expected, capture=called)

    # defaults
    out = api.schedule()
    assert out == expected
    # The wrapper passes all 10 positional args through; defaults should be preserved
    assert called["args"] == (None, None, None, "", "", 1, None, "2025", True)

    # custom
    called.clear()
    out2 = api.schedule(
        date="2025-04-01",
        start_date=None,
        end_date=None,
        team="Dodgers",
        opponent="Giants",
        sport_id=1,
        game_id=999999,
        season="2025",
        include_series_status=False,
    )
    assert out2 == expected
    assert called["args"] == (
        "2025-04-01", None, None, "Dodgers", "Giants", 1, 999999, "2025", False
    )


def test_standings(monkeypatch, api):
    called = {}
    expected = {"standings": "ok"}
    _stub(monkeypatch, mod.statsapi, "standings_data", return_value=expected, capture=called)

    out = api.standings(
        league_id="103",
        division="nlw",
        include_wildcard=True,
        season="2025",
        standings_types=None,
        date=None,
    )

    assert out == expected
    assert called["args"] == ("103", "nlw", True, "2025", None, None)


def test_team_leader(monkeypatch, api):
    called = {}
    expected = {"leaders": []}
    _stub(monkeypatch, mod.statsapi, "team_leader_data", return_value=expected, capture=called)

    out = api.team_leader(
        team_id=119,
        leader_categories="homeRuns",
        season="2025",
        leader_game_types="R",
        limit=7,
    )

    assert out == expected
    assert called["args"] == (119, "homeRuns", "2025", "R", 7)
