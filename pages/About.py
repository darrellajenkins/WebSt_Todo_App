import streamlit as st
import webbrowser


# Sample additional website page.

def goto():
	search = st.session_state["search"]
	webbrowser.open(f"https://duckduckgo.com/{search}?ia=web")


st.title("About")
st.subheader("Would you like to learn more about the Developer?")
select = st.radio('Select', options=['Other','Yes', 'No'])
if select == 'Other':
	st.write("You can now search the web. Enter your query below.")
	st.text_input(label="Search:", on_change=goto, key="search")


if select == 'Yes':
	webbrowser.open('https://github.com/darrellajenkins')
st.write("\n\n\n\n")
st.write(f"<b> {chr(169)} 2024 Inpyosis LLC<b/>",
         unsafe_allow_html=True)
