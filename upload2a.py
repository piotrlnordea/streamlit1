# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:35:21 2022

@author: piotr
"""
import os
import streamlit as st
#uploaded_files = st.file_uploader("Choose all cv files in doc, docx, pdf format", accept_multiple_files=True)


def save_uploadedfile(uploadedfile):
    with open(os.path.join('.\\', uploadedfile.name), 'wb') as f:
        f.write(uploadedfile.getbuffer())
        return st.success('Saved File:{} to Data'.format(uploadedfile.name))

st.title('upload CV files to be analysed')
st.text(' A simple way to upload CV files directly into a directory')
uploadedfiles = st.file_uploader('Upload PDF, doc,docx', type=['pdf','doc', 'docx'], accept_multiple_files=True)
for file in uploadedfiles:
    if uploadedfiles is not None:
        save_uploadedfile(file)
        
#process files!!
uploaded_file=  uploadedfiles     
uploaded_file = st.file_uploader('.\\allfiles.sum')
st.write('ttttttttttttttttt')

if uploaded_file:
    for line in uploaded_file:
        st.write(line)
        
        
st.write('THis Streamlit')

st.success('Success')

with open('.\\allfiles.sum') as f:
    st.write(f.readline())