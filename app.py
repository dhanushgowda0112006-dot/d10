import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from analysis import *

st.set_page_config(
    page_title="Cricket Data Analyzer",
    layout="wide"
)

st.title("🏏 Cricket Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload Cricket CSV File",
    type=["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success("File Uploaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    info = basic_info(df)

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", info["Rows"])
    col2.metric("Columns", info["Columns"])
    col3.metric("Missing Values", info["Missing Values"])

    st.subheader("Statistical Summary")

    st.dataframe(numeric_summary(df))

    st.subheader("Column Selection")

    column = st.selectbox(
        "Choose Column",
        df.columns
    )

    st.subheader("Value Counts")

    st.bar_chart(df[column].value_counts().head(10))

    st.subheader("Top 10 Categories")

    top = top_players(df)

    if top is not None:
        st.bar_chart(top)

    st.subheader("Correlation Heatmap")

    corr = correlation(df)

    if corr is not None:

        fig, ax = plt.subplots(figsize=(8,5))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)

    st.subheader("Missing Values")

    st.dataframe(df.isnull().sum())

else:
    st.info("Upload a cricket CSV file to start analysis.")
