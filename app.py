import streamlit as st
# import os
import pandas as pd

st.set_page_config(layout = "wide")

st.header("The XYZ.com")

content = """
    Imagine XYZ.com, a cutting-edge online accounting program revolutionizing the way individuals and small businesses handle their taxes. Much like TurboTax, XYZ.com simplifies tax filing with an intuitive, user-friendly interface that takes the stress out of financial management. Users can effortlessly navigate through complex tax codes, ensure maximum deductions, and receive real-time guidance from virtual tax experts. XYZ.com offers secure, cloud-based storage for all your financial documents, making it easy to access your information from anywhere, at any time. With advanced features like automated expense tracking, personalized tax tips, and seamless integration with popular accounting software, XYZ.com is your trusted partner for a hassle-free tax season. Say goodbye to paperwork and hello to financial peace of mind with XYZ.com!
"""

st.write(content)

st.subheader("The Team")
col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv")

with col1:
    for image, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for image, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for image, row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("images/" + row["image"])
