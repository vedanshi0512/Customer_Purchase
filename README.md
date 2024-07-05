# Project Name

## Overview

This project consists of several Python scripts designed for data loading, analysis, predictive modeling, and interactive SQL querying. Each script serves a specific purpose in managing and analyzing data from a PostgreSQL database.

## Project Structure

- [**load_data.py**](load_data.py): Establishes a connection to the PostgreSQL database and loads data into Pandas DataFrames.
  
- [**data_analysis.py**](data_analysis.py): Generates visualizations (e.g., bar charts, line charts) using Seaborn and Matplotlib to analyze data trends and patterns.
  
- [**predictive_model.py**](predictive_model.py): Builds and evaluates predictive models, providing accuracy metrics and confusion matrices for model performance assessment.
  
- [**predictive_data.py**](predictive_data.py): Provides an interactive platform for executing SQL queries against the PostgreSQL database.

## Setup

### Prerequisites

- Python 3.x
- Required Python packages: pandas, sqlalchemy, seaborn, matplotlib (install using `pip install pandas sqlalchemy seaborn matplotlib`)

### Configuration

1. Update database credentials in `load_data.py`:
   ```python
   DB_USER = 'your_username'
   DB_PASSWORD = 'your_password'
   DB_HOST = 'localhost'
   DB_PORT = '5432'
   DB_NAME = 'your_database_name'
2. Ensure your PostgreSQL database is running and accessible.

# Usage

## 1. Loading Data (load_data.py)
Connects to the PostgreSQL database and loads data into Pandas DataFrames.
![first 5 of table.jpeg](https://github.com/vedanshi0512/Customer_Purchase/blob/master/first%205%20of%20table.jpeg)

## 2. Data Analysis (data_analysis.py)
Generates visualizations to analyze data trends (e.g., total purchases per customer).

## 3. Predictive Modeling (predictive_model.py)
Builds machine learning models and evaluates their performance with accuracy metrics and confusion matrices.

![predictive model.jpeg](https://github.com/vedanshi0512/Customer_Purchase/blob/master/predictive%20model.jpeg)


## 4. Interactive SQL Queries (predictive_data.py)
Allows users to execute SQL queries interactively against the PostgreSQL database.
![sql query.jpeg](https://github.com/vedanshi0512/Customer_Purchase/blob/master/sql%20query.jpeg)


### Explanation

- The links [**Total Purchases per Customer**](https://github.com/vedanshi0512/Customer_Purchase/blob/master/Total%20purchases%20per%20customer.pdf) and [**Total Value of Purchases per Customer**](total_value_of_purchases_per_customer.pdf) link to the respective PDF files.
- Ensure the PDF files total_purchases_per_customer.pdf and total_value_of_purchases_per_customer.pdf are in the same directory as the README.

### Example Folder Structure


# Example Queries

To retrieve the first 10 entries of customer purchase data:

``` SELECT customer_id, COUNT(*) AS total_purchases, SUM(value_usd) AS total_value
FROM purchases
GROUP BY customer_id
LIMIT 10;
```

# Notes

Adjust SQL queries, visualization parameters, and machine learning models as per your specific requirements.

Ensure proper error handling and validation for user inputs in interactive components (predictive_data.py).

## Owner

[Vedanshi](https://github.com/vedanshi0512)
