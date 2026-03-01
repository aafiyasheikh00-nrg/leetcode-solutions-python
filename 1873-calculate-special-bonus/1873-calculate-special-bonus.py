import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Create bonus column with default value 0
    employees["bonus"] = 0

    # Apply condition:
    # odd employee_id AND name does not start with 'M'
    condition = (employees["employee_id"] % 2 == 1) & (~employees["name"].str.startswith("M"))

    # Give full salary as bonus where condition is true
    employees.loc[condition, "bonus"] = employees.loc[condition, "salary"]

    # Return required columns sorted by employee_id
    return employees[["employee_id", "bonus"]].sort_values("employee_id")