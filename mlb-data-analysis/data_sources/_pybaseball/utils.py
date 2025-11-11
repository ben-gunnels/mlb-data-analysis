TEAM_CODES = {
    "Angels": "ANA",
    "Astros": "HOU",
    "Athletics": "OAK",
    "Blue Jays": "TOR",
    "Braves": "ATL",
    "Brewers": "MIL",
    "Cardinals": "STL",
    "Cubs": "CHC",
    "Rays": "TBD",
    "Diamondbacks": "ARI",
    "Dodgers": "LAD",
    "Giants": "SFG",
    "Guardians": "CLE",
    "Mariners": "SEA",
    "Marlins": "FLA",
    "Mets": "NYM",
    "Nationals": "WSN",
    "Orioles": "BAL",
    "Padres": "SDP",
    "Phillies": "PHI",
    "Pirates": "PIT",
    "Rangers": "TEX",
    "Red Sox": "BOS",
    "Reds": "CIN",
    "Rockies": "COL",
    "Royals": "KCR",
    "Tigers": "DET",
    "Twins": "MIN",
    "White Sox": "CHW",
    "Yankees": "NYY"
}

PITCH_CODES = set(
    [
        "4-Seamer", 
        "Sinker", 
        "Changeup", 
        "Curveball", 
        "Cutter", 
        "Slider", 
        "Sinker",
        "FF", 
        "SIFT", 
        "CH", 
        "CUKC", 
        "FC", 
        "SL", 
        "FS", 
        "ALL"
    ]
)

LEAGUE_MINIMUM_BY_YEAR = {
    # 2022–2026 (2022 CBA)
    2022: 700_000,
    2023: 720_000,
    2024: 740_000,
    2025: 760_000,
    2026: 780_000,

    # 2017–2021 (2017 CBA)
    2017: 535_000,
    2018: 545_000,
    2019: 555_000,
    2020: 563_500,
    2021: 570_500,

    # 2012–2016 (2012 CBA)
    2012: 480_000,
    2013: 480_000,
    2014: 480_000,
    2015: 507_500,
    2016: 507_500,

    # 2007–2011 (2007 CBA)
    2007: 380_000,
    2008: 390_000,
    2009: 400_000,
    2010: 400_000,
    2011: 414_000,

    # 2003–2006 (2003 CBA)
    2003: 300_000,
    2004: 300_000,
    2005: 316_000,
    2006: 327_000,

    # 2002 (single-year)
    2002: 300_000,

    # 1997–2001 (1997 CBA)
    1997: 150_000,
    1998: 170_000,
    1999: 200_000,
    2000: 200_000,
    2001: 200_000,

    # 1995–1996 (1995 CBA)
    1995: 109_000,
    1996: 109_000,

    # 1994 (pre-1995)
    1994: 109_000,

    # 1990–1993 (1990 CBA)
    1990: 100_000,
    1991: 100_000,
    1992: 109_000,
    1993: 109_000,
}