import pandas as pd
import numbers
import numpy as np

__all__ = ["describe_endpoint", "compile_average_player_values", "monetary_string_to_numeric"]

def describe_endpoint(name, df):
    """Formats the DataFrame info string for writing."""
    buf = []
    buf.append(f"Endpoint: {name}")
    buf.append("-" * 50)
    # Capture the output of df.info()
    from io import StringIO
    s = StringIO()
    if type(df) is pd.DataFrame:
        df.info(buf=s, verbose=True)
    else:
        buf.append(f"Type: {type(df)}")
        buf.append("Not a DataFrame.")
    s.seek(0)
    buf.append(s.read().rstrip())
    buf.append("-"*50)
    buf.append("\n")  # blank line between endpoints
    return "\n".join(buf)


def compile_average_player_values(player_value_stats: list[str], stats_df: pd.DataFrame) -> dict:
    average_player_values = {}

    for stat in player_value_stats:
        if "&" in stat: # Want to sum over multiple stats
            all_stats = stat.split("&")
            _stats = stats_df[all_stats].sum(axis=1)

        elif "+" in stat: # Stats where 100 is league average, subtract 100 to get relative value
            _stats = stats_df[stat] - 100
            _stats = _stats[_stats > 0] # Only look at positive players

        else:
            _stats = stats_df[stat]

        stat_per_dollar = (_stats / stats_df["salary"]).mean()
        dollar_per_stat = 1 / stat_per_dollar

        average_player_values[f"dollar_per_{stat}"] = dollar_per_stat

    return  average_player_values


def monetary_string_to_numeric(
    monetary_val: str | numbers.Number, 
):
    if isinstance(monetary_val, numbers.Number):
        return np.float64(monetary_val)
    
    # strip dollar char and commas
    monetary_val = (
        monetary_val
        .replace("$", "")
        .replace(",", "")
    ) 

    return np.float64(monetary_val)



    