import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sqlalchemy import create_engine

# Create a connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:123456@localhost:5432/customer_purchase_db1')

# Query the database and load data into a DataFrame
query = """
SELECT customer_id, product_category, payment_method, value_usd, time_on_site, clicks_in_site
FROM purchases;
"""
df = pd.read_sql(query, engine)

# Preprocess data (example: create features and target variable)
df['target'] = df['value_usd'].apply(lambda x: 1 if x > 50 else 0)  # Example target variable

# One-hot encode categorical variables
df = pd.get_dummies(df, columns=['product_category', 'payment_method'])

X = df.drop('target', axis=1)
y = df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
