import streamlit as st
import mysql.connector
import os

DB_CONFIG = {
    'host': os.environ.get("DB_HOST", "localhost"),
    'user': os.environ.get("DB_USER", "root"),
    'password': os.environ.get("DB_PASSWORD", "h17328"),
    'database': os.environ.get("DB_NAME", "yt")
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

st.title("Student Marks Entry Form")

with st.form("student_form"):
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["M", "F"])
    dob = st.date_input("Date of Birth")
    maths = st.number_input("Maths Score", min_value=0, max_value=100, step=1)
    physics = st.number_input("Physics Score", min_value=0, max_value=100, step=1)
    chemistry = st.number_input("Chemistry Score", min_value=0, max_value=100, step=1)
    english = st.number_input("English Score", min_value=0, max_value=100, step=1)
    biology = st.number_input("Biology Score", min_value=0, max_value=100, step=1)
    economics = st.number_input("Economics Score", min_value=0, max_value=100, step=1)
    history = st.number_input("History Score", min_value=0, max_value=100, step=1)
    civics = st.number_input("Civics Score", min_value=0, max_value=100, step=1)
    
    submit_button = st.form_submit_button("Submit")

if submit_button:
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO StudentMarks (Name, Gender, DOB, Maths, Physics, Chemistry, English, Biology, Economics, History, Civics)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, gender, dob, maths, physics, chemistry, english, biology, economics, history, civics)
        cursor.execute(query, values)
        conn.commit()
        st.success("Student marks added successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error inserting data: {err}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
