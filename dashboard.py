import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dashboard_page():
    st.title("Dashboard")

    # Load data table for dashboard
    data = pd.read_csv("data/train_copy.csv")

    st.header("Data Overview")
    st.write("Here is a summary of the dataset")
    st.dataframe(data.head())


    # Plot correlation
    st.subheader("Correlation Heatmap")
    corr = data[["tenure", "TotalCharges", "MonthlyCharges"]].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap ="coolwarm")
    st.pyplot(plt)

    st.subheader("Churn Count")
    churn_count = data['Churn'].value_counts()
    st.bar_chart(churn_count)

    # Plot distribution of tenure
    st.subheader("Distribution of Tenure")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['tenure'], kde=True)
    st.pyplot(plt)

    # Plot distribution of monthly charges
    st.subheader("Distribution of Monthly Charges")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['MonthlyCharges'], kde=True)
    st.pyplot(plt)

    # Plot distribution of total charges
    st.subheader("Distribution of Total Charges")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['TotalCharges'], kde=True)
    st.pyplot(plt)