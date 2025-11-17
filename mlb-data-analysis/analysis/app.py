import pandas as pd
from shiny import App, ui, render
from pathlib import Path

from dotenv import load_dotenv
from utils import monetary_string_to_numeric

load_dotenv()

BASE_DIR = Path(__file__).parent
FREE_AGENT_EVAL_DATAFRAME_PATH = BASE_DIR / "data" / "Free Agent Batters 2026 Eval.csv"
BATTER_WAR_PROJECTIONS_DATAFRAME_PATH = BASE_DIR / "data" / "2026 Batter WAR Projections.csv"

# --- Sample DataFrame ---
df = pd.read_csv(FREE_AGENT_EVAL_DATAFRAME_PATH)

war_df = pd.read_csv(BATTER_WAR_PROJECTIONS_DATAFRAME_PATH)
war_df["WAR_based_salary_projection"] = (
    war_df[["predicted_target_fWAR", "predicted_target_bWAR"]].mean(axis=1) * 9_000_000
)

df = df.merge(
    war_df,
    how="left",
    on="player_name"
)

columns = [
    "season", 
    "player_name", 
    "age", 
    "pos",
    "predicted_value",
    "predicted_contract_years",
    "predicted_AAV",
    "market_value_AAV",
    "predicted_target_fWAR",
    "predicted_target_bWAR",
    "WAR_based_salary_projection"
]

# Reorder the columns correctly
df = df[columns]

APP_DESCRIPTION = """
    This table provides an analysis of MLB hitter free agents for the 2026 season. All columns prefixed by 
    predicted_ have been predicted by my model for the 2026 season. The column market_AAV is taken from spotrac.com for the 2026 season.
    Rows in green show players that are predicted to provide excess value over this market prediction for the 2026 season. 
    You can select which methodology to determine this excess value by toggling the 'Salary Model' feature. 
    'Standard' uses a model that predicts AAV salary from player performance. 'WAR Based' uses a projection 
    model to determine the player's WAR next year and mutiplies that value by a rough market estimate of $9,000,000/WAR
    to predict value for the next year.
"""

# --- UI ---
app_ui = ui.page_fluid(
    ui.h2("Free Agent Evaluation 2026"),
    ui.p(APP_DESCRIPTION),
    ui.input_select(
        "sort_col",
        "Sort by:",
        {
            "predicted_AAV": "Predicted AAV",
            "market_value_AAV": "Market AAV",
            "predicted_value": "Predicted Value",
            "predicted_contract_years": "Predicted Years",
            "WAR_based_salary_projection": "WAR Based Salary Projection"
        },
        selected="predicted_AAV",
    ),
    ui.input_radio_buttons(
        "sort_dir",
        "Direction:",
        {
            "asc": "Ascending",
            "desc": "Descending",
        },
        selected="desc",
        inline=True,
    ),
    ui.input_radio_buttons(
        "salary_model",
        "Salary Model:",
        {
            "std": "Standard",
            "war": "War Based",
        },
        selected="std",
        inline=True,
    ),
    ui.output_data_frame("table")
)

# --- Server ---
def server(input, output, session):
    @output
    @render.data_frame
    def table():
        df_num = df.copy()

        # 1. Make numerics
        for col in [
            "predicted_AAV",
            "market_value_AAV",
            "predicted_value",
            "WAR_based_salary_projection",
        ]:
            df_num[col] = df_num[col].apply(monetary_string_to_numeric)

        # 2. Custom sort
        sort_col = input.sort_col()
        ascending = (input.sort_dir() == "asc")
        df_sorted = df_num.sort_values(by=sort_col, ascending=ascending)

        # IMPORTANT: reset index so rows are 0..N-1
        df_sorted = df_sorted.reset_index(drop=True)

        # 3. Green vs red row masks
        if input.salary_model() == "war":
            green_mask = df_sorted["WAR_based_salary_projection"] > df_sorted["market_value_AAV"]
            red_mask   = df_sorted["WAR_based_salary_projection"] <= df_sorted["market_value_AAV"]
        else:
            green_mask = df_sorted["predicted_AAV"] > df_sorted["market_value_AAV"]
            red_mask   = df_sorted["predicted_AAV"] <= df_sorted["market_value_AAV"]

        # Now df_sorted.index is 0..N-1, so this is safe:
        green_rows = df_sorted.index[green_mask].tolist()
        red_rows   = df_sorted.index[red_mask].tolist()

        # 4. All column positions
        all_cols = list(range(len(df_sorted.columns)))

        styles = []
        if green_rows:
            styles.append({
                "location": "body",
                "rows": green_rows,
                "cols": all_cols,
                "style": {"background-color": "#9ecb9e", "color": "white"},
            })
        if red_rows:
            styles.append({
                "location": "body",
                "rows": red_rows,
                "cols": all_cols,
                "style": {"background-color": "#cb9e9e", "color": "white"},
            })

        # 5. Turn the numeric columns back into strings for display
        for col in [
            "predicted_AAV",
            "market_value_AAV",
            "predicted_value",
            "WAR_based_salary_projection",
        ]:
            df_sorted[col] = df_sorted[col].apply(lambda x: f"${x:,.0f}")

        return render.DataGrid(
            df_sorted,
            filters=True,
            styles=styles,
        )

# --- App ---
app = App(app_ui, server)
