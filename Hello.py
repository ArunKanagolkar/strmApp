
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title(" ELE.POWER CALCULATION")
st.write('3ph AC power calculator')
v = st.slider('Select voltage')
i = st.slider('Select current')
option = st.selectbox(
    "Select type of power",
    ("Three phase", "Single phase"),
)

st.write("You selected:", option)
if option == 'Three phase':
  p = (1.73*v*i*0.85)/1000
  st.write('3ph AC power in KW')
  st.text(p)
else:
  p = (v*i*0.85)/1000
  st.write('1ph AC power in KW')
  st.text(p)
  
