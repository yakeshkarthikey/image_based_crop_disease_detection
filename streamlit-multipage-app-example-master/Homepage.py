import pandas as pd
import streamlit as st 
from keras.models import load_model
from PIL import Image
import numpy as np
import hashlib
# from streamweb import _start

st.set_page_config(
    page_title="CROP DISEASE DETECTION",
    page_icon="🍀",
)

c=True

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('streamlit-multipage-app-example-master/data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


def home():
    option = st.selectbox(
                    'Enter the Crop Name',
                    ("",'Maize', 'Potato', 'Rice'))

    st.write('You selected:', option)

    o = option
    print(o)
    st.write(o)
    # st.title("Crop Disease Detection ")
    # st.subheader("Enter your Crop Image....")
    file = st.file_uploader("enter the image")
            

def main():
    s = ""
    st.title("Crop Disease Detection")
    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("Menu",menu)

    
    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password",type='password')
        
    
    
        if st.button("Login"):
            # if password == '12345':
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            print(result)
            if result:
                st.success("Sucessfully Logged in :)")
                if(st.sidebar.success("Logged in")):  
                    st.session_state["my_input"] = result[0][0]
                st.session_state["my_input"] = result[0][0]
                
            else:
                st.sidebar.error("wrong credentials try :<")
                st.sidebar.error("wrong credentials try")
                s+='0'
                st.write(s[0])        
        
        st.subheader("Check your user name and proceed")
        st.sidebar.success("Select a page above.")

        if "my_input" not in st.session_state:
            st.session_state["my_input"] = ""

        # my_input = st.text_input("your user name:", st.session_state["my_input"])
        my_input = st.session_state["my_input"]
        submit = st.button("proceed")
        if submit:
            st.write('click the Detector in the sidebar to detect the leaf disease.')
            st.session_state["my_input"] = my_input
            st.write("You have entered: ", my_input)
        
    
                            
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
        
            
    



if __name__ == '__main__':
    main()

	

