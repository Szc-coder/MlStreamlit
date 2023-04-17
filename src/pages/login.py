import streamlit as st
import streamlit_authenticator as stauth

import sys

sys.path.insert(0, '../')

import src.config as config

authenticator = stauth.Authenticate(config.test_users,
                                    config.Cookie_name,
                                    config.Cookie_key,
                                    config.Cookie_expiry_days,
                                    config.preauthorized_emails)

authenticator.login('Login🥾🥾🥾', 'main')

if st.session_state["authentication_status"]:
    st.title(f'Welcome *{st.session_state["name"]}*👋👋👋')

    if st.button('Update user details'):
        authenticator.update_user_details(st.session_state["username"], 'Update user details')

    authenticator.logout('Logout', 'main')
    

if st.session_state["authentication_status"] is None:
    try:
        if authenticator.register_user('Register user😎😎😎', preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)

if st.session_state["authentication_status"] is None:
    try:
        username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password😶‍🌫😶‍🌫😶‍🌫') 
        if username_forgot_pw:
            st.success('Password reset successfully') 
    except Exception as e:
        st.error(e)
    