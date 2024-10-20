import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


st.title('Hallo')
st.markdown("Hallo2")
conn = st.connection("gsheets", type = GSheetsConnection)
df_contacts = conn.read(spreadsheet= st.secrets["gsheets"]['spreadsheet '])

