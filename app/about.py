import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

with st.container(border=True):
    st.markdown('''
    ### Intro
    I am a long time Eve player with software engineering background. I mainly play PVE content such as abbysal and escalation.
    I also enjoy Faction Warfare content. However I am Alpha player so my gameplay is limited to the skill i have access to. With that being say,
    I personally enjoyed 1v1 small ship PVP. I decided to make these data out of curiosity and to hone my coding skill. Hopefully it is useful for some of you.
    
    ### Source Code
    The source code for the streamlit app and script I used to retrieve data are available on my github rep
    I must warn you though, the code is really messy and a lot of the task is done manually.
    Github(https://github.com/)
                
    ### Tool
    Following is the 3rd party site I used for retrieving data.
    - https://docs.everef.net/
    - https://esi.evetech.net/ui/
                
    ### Support & Feedback
    For any feedback and issue feel free to mail my Eve character IGN rekindlef2p Donation are welcome!😊
    ''')
