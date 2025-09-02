import streamlit as st
st.title("Happy Birthday")

st.balloons()

st.sidebar.header("About")
st.sidebar.text("This is our demo project")

algorithm = st.sidebar.selectbox("Your Algorithm", ["Linear regression","Logistic Regression", "Desion Tree", "Random Forest"])

st.sidebar