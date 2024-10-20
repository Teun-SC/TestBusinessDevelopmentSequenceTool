import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json

# Function to get Google Sheets data
def get_gsheet_data(spreadsheet_id, worksheet_name):
    # Define the scope of the application
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Load the credentials from Streamlit secrets
    creds = json.loads(st.secrets["connections"]["gsheets"])  # Use the TOML formatted secret
    
    # Create a service account credentials object
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
    
    # Authorize the client
    client = gspread.authorize(credentials)
    
    # Open the spreadsheet by ID
    sheet = client.open_by_key(spreadsheet_id)
    
    # Select the worksheet
    worksheet = sheet.worksheet(worksheet_name)
    
    # Get all values from the worksheet
    data = worksheet.get_all_records()
    
    return pd.DataFrame(data)

# Streamlit app
st.title('Hallo')
st.markdown("Hallo2")

# Read from Google Sheets
spreadsheet_id = st.secrets["connections"]["gsheets"]["spreadsheet_id"]
worksheet_name = "Database-Contacts"  # Change this to your worksheet name

try:
    df_contacts = get_gsheet_data(spreadsheet_id, worksheet_name)
    st.write(df_contacts)  # Display the data
except Exception as e:
    st.error(f"Error reading Google Sheets: {e}")
