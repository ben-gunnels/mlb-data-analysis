__all__ = ["KEEP_RENAME_MAP", "ROLLING_COLS"]

batter_bref_war_keep_cols_rename = {
    "name_common": "player_name",
    "mlb_ID": "mlb_id",
    "team_ID": "team",
    "year_ID": "season",
    "salary": "salary",
    "WAR": "bWAR"
}


batter_stats_keep_cols_rename = {
    "IDfg": "fg_id",
    "Season": "season",
    "Name": "player_name",
    "Team": "team",
    "Age": "age",
    "G": "G",
    "AB": "AB",
    "PA": "PA",
    "H": "H",
    "1B": "1B",
    "2B": "2B",
    "3B": "3B",
    "HR": "HR",
    "R": "R",
    "RBI": "RBI",
    "BB": "BB",
    "IBB": "IBB",
    "SO": "SO",
    "SB": "SB",
    "CS": "CS",
    "AVG": "AVG",
    "GB": "GB",
    "FB": "FB",
    "LD": "LD",
    "Pitches": "pitches",
    "Balls": "balls",
    "Strikes": "strikes",
    "BB%": "BB%",
    "K%": "K%",
    "BB/K": "BB/K",
    "OBP": "OBP",
    "SLG": "SLG",
    "OPS": "OPS",
    "ISO": "ISO",
    "BABIP": "BABIP",
    "GB/FB": "GB/FB",
    "LD%": "LD%",
    "GB%": "GB%",
    "FB%": "FB%",
    "HR/FB": "HR/FB",
    "wOBA": "wOBA",
    "wRAA": "wRAA",
    "wRC": "wRC",
    "Pos": "Pos",
    "RAR": "RAR",
    "WAR": "fWAR",
    "wRC+": "wRC+",
    "WPA": "WPA",
    "Contact%": "contact%",
    "Zone%": "zone%",
    "SwStr%": "sw_str%",
    "Pull%+": "pull%+",
    "Cent%+": "cent%+",
    "Oppo%+": "oppo%+",
    "Soft%+": "soft%+",
    "Med%+": "med%+",
    "Hard%+": "hard%+",
    "EV": "EV",
    "LA": "LA",
    "Barrel%": "barrel%",
    "maxEV": "max_ev",
    "HardHit%": "hard_hit%",
}


batter_statcast_pct_keep_cols_rename = {
    "player_name": "player_name",
    "player_id": "statcast_id",
    "xwoba": "xwoba",
    "xba": "xba",
    "xslg": "xslg",
    "xiso": "xiso",
    "xobp": "xobp",
    "arm_strength": "arm_strength",
    "sprint_speed": "sprint_speed",
    "oaa": "oaa",
    "bat_speed": "bat_speed",
    "squared_up_rate": "squared_up_rate",
    "swing_length": "swing_length"
}


batter_statcast_exp_keep_cols_rename = {
    "player_id": "statcast_id",                 
    "est_ba": "est_ba",                  
    "est_ba_minus_ba_diff": "est_ba_minus_ba_diff",    
    "est_slg": "est_slg",                 
    "est_slg_minus_slg_diff": "est_slg_minus_slg_diff",  
    "est_woba": "est_woba",                
    "est_woba_minus_woba_diff": "est_woba_minus_woba_diff",
}


batter_free_agent_rename = {
    "From": "fa_team",
    "Player": "player_name",
    "Pos": "pos",
    "Yrs": "contract_years",
    "Value": "value",
    "AAV": "AAV"
}

ROLLING_COLS = [
    "AB", "PA", "H", "1B", "2B", "3B", "HR", "R", "RBI",
    "BB", "IBB", "SO", "SB", "CS",

    "AVG", "OBP", "SLG", "OPS", "ISO", "BABIP",
    "wOBA", "wRAA", "wRC", "wRC+", "WPA",

    "BB%", "K%", "BB/K", "contact%", "zone%", "sw_str%",

    "EV", "LA", "barrel%", "max_ev", "hard_hit%",
    "pull%+", "cent%+", "oppo%+", "soft%+", "med%+", "hard%+",

    "GB", "FB", "LD", "GB%", "FB%", "LD%", "GB/FB", "HR/FB",

    "xwoba", "xba", "xslg", "xiso", "xobp",
    "arm_strength", "sprint_speed", "oaa",
    "bat_speed", "squared_up_rate", "swing_length",

    "est_ba", "est_slg", "est_woba",
    "est_slg_minus_slg_diff", "est_woba_minus_woba_diff"
]


KEEP_RENAME_MAP = {
    "bref_war": batter_bref_war_keep_cols_rename,
    "stats": batter_stats_keep_cols_rename,
    "statcast_pct": batter_statcast_pct_keep_cols_rename,
    "statcast_exp": batter_statcast_exp_keep_cols_rename,
    "free_agents": batter_free_agent_rename,
}

