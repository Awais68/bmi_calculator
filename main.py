import streamlit as st
import pandas as pd

# st.set_page_config( page_icon="📟", title="BMI_cALCULATOR", layout="wide")

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="📟",  # Emoji or path to image file
    layout="centered"
)


footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #555;
    text-align: center;
    padding: 10px;
    font-size: 14px;
    border-top: 1px solid #ddd;
}
</style>
<div class="footer">
    ALl Rights Reserved © 2025 AS Developers | <a href="https://www.linkedin.com/feed/" target="_blank">More Info</a>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
st.header("Welcome to the BMI CALCULATOR App! ⚖️")  

height = st.slider("Enter your height (in cm):",100, 250, 175)
weight = st.slider("Enter Your weight (in Kg):", 40, 200, 70)

bmi = weight / ((height/100) **2)

st.write(f" Your BMI is {bmi:.2f}  ")


st.write( "### BMI Categories ###")
st.write("- Underweight: BMI less than 10.5")
st.write("- Normal weight: BMI Between 18.5 and 24.9")
st.write("- Overweight: BMI Between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")


st.write("create by AS Developers")

