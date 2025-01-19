
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title(" ELE.POWER CALCULATION")
st.write('Single and Three phase AC power calculator')
v = st.slider('Select line voltage',min_value=1, max_value=500)
i = st.slider('Select line current',min_value=1, max_value=500)
pf = st.slider('Select line Power factor',min_value=0.1, max_value=1.0)
option = st.selectbox(
    "Select type of system",
    ("Three phase", "Single phase"),
)

st.write("You selected:", option)
if option == 'Three phase':
  p = (1.73*v*i*pf)/1000
  st.write('3ph AC power in KW')
  st.text(p)
else:
  p = (v*i*pf)/1000
  st.write('1ph AC power in KW')
  st.text(p)
  
