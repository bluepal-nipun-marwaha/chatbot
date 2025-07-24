import streamlit as st
import sqlite3
import subprocess
import signal
import os
import json

# DB Setup
conn = sqlite3.connect('emails.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS emails (
        name TEXT PRIMARY KEY,
        email TEXT NOT NULL
    )
''')
conn.commit()

# Functions
def add_email(name, email):
    try:
        cursor.execute("INSERT INTO emails (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def reset_email():
    try:
        cursor.execute('DELETE FROM emails')
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def get_all_emails():
    cursor.execute('SELECT * FROM emails')
    return cursor.fetchall()

def write_emails():
    mail_list = get_all_emails()
    with open('email_list.json',  'w') as f:
        json.dump(mail_list, f)

# Streamlit App
st.title('📧 Mail Reader')

st.write('')

if 'monitor_process' not in st.session_state:
    st.session_state.monitor_process = None

st.write('Press this button to start monitoring the emails')

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('MONITOR'):
        if st.session_state.monitor_process is None or st.session_state.monitor_process.poll() is not None:
            write_emails()
            st.session_state.monitor_process = subprocess.Popen(['python', 'monitor.py'])
            st.success("Monitoring started.")
        else:
            st.info("Already running.")

with col2:
    if st.button('STOP'):
        proc = st.session_state.monitor_process
        if proc and proc.poll() is None:
            if os.name == "nt":  # Windows
                proc.terminate()
            else:  # Unix/Linux/macOS
                os.kill(proc.pid, signal.SIGTERM)
            st.session_state.monitor_process = None
            st.success("Monitoring stopped.")
        else:
            st.info("Nothing is running.")
    
if st.session_state.monitor_process and st.session_state.monitor_process.poll() is None:
    st.markdown("⏳ Monitoring is running...")
else:
    st.markdown("✅ Monitoring is stopped.")
        
st.write('')

st.subheader('Enter emails to monitor')
name = st.text_input('Enter the Name')
mail = st.text_input('Enter the Email')

if st.button("✅ Save and Continue"):
    if name and mail:
        success = add_email(name, mail)
        if success:
            st.success(f"Saved: {name} → {mail}")
        else:
            st.warning("Name already exists. Use a unique name.")
    else:
        st.warning("Please enter both name and email.")

st.write('')

if st.button('RESET'):
    success = reset_email()

st.write("### Monitored Emails")
email_list = get_all_emails()
for n, e in email_list:
    st.write(f"**{n}**: {e}")