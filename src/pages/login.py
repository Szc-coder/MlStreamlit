import streamlit as st
import streamlit_authenticator as stauth

import sys

sys.path.insert(0, '../')

import src.config as config

import sqlite3

conn = sqlite3.connect('mlst_user.db')
cu = conn.cursor()

authenticator = stauth.Authenticate(config.test_users,
                                    config.Cookie_name,
                                    config.Cookie_key,
                                    config.Cookie_expiry_days,
                                    config.preauthorized_emails)

authenticator.login('Login🥾🥾🥾', 'main')

if st.session_state["authentication_status"]:
    try:
        cmd = "SELECT * FROM users"
        cu.execute(cmd)
        login_user = cu.fetchall()
        login_user = [i for i in login_user if i[0] == st.session_state["username"]][0]

        st.session_state['email'] = login_user[1]
    except Exception as e:
        st.warning(e)

if st.session_state["authentication_status"]:
    st.title(f'Welcome *{st.session_state["name"]}*👋👋👋')

    authenticator.update_user_details(st.session_state["username"], 'Update user details')
    # update to database
    new_name = st.session_state["name"]
    new_email = st.session_state["email"]

    cu.execute('UPDATE users SET name = ?, email = ? WHERE username = ?',
               (new_name, new_email, st.session_state["username"]))
    conn.commit()

    authenticator.logout('Logout', 'main')

if st.session_state["authentication_status"] is None:
    try:
        new_user_name = authenticator.register_user('Register user😎😎😎', preauthorization=False)
        new_user_data = config.test_users['usernames'][new_user_name]

        cmd = f"INSERT INTO users VALUES ('{new_user_name}', '{new_user_data['email']}', '{new_user_data['name']}', '{new_user_data['password']}')"

        cu.execute(cmd)
        conn.commit()
        st.success('User registered successfully')
    except Exception as e:
        pass

    # try:
    #     username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password(
    #         'Forgot password😶‍🌫😶‍🌫😶‍🌫')
    #     if username_forgot_pw:
    #         st.success('Password reset successfully')
    # except Exception as e:
    #     st.error(e)

cu.close()
