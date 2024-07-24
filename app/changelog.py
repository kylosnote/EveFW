import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

with st.container(border=True):
    st.markdown('''
    ### 23-July-2024
    - Initial Release for Tier 1 Frigate, Destroyer and Cruiser Solo Kill data.
''')