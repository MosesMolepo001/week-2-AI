import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load the dataset
df = pd.read_csv("FAOSTAT_data_en_7-18-2025.csv")

# Display the first few rows
print("Dataset Preview:")
print(df.head())

# Clean and preprocess (update column names as needed)
# Example assumes your CSV has columns named exactly like these
# Filter for 'Yield' data and rename 'Value' column
df = df[df['Element'] == 'Yield'].rename(columns={'Value': 'Yield'})

# Drop any rows with missing values in 'Yield' or 'Year'
df = df.dropna(subset=["Yield", "Year"])

# Define input features and target variable
X = df[["Year"]]
y = df["Yield"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n📊 Model Performance:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot: Actual vs Predicted
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Crop Yield")
plt.grid(True)
plt.tight_layout()
plt.show()
