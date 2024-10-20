import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Function to get Google Sheets data
def get_gsheet_data(spreadsheet_id, worksheet_name):
    # Define the scope of the application
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Load the credentials from Streamlit secrets
    creds = {
        "type": st.secrets["connections"]["gsheets"]["type"],
        "project_id": st.secrets["connections"]["gsheets"]["project_id"],
        "private_key_id": st.secrets["connections"]["gsheets"]["private_key_id"],
        "private_key": st.secrets["connections"]["gsheets"]["private_key"].replace("\\n", "\n"),  # Ensure proper newline characters
        "client_email": st.secrets["connections"]["gsheets"]["client_email"],
        "client_id": st.secrets["connections"]["gsheets"]["client_id"],
        "auth_uri": st.secrets["connections"]["gsheets"]["auth_uri"],
        "token_uri": st.secrets["connections"]["gsheets"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["connections"]["gsheets"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["connections"]["gsheets"]["client_x509_cert_url"]
    }
    
    # Create a service account credentials object
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds, scope)
    
    # Authorize the client
    client = gspread.authorize(credentials)
    
    # Open the spreadsheet by ID
    spreadsheet = client.open_by_key(spreadsheet_id)
    
    # Open the specified worksheet
    worksheet = spreadsheet.worksheet(worksheet_name)
    
    # Get all values from the worksheet
    data = worksheet.get_all_values()
    
    # Convert to DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # The first row is the header
    return df

# Streamlit UI
st.title('Google Sheets Data Viewer')

# Google Sheets configuration
spreadsheet_id = "1l2UR6oq9wZTavT-wbo0229KmVJPFqwlb7bg70C6nR8E"  # Your spreadsheet ID
worksheet_name = "Database-Contacts"  # The name of your worksheet

try:
    # Get Google Sheets data
    df_contacts = get_gsheet_data(spreadsheet_id, worksheet_name)

    # Display DataFrame in Streamlit
    st.subheader('Contacts Data')
    st.dataframe(df_contacts)
except Exception as e:
    st.error(f"Error reading Google Sheets: {e}")
