import streamlit as st
st.title("Machine Learning Project")
st.header("Regreesion model tutorial")
st.subheader("Definition of regression model")
st.text("Hello Srtewdslk")
st.markdown("# this od my first makdown")
st.markdown("## this od my first makdown")
st.markdown("#### this od my first makdown")

st.success("successful")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error")
st.exception("NameError('name pd is not defined')")


import pandas
st.help(pandas)

st.help(range)

st.write("Text with Write")

st.write(range(10))

from PIL import Image
img= Image.open("1.jpg")
st.image(img)