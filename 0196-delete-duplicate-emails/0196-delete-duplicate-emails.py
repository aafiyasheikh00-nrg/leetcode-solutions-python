import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by id so the smallest id comes first
    person.sort_values(by='id', inplace=True)
    
    # Drop duplicate emails, keeping the first (smallest id)
    person.drop_duplicates(subset='email', keep='first', inplace=True)