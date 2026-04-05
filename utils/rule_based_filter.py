import pandas as pd

def apply_rules(df, diabetes, hypertension, obesity, heart_disease):
    filtered_df = df.copy()
    
    if diabetes:
        # Remove foods not suitable for diabetes or high in sugar
        filtered_df = filtered_df[(filtered_df['suitable_for_diabetes'] == True) & (filtered_df['sugar'] < 10)]
        
    if hypertension:
        # Remove foods not suitable for hypertension or high in sodium
        filtered_df = filtered_df[(filtered_df['suitable_for_hypertension'] == True) & (filtered_df['sodium'] < 400)]
        
    if heart_disease:
        # Remove foods not suitable for heart disease
        filtered_df = filtered_df[(filtered_df['suitable_for_heart_disease'] == True) & (filtered_df['fat'] < 15)]
        
    if obesity:
        # Restrict high calorie and high fat foods
        filtered_df = filtered_df[(filtered_df['calories'] < 400) & (filtered_df['fat'] < 20)]
        
    return filtered_df
