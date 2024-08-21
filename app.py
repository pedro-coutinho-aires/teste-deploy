apt-get matplotlib

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setting the title of the dashboard
st.title('Dashboard Example with Two Columns and Graph Gallery')

# Example data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 8]
})

# Two columns layout
col1, col2 = st.columns(2)

# First column
with col1:
    st.header('Column 1')
    st.subheader('Bar Chart')
    
    fig, ax = plt.subplots()
    ax.bar(data['Category'], data['Values'], color='skyblue')
    ax.set_title('Bar Chart Example')
    st.pyplot(fig)
    
    st.subheader('Line Chart')
    
    fig, ax = plt.subplots()
    ax.plot(data['Category'], data['Values'], marker='o', linestyle='-', color='green')
    ax.set_title('Line Chart Example')
    st.pyplot(fig)

# Second column
with col2:
    st.header('Column 2')
    st.subheader('Scatter Plot')
    
    fig, ax = plt.subplots()
    ax.scatter(data['Category'], data['Values'], color='red')
    ax.set_title('Scatter Plot Example')
    st.pyplot(fig)
    
    st.subheader('Pie Chart')
    
    fig, ax = plt.subplots()
    ax.pie(data['Values'], labels=data['Category'], autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightblue', 'lightgreen'])
    ax.set_title('Pie Chart Example')
    st.pyplot(fig)

# Gallery section for additional graphs
st.header('Gallery of Graphs')

gallery_col1, gallery_col2 = st.columns(2)

# First graph in gallery
with gallery_col1:
    st.subheader('Histogram')
    
    hist_data = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.hist(hist_data, bins=30, color='purple')
    ax.set_title('Histogram Example')
    st.pyplot(fig)

# Second graph in gallery
with gallery_col2:
    st.subheader('Box Plot')
    
    box_data = [np.random.randn(100) for _ in range(4)]
    fig, ax = plt.subplots()
    ax.boxplot(box_data)
    ax.set_title('Box Plot Example')
    st.pyplot(fig)
