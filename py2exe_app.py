import streamlit as st 
import os

st.title("Convert Python code to exe")

python_file = st.selectbox('Select a file', os.listdir('.'))

if st.button("Convert .py to .exe"):
	st.write('You selected `%s`' % python_file)
	os.system("pyinstaller --onefile -w " + python_file )
	st.write('Converted file is saved in /dist directory')