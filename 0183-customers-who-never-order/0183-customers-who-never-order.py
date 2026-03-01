import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_customers = orders["customerId"]
    
    # Step 2: Select customers whose id is NOT in ordered_customers
    result = customers[~customers["id"].isin(ordered_customers)]
    
    # Step 3: Return only the name column with correct column name
    return result[["name"]].rename(columns={"name": "Customers"})