#!/usr/bin/env python
# coding: utf-8

# In[7]:


import ipywidgets as widgets
widgets.IntSlider()
import os
print(os.path.abspath('Untitled4.py'))



# In[2]:


import ipywidgets as widgets
from IPython.display import display, clear_output
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dummy stock data
dates = pd.date_range(start='2023-01-01', periods=100)
prices = np.cumsum(np.random.randn(100)) + 100

print('All Good')


# In[3]:


# Widgets
stock_picker = widgets.Dropdown(
    options=['AAPL', 'GOOGL', 'MSFT'],
    description='Stock:'
)
analyze_button = widgets.Button(description='Analyze Stock')



# In[4]:


# Output area
output = widgets.Output()



# In[5]:


# Callback function
def analyze_stock(b):
    with output:
        clear_output()
        # Simulate moving averages
        df = pd.DataFrame({'Date': dates, 'Price': prices})
        df['5-day MA'] = df['Price'].rolling(window=5).mean()
        df['30-day MA'] = df['Price'].rolling(window=30).mean()
        
        # Plot
        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df['Price'], label='Price')
        plt.plot(df['Date'], df['5-day MA'], label='5-day MA', linestyle='--')
        plt.plot(df['Date'], df['30-day MA'], label='30-day MA', linestyle='--')
        plt.legend()
        plt.title(f"Analysis for {stock_picker.value}")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid()
        plt.show()
        
        # Recommendation
        if df['5-day MA'].iloc[-1] > df['30-day MA'].iloc[-1]:
            print(f"Recommendation: BUY {stock_picker.value}")
        else:
            print(f"Recommendation: DO NOT BUY {stock_picker.value}")

print("all good")


# In[6]:


# Link button to function
analyze_button.on_click(analyze_stock)

# Display UI
display(stock_picker, analyze_button, output)


# In[ ]:




