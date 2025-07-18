# 🌾 Crop Yield Prediction using FAOSTAT Data

## 🎯 Objective
To demonstrate how supervised machine learning (linear regression) can be used to predict agricultural crop yields using FAOSTAT data, supporting **UN SDG 2: Zero Hunger**.

## 📂 Dataset
- **Source**: [FAOSTAT](https://www.fao.org/faostat/)
- **File**: `FAOSTAT_data_en_7-18-2025.csv`
- **Domain**: Crops and Livestock Products
- **Preview**:

| Area        | Element        | Unit   | Value  |
| ----------- | -------------- | ------ | ------ |
| Afghanistan | Area harvested | ha     | 96000  |
| Afghanistan | Yield          | kg/ha  | 1197.9 |
| Afghanistan | Production     | tonnes | 115000 |


## 🧠 ML Technique
- Type: **Supervised Learning**
- Model: **Linear Regression**
- Features: Rainfall, Temperature (if available)
- Target: Yield (kg/ha)

## 🛠️ Tools & Libraries
- Python
- Pandas, Matplotlib, Seaborn
- Scikit-learn

## 📊 Results
- **Mean Absolute Error**: 2178.98
- **R² Score**: 0.07

## 🧭 Insights
While the model's predictive accuracy is limited, it highlights how climate variables impact yield. With more comprehensive data (e.g., soil quality, irrigation), performance could be significantly improved.

## 🔐 Ethical Considerations
- Potential data bias due to incomplete reporting.
- Smallholder farmers may be underrepresented.
- Model decisions should not be deployed in isolation without expert oversight.

## 💡 Next Steps
- Integrate additional environmental and economic features.
- Use time-series data for trend analysis.
- Explore more advanced models (e.g., Random Forest, XGBoost).

## 📌 Author
- Part of the **PLP Academy AI for Sustainable Development (Week 2 Assignment)**.
- [GitHub](https://github.com/mosesakpala)
