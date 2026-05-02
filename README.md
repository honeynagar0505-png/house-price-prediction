# House Price Prediction using Machine Learning

## Overview

This project predicts house prices based on features such as area, number of bedrooms, and bathrooms using a Machine Learning model.

The purpose of this project is to understand the complete machine learning workflow, including data preprocessing, feature selection, model training, evaluation, and prediction.

---

## Features

* Exploratory Data Analysis (EDA)
* Data Cleaning and Preprocessing
* Linear Regression Model
* Data Visualization
* Model Evaluation using error metrics
* Prediction for new input data

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Project Structure

```
HousePricePrediction/
│── main.py
│── data.csv
│── README.md
```

---

## Dataset

The dataset includes the following features:

* area: Size of the house (in square feet)
* bedrooms: Number of bedrooms
* bathrooms: Number of bathrooms
* price: Target variable (house price)

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
```

### 2. Install dependencies

```
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Run the project

```
python main.py
```

---

## Machine Learning Workflow

1. Load dataset
2. Handle missing values
3. Select features and target variable
4. Split dataset into training and testing sets
5. Train model using Linear Regression
6. Make predictions
7. Evaluate model using Mean Squared Error
8. Visualize results

---

## Model Evaluation

The model is evaluated using:

Mean Squared Error (MSE)

Lower values indicate better model performance.

---

## Example Prediction

Input:

```
Area = 1600
Bedrooms = 3
Bathrooms = 2
```

Output:

```
Predicted Price ≈ XX,XX,XXX
```

---

## Future Improvements

* Use a larger real-world dataset
* Implement advanced models like Random Forest and Decision Tree
* Perform hyperparameter tuning
* Deploy the project using Streamlit
* Add a user interface for inputs

---

## Contributing

Contributions are welcome. You can fork the repository and submit improvements.

---

## Contact

GitHub: https://github.com/yourusername

---

## Acknowledgment

This project is developed for learning and demonstrating machine learning concepts.

