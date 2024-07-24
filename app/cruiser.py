import streamlit as st
from st_pages import Page, add_page_title, show_pages
import pandas as pd

add_page_title() 

# Default styling
headers = {
    'selector': 'th:not(.index_name)',
    'props': 'background-color: blue; color: red;'
 }#TODO Not working

coloring = {'background-color': 'black',
                                'color': 'cyan',
                                'border-color': 'white'}

def get_monthly_component(month:str, title:str):
    st.header(title)

    overview,tab1,tab2,tab3,tab4 = st.tabs(["Overview","Attacker","Victim", "System", "Faction"])

    with overview:
        overview = pd.read_json(f"./data/{month}/cruiser_overview.json")
        overview_final = overview.style.set_properties(**coloring).set_table_styles([headers])

        st.subheader("Overview")
        st.dataframe(overview_final, hide_index=True, column_config={1:"Total", 2:"Attacker", 3:"Victim"})

    with tab1:
        cruiser_attacker_rank = pd.read_json(f"./data/{month}/cruiser_attacker_rank.json")

        final = cruiser_attacker_rank.style.set_properties(**coloring).set_table_styles([headers])

        st.subheader("Top Attacker Rank")
        st.dataframe(final, hide_index=True, column_config={ 1:"Total", 2:"Ship"})
        # with st.expander("See explanation"):
        #     st.write('''
        #         The chart above shows some numbers I picked for you.
        #         I rolled actual dice for these, so they're *guaranteed* to
        #         be random.
        #     ''')
        
        st.divider()

        st.subheader("Most Popular Weapon")
        attacker_weapon_rank =  pd.read_json(f"./data/{month}/cruiser_attacker_weapon_rank.json")
        final_attacker_weapon = attacker_weapon_rank.style.set_properties(**coloring).set_table_styles([headers])
        st.dataframe(final_attacker_weapon, hide_index=True, column_config={ 1:"Total", 2:"Attacker", 3:"Weapon", 4:"Victim"})
        # with st.expander("See explanation"):
        #     st.write('''
        #         The chart above shows some numbers I picked for you.
        #         I rolled actual dice for these, so they're *guaranteed* to
        #         be random.
        #     ''')

    with tab2:
        victim_rank = pd.read_json(f"./data/{month}/cruiser_victim_rank.json")
        victim_final = victim_rank.style.set_properties(**coloring).set_table_styles([headers])
        
        st.subheader("Top Victim Rank")
        st.dataframe(victim_final, hide_index=True, column_config={ 1:"Total", 2:"Ship"})
        
        # with st.expander("See explanation"):
        #     st.write('''
        #         The chart above shows some numbers I picked for you.
        #         I rolled actual dice for these, so they're *guaranteed* to
        #         be random.
        #     ''')
        
        st.divider()

    with tab3:
        system_rank = pd.read_json(f"./data/{month}/cruiser_system_rank.json")
        system_final = system_rank.style.set_properties(**coloring).set_table_styles([headers])

        st.subheader("Most Popular System")
        st.dataframe(system_final, hide_index=True, column_config={ 1:"Total", 2:"System"})
        # with st.expander("See explanation"):
        #     st.write('''
        #         The chart above shows some numbers I picked for you.
        #         I rolled actual dice for these, so they're *guaranteed* to
        #         be random.
        #     ''')

    with tab4:
        st.subheader("Attacker Faction Rank")
        attacker_faction_rank = pd.read_json(f"./data/{month}/cruiser_attacker_faction_rank.json")
        attacker_faction_final = attacker_faction_rank.style.set_properties(**coloring).set_table_styles([headers])
        st.dataframe(attacker_faction_final, hide_index=True, column_config={ 1:"Total", 2:"Faction"})

        # with st.expander("See explanation"):
        #     st.write('''
        #         The chart above shows some numbers I picked for you.
        #         I rolled actual dice for these, so they're *guaranteed* to
        #         be random.
        #     ''')
        st.subheader("Victim Faction Rank")
        victim_faction_rank = pd.read_json(f"./data/{month}/cruiser_victim_faction_rank.json")
        victim_faction_final = victim_faction_rank.style.set_properties(**coloring).set_table_styles([headers])
        st.dataframe(victim_faction_final, hide_index=True, column_config={ 1:"Total", 2:"Faction"})

        # with st.expander("See explanation"):
        #     st.write('''
        #         The chart above shows some numbers I picked for you.
        #         I rolled actual dice for these, so they're *guaranteed* to
        #         be random.
        #     ''')


with st.container(border=True):
    get_monthly_component(month='6', title='June 2024')


with st.container(border=True):
    get_monthly_component(month='5', title='May 2024')
