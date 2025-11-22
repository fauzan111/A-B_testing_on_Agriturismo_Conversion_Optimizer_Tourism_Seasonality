import pandas as pd
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

def analyze_results():
    print("Loading data...")
    try:
        df = pd.read_csv('experiment_data.csv')
    except FileNotFoundError:
        print("Error: 'experiment_data.csv' not found. Run generate_data.py first.")
        return

    print(f"Total records: {len(df)}")
    
    # 1. Basic Conversion Rates
    print("\n--- Basic Conversion Rates ---")
    conversion_rates = df.groupby('variant')['converted'].mean()
    print(conversion_rates)
    
    # 2. T-Test
    print("\n--- T-Test (A vs B) ---")
    group_a = df[df['variant'] == 'A']['converted']
    group_b = df[df['variant'] == 'B']['converted']
    
    t_stat, p_val = stats.ttest_ind(group_a, group_b)
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_val:.4f}")
    
    if p_val < 0.05:
        print("Result is Statistically Significant!")
    else:
        print("Result is NOT Statistically Significant.")

    # 3. Logistic Regression (controlling for Region and Season)
    print("\n--- Logistic Regression Analysis ---")
    # Extract month for seasonality
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    
    # Formula: converted ~ variant + region + month
    # We treat region and month as categorical? Maybe just month as continuous for simplicity or factor.
    # Let's use C() for categorical
    
    model = smf.logit("converted ~ C(variant) + C(region) + C(month)", data=df)
    result = model.fit()
    
    print(result.summary())

if __name__ == "__main__":
    analyze_results()
