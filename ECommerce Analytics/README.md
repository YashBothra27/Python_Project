## 🛒 E-Commerce Business Analytics & Return Prediction

### 📌 Project Overview

This project focuses on analyzing a large-scale e-commerce dataset to extract business insights and build machine learning models for prediction tasks.

The analysis includes:
* Exploratory Data Analysis (EDA)
* Revenue and sales insights
* Customer behavior analysis
* Machine learning models for price prediction and return prediction

---

### 📂 Dataset

* Source: Kaggle
* Dataset: Amazon E-Commerce Dataset
* Link: https://www.kaggle.com/datasets/sharmajicoder/amazon-e-commerce

### 📊 Dataset Features:

* Product details (category, subcategory, brand)
* Pricing (price, discount, final_price)
* Customer interaction (rating, review_count)
* Transaction details (payment_method, location, device)
* Logistics (shipping_time_days, delivery_status)
* Target variable: `is_returned`

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn

---

## ⚙️ Workflow

### 1. Data Loading

* Imported dataset into a Pandas DataFrame
* Inspected structure using `.head()` and `.info()`

### 2. Data Cleaning

* Handled missing values and duplicates
* Converted data types (dates, numerical values)
* Removed irrelevant columns (IDs, unnecessary features)

### 3. Data Analysis

* Performed statistical analysis
* Explored trends across categories, pricing, and customer behavior

### 4. Data Visualization

* Created visualizations for:
  * Category distribution
  * Price distribution by category
  * Revenue by category
  * Monthly revenue trends
  * Payment method distribution
  * Revenue by location

### 5. Machine Learning

* Built classification model (Random Forest) for return prediction
* Built regression model (Linear Regression) for price prediction
* Evaluated models using appropriate metrics

---

## ⚠️ Key Learning

* Including `price` leads to artificially high accuracy (data leakage)
* Removing it results in realistic but lower performance
* Feature selection is critical in machine learning

---

## 💡 Business Impact

* Helps identify revenue-driving categories
* Supports pricing strategy decisions
* Enables return prediction to reduce logistics cost
* Provides insights for customer behavior and demand

---

## 📈 Key Insights

* Product distribution is balanced across categories
* Electronics category generates the highest revenue
* Sales show seasonal trends across months
* Payment methods are evenly distributed
* Return prediction model performs well for non-returns but struggles with returns
* Price prediction model shows low performance without base price (due to feature limitation)

---

## 📌 Conclusion

This project demonstrates how data analysis and machine learning can be used to extract meaningful insights and support decision-making in an e-commerce environment.

---

## 👨‍💻 Author

Yash Kumar Bothra

---

⭐ If you found this project useful, feel free to explore and give it a star!
