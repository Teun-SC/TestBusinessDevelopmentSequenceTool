import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from urllib.error import HTTPError


st.title('Hallo')
st.markdown("Hallo2")
conn = st.connection("gsheets", type = GSheetsConnection)



# df_contacts = conn.read(spreadsheet=st.secrets["gsheets"]['spreadsheet'], worksheet='Database-Contacts')
# df_contacts = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1l2UR6oq9wZTavT-wbo0229KmVJPFqwlb7bg70C6nR8E/edit?gid=0#gid=0", worksheet='Database-Contacts')


