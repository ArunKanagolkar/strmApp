

import streamlit as st
import mymodel as m

st.write("Hello world")
st.write('This My first App Deploy')
w = st.slider('Forecast with Days')
f = w*2
st.write(m.run(windows=f))
