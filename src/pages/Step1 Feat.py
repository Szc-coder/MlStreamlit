import streamlit as st

try:
    if st.session_state["authentication_status"]:
        st.title(f'Welcome *{st.session_state["name"]}*👋👋👋')




except:
    st.warning('Please to login first')
