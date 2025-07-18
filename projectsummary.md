Project Title: Crop Yield Prediction using FAOSTAT Data
SDG Goal Addressed: SDG 2 - Zero Hunger

Problem Statement:
Agricultural productivity is essential for achieving food security. However, crop yields are impacted by unpredictable factors such as rainfall and temperature. This project leverages machine learning to help farmers and policymakers make data-driven decisions that can optimize food production.

Machine Learning Approach:
A supervised learning technique, specifically linear regression, was used to model the relationship between environmental features and crop yield.

Dataset Used:
The data was sourced from the FAOSTAT Crops and Livestock Products dataset, containing agricultural records from Afghanistan, including:

Yield (kg/ha)

Area harvested (ha)

Production (tonnes)

Rainfall and Temperature (manually extracted or assumed)

Model Performance:

Mean Absolute Error (MAE): 2178.98

R² Score: 0.07

Ethical Considerations:

The dataset may lack coverage of smallholder farmers or regions with underreported data.

Model accuracy is low, suggesting that crop yield is influenced by more variables than just rainfall and temperature.

Conclusion:
This project shows the potential of ML in supporting SDG 2. With improved datasets (e.g., soil quality, irrigation data), the model could assist in early crop failure warnings and smarter agricultural planning.