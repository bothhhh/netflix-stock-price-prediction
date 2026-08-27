# Netflix Stock Price Prediction

## 📌 Project Overview

This project uses machine learning techniques to analyse historical Netflix stock market data and predict the **closing stock price** of Netflix.

The project involves data exploration, preprocessing, feature selection, model training, evaluation, and saving the final machine learning model.

## 🎯 Objective

The main objective of this project is to predict the **Netflix closing stock price** using historical stock market features.

This is a **supervised machine learning regression problem**.

## 📊 Dataset

The project uses historical Netflix stock data with features including:

* Date
* Open
* High
* Low
* Close
* Volume

The dataset was obtained from Kaggle.

> **Note:** The dataset is not included in this repository. Please obtain the dataset from the original source before running the project.

## 🔍 Project Workflow

The project follows these main steps:

1. Reading the dataset using Pandas
2. Removing duplicate records
3. Exploring and understanding the dataset
4. Visualising the target variable
5. Performing Exploratory Data Analysis (EDA)
6. Analysing outliers
7. Checking for missing values
8. Performing correlation and feature analysis
9. Selecting relevant features
10. Preparing data for machine learning
11. Splitting the dataset into training and testing sets
12. Normalising the data using Min-Max Scaling
13. Training multiple machine learning models
14. Evaluating and selecting a model
15. Saving the trained model for future predictions

## 🤖 Machine Learning Models

The following regression algorithms were investigated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* AdaBoost Regressor
* K-Nearest Neighbours (KNN) Regressor

The models were evaluated using regression performance metrics, including R² and prediction accuracy calculations.

## 🛠️ Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Pickle

## 📁 Repository Structure

```text
netflix-stock-price-prediction/
│
├── netflix_stock_price_prediction.ipynb
├── NetflixML.py
├── NetflixStockPredictionModel.pkl
└── README.md
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/netflix-stock-price-prediction.git
```

### 2. Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 3. Download the dataset

Download the Netflix stock dataset from the original Kaggle source.

Place the dataset in the appropriate project directory.

### 4. Run the notebook

Open the Jupyter Notebook file:

```text
netflix_stock_price_prediction.ipynb
```

You can run it using:

* Google Colab
* Jupyter Notebook
* Visual Studio Code

## 💾 Saved Model

The trained machine learning model is saved as:

```text
NetflixStockPredictionModel.pkl
```

The saved model can be loaded and used to make predictions based on input features such as:

* Open price
* High price
* Low price
* Trading volume

## 📈 Future Improvements

Possible future improvements include:

* Adding more historical data
* Improving feature engineering
* Experimenting with additional machine learning models
* Performing hyperparameter tuning
* Creating data visualisations for model predictions
* Developing a web application for stock price predictions

## 👥 Project Information

This project was developed as part of a group machine learning project.

## ⚠️ Disclaimer

This project is for educational and research purposes only. Stock market predictions involve uncertainty and should not be considered financial advice.

## 👨‍💻 Author

**Limpanhaboth Yin**

Software Engineering Student | Aspiring Software Developer

---

⭐ If you found this project interesting, feel free to explore the repository!
