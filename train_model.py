import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv('training_data.csv')

# Drop completely empty columns (like 'Unnamed: 133')
df = df.dropna(axis=1, how='all')

# Separate features and target
if 'prognosis' in df.columns:
    X = df.drop(['prognosis'], axis=1)
    y = df['prognosis']
else:
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

# Fill any remaining missing values with 0
X = X.fillna(0)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes model
clf = GaussianNB()
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model trained successfully!")
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(clf, file)

print("\nModel saved successfully as 'model.pkl'.")
