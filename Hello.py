
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


st.title("Hello world")
st.write('This My first App Deploy')
v = st.slider('Select voltage')
i = v = st.slider('Select current')
p = v*i
st.text(p)
st.write('Power curve')
plt.plot(p)
