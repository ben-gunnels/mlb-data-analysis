import pandas as pd
import os
from shiny import App, ui, render

from dotenv import load_dotenv
from utils import monetary_string_to_numeric

load_dotenv()

FREE_AGENT_EVAL_DATAFRAME_PATH = os.getenv("MLB_FREE_AGENTS_2026_EVAL_TABLE")

# --- Sample DataFrame ---
df = pd.read_csv(FREE_AGENT_EVAL_DATAFRAME_PATH)

columns = [
    "season", 
    "player_name", 
    "age", 
    "pos",
    "predicted_value",
    "predicted_contract_years",
    "predicted_AAV",
    "market_value_AAV",
]

# Reorder the columns correctly
df = df[columns]

# --- UI ---
app_ui = ui.page_fluid(
    ui.h2("Free Agent Evaluation 2026"),
    ui.input_select(
        "sort_col",
        "Sort by:",
        {
            "predicted_AAV": "Predicted AAV",
            "market_value_AAV": "Market AAV",
            "predicted_value": "Predicted Value",
            "predicted_contract_years": "Predicted Years",
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
    ui.output_data_frame("table")
)

# --- Server ---
def server(input, output, session):
    @output
    @render.data_frame
    def table():
        df_num = df.copy()
        for col in ["predicted_AAV", "market_value_AAV", "predicted_value"]:
            df_num[col] = df_num[col].apply(monetary_string_to_numeric)

        # --- 2. Apply *your* custom sort based on UI inputs ---
        sort_col = input.sort_col()
        ascending = (input.sort_dir() == "asc")
        df_sorted = df_num.sort_values(by=sort_col, ascending=ascending)

        # Which rows should be green vs red?
        green_rows = df_sorted.index[df_sorted["predicted_AAV"] > df_sorted["market_value_AAV"]].tolist()
        red_rows   = df_sorted.index[df_sorted["predicted_AAV"] <= df_sorted["market_value_AAV"]].tolist()

        # All column indices (so the *whole* row gets colored)
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

        # Turn the sorted columns back into strings
        for col in ["predicted_AAV", "market_value_AAV", "predicted_value"]:
            df_sorted[col] = (
                df_sorted[col]
                .apply(lambda x: f"${x:,.0f}")
            )

        return render.DataGrid(
            df_sorted,
            filters=True,
            styles=styles
        )

# --- App ---
app = App(app_ui, server)
