# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:47:18 2023

@author: 331830
"""

import streamlit as st
import pandas as pd
import time
from schedule import every, repeat, run_pending

st.write("""
# My first app
Power Hello *world!* NRaDy Power Refresh sec
""")

with st.empty():
    @repeat(every(10).seconds)
    def plot_line_chart():
        df = pd.read_csv("my_data.csv")
        st.line_chart(df)
    plot_line_chart()
    while True:
        run_pending()
        time.sleep(1)