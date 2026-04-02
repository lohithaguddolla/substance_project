import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset
data = {
    'age': [18, 22, 25, 30, 35, 40, 28, 19],
    'stress': [3, 2, 3, 1, 2, 1, 3, 2],
    'sleep': [5, 6, 4, 7, 6, 8, 5, 6],
    'alcohol': [1, 0, 1, 0, 1, 0, 1, 0],
    'smoking': [1, 0, 1, 0, 1, 0, 1, 0],
    'risk': [2, 1, 2, 0, 1, 0, 2, 1]  # 0=Low, 1=Medium, 2=High
}

df = pd.DataFrame(data)

X = df.drop('risk', axis=1)
y = df['risk']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained successfully!")