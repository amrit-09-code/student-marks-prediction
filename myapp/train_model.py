import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

data = {
    'study_hours': [2, 5, 8, 3, 7, 9, 4, 6, 1, 10],
    'attendance': [60, 85, 95, 70, 90, 98, 75, 88, 50, 99],
    'previous_marks': [40, 65, 85, 50, 78, 92, 60, 72, 30, 95],
    'sleep_hours': [6, 7, 8, 5, 7, 8, 6, 7, 5, 8],
    'final_marks': [45, 68, 88, 52, 80, 94, 62, 75, 35, 97]
}

df = pd.DataFrame(data)
X = df[['study_hours','attendance','previous_marks','sleep_hours']]
y = df['final_marks']

model = RandomForestRegressor()
model.fit(X, y)

path = os.path.join(os.path.dirname(__file__), 'model.pkl')
with open(path, 'wb') as f:
    pickle.dump(model, f)

print("Model trained successfully!")