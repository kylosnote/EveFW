import streamlit as st
from st_pages import Page, add_page_title, show_pages
import pandas as pd
import altair as alt

add_page_title(layout="wide")

show_pages(
    [
        Page("./app/app.py", "Home", "🏠"),
        Page("./app/frigate.py", "Frigate", ""),
        Page("./app/destroyer.py", "Destroyer", ""),
        Page("./app/cruiser.py", "Cruiser", ""),
        Page("./app/about.py", "About", ""),
        Page("./app/todo.py", "Todo", ""),
        Page("./app/changelog.py", "Changelog", "")
    ]
)


with st.container(border=True):
    st.header("Overview")

    #TODO:auto loop available data
    #Show total number of 1v1 PVP of each ship class each month
    may = pd.read_json(f"./data/5/all_overview.json")
    may.columns = ["Total", "Ship Type"]
    may.insert(loc=2,column="Month", value="May", allow_duplicates=True)

    june = pd.read_json(f"./data/6/all_overview.json")
    june.columns = ["Total", "Ship Type"]
    june.insert(loc=2,column="Month", value="June", allow_duplicates=True)
    all_overview = pd.concat([may,june])

    # st.altair_chart(data=all_overview, x="Month", y=["Ship Type", "Total"],)
    chart = alt.Chart(all_overview).mark_bar().encode(
        x="Month:N",
        y= "Total:Q",
        xOffset="Ship Type:N",
        color="Ship Type:N"
    )
    st.altair_chart(chart)

    st.divider()

    st.markdown(
        '''
        This site is focus on data related to solo kill among T1 same ship class. 
        The data I retrieve is start from May as I started working on this project in June.
        '''
    )