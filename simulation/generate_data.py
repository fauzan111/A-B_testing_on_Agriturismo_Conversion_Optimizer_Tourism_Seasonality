import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker with Italian locale
fake = Faker('it_IT')

def simulate_conversion(variant, region, date):
    """
    Simulates conversion probability based on Variant, Region, and Seasonality.
    
    Hypothesis: 
    - Variant B (Zero Km Food) performs better overall for Italians.
    - Effect is stronger in 'Foodie' regions (e.g., Emilia-Romagna, Sicily) vs 'Industrial' (Lombardy).
    - Seasonality: Ferragosto (Aug 15) and Pasquetta (Variable, say April) boost overall bookings, 
      but maybe 'Nature/Food' (B) appeals more during Pasquetta (Spring) and 'Pool' (A) during Ferragosto (Summer heat)?
      
    Let's stick to the user prompt: "Test if emphasizing 'Zero Km Food' converts better... for domestic travelers".
    """
    
    base_prob = 0.15 # Base conversion rate
    
    # Variant Effect
    if variant == 'B':
        base_prob += 0.05 # +5% for Zero Km Food (Italians love food)
        
    # Regional Effect (Simulated)
    # South/Islands might care more about tradition/food? Or maybe City dwellers (Lombardy) want nature?
    # Let's say Lombardy users are +2% likely to convert on B (escape to nature).
    if region == 'Lombardia':
        if variant == 'B':
            base_prob += 0.02
    elif region == 'Sicilia':
        # Maybe they prefer Pool (A) because it's hot?
        if variant == 'A':
            base_prob += 0.03

    # Seasonality Effect
    # Ferragosto (Aug 15) - Peak Summer. Pool (A) should be very popular.
    # Pasquetta (April) - Spring. Food/Nature (B) should be popular.
    
    month = date.month
    day = date.day
    
    # Simple seasonality curve
    if month == 8: # August
        base_prob += 0.10 # High demand
        if variant == 'A':
            base_prob += 0.05 # Pool is king in August heat
    elif month == 4: # April (Pasquetta approx)
        base_prob += 0.05
        if variant == 'B':
            base_prob += 0.05 # Spring picnic/food
            
    # Clamp probability
    prob = max(0.0, min(1.0, base_prob))
    
    return random.random() < prob

def generate_data(n_users=1000):
    data = []
    start_date = datetime(2024, 1, 1)
    
    print(f"Generating {n_users} synthetic users...")
    
    regions = [
        'Lombardia', 'Lazio', 'Campania', 'Sicilia', 'Veneto', 'Piemonte', 
        'Emilia-Romagna', 'Toscana', 'Puglia', 'Calabria'
    ]
    
    for _ in range(n_users):
        # User Attributes
        user_id = fake.uuid4()
        name = fake.name()
        address = fake.address()
        region = random.choice(regions) # fake.region() might not be available
        
        # Experiment Assignment
        variant = random.choice(['A', 'B'])
        
        # Simulation Date (random day in year)
        days_offset = random.randint(0, 365)
        date = start_date + timedelta(days=days_offset)
        
        # Outcome
        converted = simulate_conversion(variant, region, date)
        
        data.append({
            'user_id': user_id,
            'name': name,
            'region': region,
            'variant': variant,
            'date': date,
            'converted': 1 if converted else 0
        })
        
    df = pd.DataFrame(data)
    df.to_csv('experiment_data.csv', index=False)
    print("Data generated and saved to 'experiment_data.csv'")
    return df

if __name__ == "__main__":
    generate_data(2000)
