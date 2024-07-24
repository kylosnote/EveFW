import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

with st.container(border=True):
    st.markdown('''
    This is a Todo page for upcoming changes to the site. At the moment no new feature are in plan yet.
    I will see if I get any feedback and suggestion and apply changes accordingly.

''')