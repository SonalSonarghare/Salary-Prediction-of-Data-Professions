# 💼 Salary Prediction of Data Professions

This repository contains the code and resources for predicting salaries based on various factors such as experience, job role, and performance. The project aims to help job seekers and employers understand the variability in salaries within the data profession field.

## 📋 Table of Contents

- [📌 Problem Statement](#problem-statement)
- [📊 Dataset](#dataset)
- [🔍 Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [🛠️ Data Preprocessing](#data-preprocessing)
- [🧠 Model Development and Evaluation](#model-development-and-evaluation)
- [🏆 Model Selection](#model-selection)
- [💾 Model Saving and Feature Importance](#model-saving-and-feature-importance)
- [🌐 Model Deployment](#model-deployment)
- [📈 Conclusion](#conclusion)
- [📞 Contact](#contact)

## 📌 Problem Statement

The goal of this project is to highlight the variability in salaries based on experience, job role, and performance. Accurate salary predictions are important for job seekers and employers to make informed decisions.

## 📊 Dataset

The dataset contains information about various data professions, including features such as age, experience, job role, ratings, and salaries.

## 🔍 Exploratory Data Analysis (EDA)

1. Summary Statistics:
    - Display the first few rows, last few rows, and the shape of the dataset.
2. Data Visualization:
    - Visualize the distribution of sexes, designations, units, and ratings.
    - Plot salary distribution by sex and designation.

## 🛠️ Data Preprocessing

1. Fill null values in columns like `LAST NAME`, `DOJ`, `AGE`, `LEAVES USED`, `LEAVES REMAINING`, and `RATINGS`.
2. Perform One-Hot Encoding to convert categorical variables into a suitable format for model training.

## 🧠 Model Development and Evaluation

1. Train various regression models:
    - Linear Regression (0.942)
    - Decision Trees (0.91)
    - Random Forests (0.933)
    - Gradient Boosting (0.917)

2. Evaluate models using metrics such as RMSE, MAE, and R-squared.

## 🏆 Model Selection

The Linear Regression model was selected based on its superior performance across evaluation metrics. It achieved the lowest RMSE and MAE, along with the highest R-squared value (0.942).

## 💾 Model Saving and Feature Importance

1. Save the trained model to a file for future use.
2. Identify and display feature importance to understand the impact of different features on salary predictions.

## 🌐 Model Deployment

Deploy the selected model to a flask application for real-time salary predictions.
![image](https://github.com/SonalSonarghare/Salary-Prediction-of-Data-Professions/assets/116957485/ef483589-55b3-48f8-9107-a13e9bafbd2d)

## 📈 Conclusion

The Linear Regression model emerged as the best performer, exhibiting the lowest RMSE and MAE, and the highest R-squared value. Features such as age, past experience, and job role were significant predictors of salary. Continuous monitoring and feature engineering could further enhance model performance.

## 📞 Contact

For any queries or suggestions, feel free to contact:
- Sonal Sonarghare
- Email: sonalsonarghare30@gmail.com
- A.P. Shah Institute of Technology
