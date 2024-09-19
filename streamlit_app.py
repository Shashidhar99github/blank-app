import streamlit as st
import pandas as pd
import numpy as np
st.write("This is my first code to execute and run in Streamlit")
df = pd.DataFrame({
    'First column':[1,2,3,4,5],
    'Second column':[19,28,18,16,62],
    'Third column':[20,10,29,18,18]
})
st.table(df)
# df

dataframe = np.random.randn(5,5)
st.dataframe(dataframe)

DataF=pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(DataF.style.highlight_max(axis=0))