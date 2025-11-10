from ._pybaseball import *

class PyBaseball:
    """Wrapper to encapsulate the pybaseball functions into logical
        objects.
    """
    def __init__(self):
        self.batter = Batter()
        self.draft_and_prospects = DraftAndProspects()
        self.fielder_and_runner = FielderAndRunner()
        # self.lahman = LahmanAPI() # Seems to not be in order
        self.league = League()
        self.pitcher = Pitcher()
        self.player_search = PlayerSearch()
        self.team = Team()