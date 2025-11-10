import sys
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class Salary:
    def __init__(self, payroll_source_paths: dict, salary_source_paths: dict, recent_year: int = 2025):
        self.payroll_source_paths = payroll_source_paths
        self.salary_source_paths = salary_source_paths

        self.cached_payroll_source_path = os.getenv("CACHED_PAYROLL")
        self.cached_salary_source_path = os.getenv("CACHED_SALARY")

        self.recent_year = recent_year

    def _compile_payroll_df(self):
        """This function assumes that data has been copied manually from Spotrac.com for the recent year.
            The intention is to merge the larger data frame that is sourced from 2011 to 2024 with the most recent year
            of payrolls. In order to merge the two, the recent dataframe must be reformatted.
        """
        mlb_payrolls_recent_df = pd.read_csv(self.payroll_source_paths["recent"])
        mlb_payrolls_large_df = pd.read_csv(self.payroll_source_paths["historical"])

        # Rename columns to match the larger historical data set
        mlb_payrolls_recent_df = mlb_payrolls_recent_df.rename({
            'Avg AgeTeam': 'Average Age',
            'Total PayrollAllocations': 'Total Payroll Allocations',
            'Active26-Man': 'Active 26-Man'
        }, axis=1)

        mlb_payrolls_recent_df["Year"] = self.recent_year
        mlb_payrolls_recent_df["Wins"] = mlb_payrolls_recent_df.apply(lambda row: int(row["Record"].split("-")[0]), axis=1)
        mlb_payrolls_recent_df["Losses"] = mlb_payrolls_recent_df.apply(lambda row: int(row["Record"].split("-")[1]), axis=1)
        mlb_payrolls_recent_df = mlb_payrolls_recent_df.drop("Rank", axis=1)
        mlb_payrolls_recent_df = mlb_payrolls_recent_df.drop("Record", axis=1)

        # Extraneous columns
        mlb_payrolls_large_df = mlb_payrolls_large_df.drop(["Team Name", "Postseason"], axis=1)

        return pd.concat([mlb_payrolls_recent_df, mlb_payrolls_large_df]).sort_values(by="Year", ascending=False).reset_index(drop=True)
    

    def payroll(
        self,
        season: int | None = None
    ) -> pd.DataFrame:
        if (self.cached_payroll_source_path and 
            os.path.exists(self.cached_payroll_source_path)):
            payroll_df = pd.read_csv(self.cached_payroll_source_path)

        else:
            payroll_df = self._compile_payroll_df()
            
            if self.cached_payroll_source_path:
                # Save to the known cache path
                payroll_df.to_csv(self.cached_payroll_source_path)
            else:
                # Save here
                payroll_df.to_csv()

        return payroll_df[payroll_df["Year"] == season].reset_index(drop=True) if season else payroll_df.reset_index(drop=True)

