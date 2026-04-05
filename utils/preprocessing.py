import pandas as pd

def clean_data(df):
    """
    Basic preprocessing steps for the nutrition dataset.
    """
    # Fill missing values
    df.fillna(0, inplace=True)
    
    # Ensure correct data types
    numeric_cols = ['calories', 'protein', 'fat', 'carbohydrates', 'sugar', 'sodium', 'fiber']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
    bool_cols = ['suitable_for_diabetes', 'suitable_for_hypertension', 'suitable_for_heart_disease']
    for col in bool_cols:
        df[col] = df[col].astype(bool)
        
    return df
