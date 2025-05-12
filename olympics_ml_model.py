
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Excel
df = pd.read_excel("olympics_analysis_report.xlsx")

# Target column
df['Medal_Won'] = df['Medal'].notnull().astype(int)

# Features
df = df[['Year', 'Sport', 'Discipline', 'Gender', 'Country', 'Medal_Won']].dropna()

# Encode categorical
label_encoders = {}
for col in ['Sport', 'Discipline', 'Gender', 'Country']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

X = df.drop("Medal_Won", axis=1)
y = df["Medal_Won"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("✅ Accuracy:", round(accuracy_score(y_test, y_pred), 3))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
