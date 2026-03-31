import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

DATA_FILE = 'data.csv'
MODEL_FILE = 'model.pkl'

def generate_synthetic_data(num_samples=200):
    """Generates a synthetic supply chain dataset and saves it to data.csv.
    Input features: distance, traffic level (1-3), weather condition (0/1)
    Output: delay (0 = on time, 1 = delayed)
    """
    np.random.seed(42)
    # distance: random value between 10 and 1000 km
    distances = np.random.uniform(10, 1000, num_samples)
    # traffic: 1 (low), 2 (medium), 3 (high)
    traffic_levels = np.random.randint(1, 4, num_samples)
    # weather: 0 (clear), 1 (bad)
    weather_conditions = np.random.randint(0, 2, num_samples)
    
    # Calculate delay logic
    delays = []
    for d, t, w in zip(distances, traffic_levels, weather_conditions):
        # A simple logic: if distance is long and traffic is high or weather is bad -> delay
        # We add some randomness
        delay_prob = 0.1
        if d > 500:
            delay_prob += 0.3
        if t == 3:
            delay_prob += 0.4
        elif t == 2:
            delay_prob += 0.2
        if w == 1:
            delay_prob += 0.3
            
        is_delayed = 1 if np.random.rand() < delay_prob else 0
        delays.append(is_delayed)
        
    df = pd.DataFrame({
        'distance': distances,
        'traffic': traffic_levels,
        'weather': weather_conditions,
        'delay': delays
    })
    
    # Save the sample dataset inside the project
    df.to_csv(DATA_FILE, index=False)
    print(f"Generated synthetic {DATA_FILE} with {num_samples} records.")
    return df

def train_model():
    """Loads dataset, trains a Random Forest model, and saves it."""
    # Check if data exists, if not generate it
    if not os.path.exists(DATA_FILE):
        df = generate_synthetic_data()
    else:
        df = pd.read_csv(DATA_FILE)
        
    X = df[['distance', 'traffic', 'weather']]
    y = df['delay']
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Test model accuracy
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model trained successfully! Accuracy: {accuracy:.2f}")
    
    # Save the trained model as a .pkl file
    with open(MODEL_FILE, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_FILE}")

if __name__ == '__main__':
    train_model()
