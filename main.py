import sqlite3
import streamlit as st

conn = sqlite3.connect("crud.db")
cursor = conn.cursor()

query = """ CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"emailid"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
); """

cursor.execute(query)


def adduser(name, email):
    insert_query = "INSERT INTO user (name, emailid) VALUES (?, ?)"
    cursor.execute(insert_query, (name, email))
    conn.commit()


def Create_User():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.title("Create User")
        getname = st.text_input("Enter the Name")
        getemail = st.text_input("Enter the Email")
        if st.button("Add user"):
            adduser(getname, getemail)
            st.success("User Added Success")


    with col2:
        st.title("Table")
        query = "SELECT * from user"
        cursor.execute(query)
        getdata = cursor.fetchall()
        st.table(getdata)


def Update_User():
    col1, col2 = st.columns([1,2])
    with col1:
        st.write("# Update User")
        query = "SELECT * from user"
        cursor.execute(query)
        getData = cursor.fetchall()
        datas = [item[1] for item in getData]
        user_selected = st.selectbox("Choose User", datas)
        email = st.text_input("Enter the Email")
        if st.button("Update User"):
            update_query = "UPDATE user SET emailid = ? WHERE name = ?"
            cursor.execute(update_query, (email, user_selected))
            conn.commit()

    with col2:
        st.write("# Name: ", f" {user_selected}")
        st.table(getData)

def Delete_User():
    st.write("# Delete User")



st.set_page_config(page_title="Database Connection", page_icon="🦈", layout="wide")


st.sidebar.write("# iamdev")
selected_page = st.sidebar.selectbox('Choose Option', ['Create User', 'Update User', 'Delete User'])

if selected_page == "Create User":
    Create_User()

elif selected_page == "Update User":
    Update_User()

elif selected_page == "Delete User":
    Delete_User()

