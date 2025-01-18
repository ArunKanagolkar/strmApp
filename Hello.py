
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title(" POWER CALCULATION")
st.write('3ph AC power calculator')
v = st.slider('Select voltage')
i = v = st.slider('Select current')
p = 1.73*v*i*0.85
st.write('3ph AC power')
st.text(p)
