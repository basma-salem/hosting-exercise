import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('Simple Streamlit App')

st.write("Here's our first attempt at using Streamlit to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    
    st.header("FastAPI Integration Example")
if st.button('Call FastAPI'):
    response = requests.get('https://hosting-exercise-3hnp.onrender.com/')
    if response.status_code == 200:
        st.success(f"FastAPI Response: {response.json()}")
    else:
        st.error("Failed to connect to FastAPI")