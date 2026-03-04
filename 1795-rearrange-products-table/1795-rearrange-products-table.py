import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Convert wide table to long format
    result = products.melt(
        id_vars='product_id',
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )
    
    # Remove rows where the product is not available (price is null)
    result = result.dropna(subset=['price'])
    
    return result