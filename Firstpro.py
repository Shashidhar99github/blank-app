import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20)),
)
st.table(dataframe.style.highlight_max(axis=0))

st.write(":balloon: Next Table :balloon:")
df = np.random.randn(5,5)
st.table(df)