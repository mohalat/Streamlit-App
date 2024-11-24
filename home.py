import streamlit as st
from PIL import Image

image = Image.open(r"c:\Users\User01\Downloads\2024-11-17 at 8.18.32 PM.jpeg")
st.image(image, width = 700) 

def home_page():
    st.title("Embedded ML model in GUIs --using streamlit")

    st.markdown(""" 
    This app uses machine learning to predict whether a customer is likely to churn or not.
    """)

    st.subheader("Instructions")
    st.markdown("""
    - Upload a csv file
    - Select the features for classification
    - Choose a machine learning model from the dropdown
    - Click on 'Classify' to get the predicted results
    - The app gives you a report on the performance of the model
    - Expect it to give metrices like f1 score, precision, recall, and accuracy
    """)

    st.header("App Features")
    st.markdown("""
    - **Data View**: Access the customer data.
    - **Predict View**: Shows the various models & predictions you will make.
    - **Dashboard**: Shows data visualization for insights.
    """)

    st.subheader("User Benefits")
    st.markdown("""
    - **Data Driven Decisions**: You make an informed decision backed by data
    - **Access Machine Learning**: Utilize machine learning algorithms 
    """)

    st.write("### HOW TO USE THIS APP")
    with st.container(border=True):
        st.code("""
        # Activate the virtual environment
        env/Scripts/activate

        # Run the app
        streamlit run app.py
        """)
    # Adding a video using the link
    st.video("https://www.youtube.com/watch?v=wlZhfMo98zs&ab_channel=DisneyJr.", autoplay=True)

    # Adding a clickable video
    st.markdown("Watch a demo__ [here](https://www.youtube.com/watch?v=wlZhfMo98zs&ab_channel=DisneyJr.)")
    st.subheader("Author: Abdul")

    # Adding an image using the path / way 1
    st.image(r"C:\Users\User01\Downloads\Downloads\download.png")

    # Way 2
    # install pillow -- from PIL import Image
    #image = Image.open(r"c:\Users\user\Pictures\2024-10-16 191911.png")
    #st.image(image, width = 100) 

    # Adding a contact/personal details
    st.divider()
    st.write("+++" * 27)
    st.write("Need Help?")
    st.write("Contact me on:")
    st.write("Call: 123-456-7890")
    st.write("Email: [Lwz5S@example.com](mailto:Lwz5S@example.com)")