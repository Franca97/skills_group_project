# Import packages and libraries:
import pandas as pd
import numpy as np
# visualization
import matplotlib.pyplot as plt

# Import the dataset from http://codingxcamp.com/datasets/appl_1980_2014.csv
apple = pd.read_csv("http://codingxcamp.com/datasets/appl_1980_2014.csv")  # assign data frame to apple

# TASK 1: Assign it to a variable apple and read the head
apple.head()  # read the head

# TASK 2: Check out the type of the columns
apple.dtypes  # checking datatypes

# We transform the Date column as a datetime type
# it seems APPLE DOES NOT SUPPORT ANYMORE stock fetching - please try to use QUANDL instead(https://medium.com/python-data/quandl-getting-end-of-day-stock-data-with-python-8652671d6661)
# setting up
import quandl  # importing quandl

quandl.ApiConfig.api_key = '_ygDz5fgayR6fp7HybaW'  # specify api key to pull the data

# pulling data from quandl for the apple stock
apple = quandl.get_table("WIKI/PRICES", [ticker = "AAPL"],  # pulling data from quandl
qopts = {"columns: ["ticker", "date", "adj_close"]},"
date = {"gte": 2018 - 12 - 31, "lte": "2019-12-31"},
       paginate = TRUE)
apple.head()  # inspecting head()

# Transforming
apple.Date = pd.to_datetime(apple.Date)  # transform colunm as datetime type
apple['Date'].head()  # showing the head of the dataset

# TASK 3: Set the date as the index

# As the index is from the most recent date we make the first entry the oldest date.
apple.sort_index(ascending=True).head()  # therefore we order in ascending order and show the head of the table

# we get the last business day of each month
apple_month = apple.resample('BM').mean()
apple_month.head()  # showing the head

# Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches

