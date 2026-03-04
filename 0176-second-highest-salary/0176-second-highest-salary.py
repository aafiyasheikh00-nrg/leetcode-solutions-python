import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get distinct salaries in descending order
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # If there is no second highest salary
    if len(salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    
    # Return the second highest salary
    return pd.DataFrame({'SecondHighestSalary': [salaries.iloc[1]]})