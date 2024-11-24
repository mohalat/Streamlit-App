import streamlit as st
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page
from auth import authenticate


# Assigning to the appropriate pages
def main():
    authenticate()          # Authenticate user credentials
    if st.session_state.authenticated:
        # Creating a sidebar
        st.sidebar.title("Navigator")
        st.sidebar.write("Select a page")
        page = st.sidebar.selectbox("Navigate", ["Home", "Data", "Predict", "Dashboard"])

        if page == "Home":
            home_page()
        elif page == "Data":
            data_page()
        elif page == "Predict":
            predict_page()
        elif page == "Dashboard":
            dashboard_page()


if __name__ == "__main__":
    main()