import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Invalid N (zero or negative)
    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    distinct_salaries = (
        employee['salary']
        .drop_duplicates()
        .sort_values(ascending=False)
    )
    
    # Not enough distinct salaries
    if N > len(distinct_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    return pd.DataFrame({
        f'getNthHighestSalary({N})': [distinct_salaries.iloc[N - 1]]
    })