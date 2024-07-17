# Bengaluru House Price Prediction

## Overview
This project predicts house prices in Bengaluru using a linear regression model. The model takes into account various attributes like square footage, number of bedrooms (BHK), location, and number of bathrooms.

## Dataset
The dataset includes the following features:
- `location`: The location of the house.
- `size`: The size of the house in BHK (e.g., 2 BHK, 3 BHK).
- `total_sqft`: The total area of the house in square feet.
- `bath`: The number of bathrooms.
- `price`: The price of the house (target variable).

## Methodology
1. **Data Loading and Preprocessing**: The dataset is loaded and cleaned to handle missing values, remove duplicates, and convert relevant columns to numerical types.
2. **Exploratory Data Analysis (EDA)**: EDA is conducted to understand the distribution and relationships within the data, using visualizations to identify patterns and correlations.
3. **Feature Engineering**: New features are created, and categorical variables are converted into numerical ones using techniques like one-hot encoding. Data is normalized to ensure all features contribute equally to the model.
4. **Model Training**: The dataset is split into training and testing sets, and a linear regression model is trained on the training set to predict house prices.
5. **Evaluation**: The model's performance is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to assess accuracy and reliability.
6. **Inference**: The trained model is used to make predictions on new data, providing estimated house prices based on the input features.

## Strengths of Techniques Used
1. **Data Cleaning and Preprocessing**: Ensures high-quality data for training, crucial for model performance.
2. **Exploratory Data Analysis (EDA)**: Helps in understanding the data and identifying key features influencing house prices.
3. **Feature Engineering**: Transforms raw data into meaningful features, improving the model's predictive power.
4. **Linear Regression Model**: A simple yet effective model for predicting house prices, providing interpretable results.

## Acknowledgements
This project uses data and techniques to provide accurate and reliable house price predictions for Bengaluru.
