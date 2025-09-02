import streamlit as st
st.title("Machine Learning Project")

from PIL import Image
img= Image.open("1.jpg")
# st.image(img)
st.image(img,width = 300, caption = "Sample Image") 
vid_file = open("PBD.mp4", "rb")
vid_bytes  = vid_file.read ()
st.video(vid_bytes)

audio_file = open("Hare Krishna.m4a", "rb")
st.audio(audio_file)

#ML(Gender,  M/F)
# checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing/hiding widget")

# radiobox
status = st.radio("What is your Status",("Active","Inactive"))

if status=="Active":
    st.success("You are Active")

if status=="Inactive":
    st.warning("You are inactive, Active it !!")

#selectBox
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Scientist", "Doctor", "Businessman"])
st.write("You selected this option", occupation)

#multiselect
location = st.multiselect("Where do you live", ["Karnataka", "Mumbai", "Pune", "Delhi"])

st.write("You selected", len(location),"location")

#Slider
level=st.slider("What is your level",1,5)

#Buttons
st.button("Submit your form")
if st.button("About"):
    st.text("Streamlot is cool")

if st.button("Submit"):
    st.text("Successful submitted")

first_name = st.text_input("Enter your first name", "Type here...")
if st.button("submit", key='1'):
    result = first_name.title()
    st.success(result)

#text arena
message= st.text_area("Enter your message", "Type here...")
if st.button("Submit", key="2"):
    result = message.title()
    st.success(result)

import datetime
today = st.date_input("Today is", datetime.datetime.now())

# Time
the_time=st.time_input("The time is", datetime.time())

#Display Json Output
st.text("Display json Data")
st.json({"Name":"Shivam",
        "Gender":"Male"})

# #import numpy as np
# st.text("Display Row Code")
# st.code("import numpy as np")

#Display row code with dataframe
with st.echo():
    import pandas as pd
    df = pd.DataFrame()

#Progress bar

import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+10)

#pinner
with st.spinner("Waiting .."):
    time.sleep(5)
st.success("Finished")



