import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from urllib.error import HTTPError


st.title('Hallo')
st.markdown("Hallo2")
conn = st.connection("gsheets", type = GSheetsConnection)

print(st.secrets["gsheets"]['spreadsheet'])

try:
    df_contacts = conn.read(spreadsheet=st.secrets["gsheets"]['spreadsheet'])
except HTTPError as e:
    st.error(f"Failed to connect to Google Sheets: {e}")

